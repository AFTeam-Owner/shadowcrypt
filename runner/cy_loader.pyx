from cpython.mem cimport PyMem_Malloc, PyMem_Free
from libc.stdio cimport FILE, fopen, fread, fclose, fseek, ftell, SEEK_END, SEEK_SET
from libc.string cimport memset, fgets
import sys
import os
import struct
import base64
import subprocess

BLOCK_SIZE = 16
ROUNDS = 20

cdef unsigned char SINE_TABLE[256]
cdef unsigned char COSINE_TABLE[256]

def _init_tables():
    import math
    cdef int i
    for i in range(256):
        SINE_TABLE[i] = <unsigned char>int((math.sin(i / 256.0 * 2 * math.pi) + 1) * 127.5) & 0xFF
        COSINE_TABLE[i] = <unsigned char>int((math.cos(i / 256.0 * 2 * math.pi) + 1) * 127.5) & 0xFF

cdef unsigned char complex_transform_inverse(unsigned char b, int round_num):
    cdef int x
    cdef unsigned char val
    for x in range(256):
        val = (x * 7 + 13 + SINE_TABLE[(x + round_num) % 256]) % 256
        val = (val + COSINE_TABLE[(val * round_num) % 256]) % 256
        val = val ^ ((round_num * 31) & 0xFF)
        if val == b:
            return <unsigned char>x
    return 0

cdef bytes inverse_permute_block(bytes block):
    cdef int perm[16] = [3, 7, 12, 1, 14, 0, 9, 5, 11, 2, 15, 8, 6, 13, 4, 10]
    cdef unsigned char inv[16]
    cdef int i
    for i in range(16):
        inv[perm[i]] = i
    cdef unsigned char res[16]
    for i in range(16):
        res[i] = block[inv[i]]
    return bytes(res)

cdef bytes decrypt_block(bytes block, int round_num):
    cdef bytes permuted = inverse_permute_block(block)
    cdef unsigned char res[16]
    cdef int i
    for i in range(16):
        res[i] = complex_transform_inverse(permuted[i], round_num)
    return bytes(res)

def simple_checksum(bytes data):
    cdef unsigned int csum = 0
    cdef int i
    for i in range(len(data)):
        csum = (csum + data[i]) & 0xFFFFFFFF
    return csum

def anti_debug():
    try:
        if sys.gettrace() is not None:
            return True
    except:
        pass
    if os.environ.get('LD_PRELOAD'):
        return True
    try:
        with open('/proc/self/status', 'r') as f:
            for line in f:
                if line.startswith('TracerPid:'):
                    tracerpid = int(line.split()[1])
                    if tracerpid != 0:
                        return True
    except:
        pass
    try:
        output = subprocess.check_output(['ps', 'aux'], text=True)
        debuggers = ['gdb', 'lldb', 'strace', 'ltrace', 'ida', 'ollydbg']
        for dbg in debuggers:
            if dbg in output:
                return True
    except:
        pass
    return False

def run_shc(str filepath):
    _init_tables()
    if anti_debug():
        print("Debugging detected. Exiting.")
        return

    cdef FILE* f = fopen(filepath.encode('utf-8'), b"rb")
    if not f:
        print("Failed to open file.")
        return

    cdef unsigned char header[56]
    cdef size_t read_bytes = fread(header, 1, 56, f)
    if read_bytes != 56:
        fclose(f)
        print("Invalid file format.")
        return

    cdef unsigned int checksum = struct.unpack('>I', bytes(header[0:4]))[0]
    cdef unsigned int version = struct.unpack('>I', bytes(header[4:8]))[0]
    cdef unsigned long long timestamp = 0
    cdef int i
    for i in range(8):
        timestamp = (timestamp << 8) | header[8 + i]

    fseek(f, 0, SEEK_END)
    cdef size_t file_size = ftell(f)
    cdef size_t data_size = file_size - 56
    fseek(f, 56, SEEK_SET)

    cdef unsigned char* encrypted_data = <unsigned char*>PyMem_Malloc(data_size)
    if not encrypted_data:
        fclose(f)
        print("Memory allocation failed.")
        return

    read_bytes = fread(encrypted_data, 1, data_size, f)
    fclose(f)
    if read_bytes != data_size:
        PyMem_Free(encrypted_data)
        print("Failed to read encrypted data.")
        return

    cdef bytes data = bytes([encrypted_data[i] for i in range(data_size)])
    PyMem_Free(encrypted_data)

    cdef int round_num
    for round_num in range(ROUNDS - 1, -1, -1):
        cdef bytearray new_data = bytearray()
        cdef int offset
        for offset in range(0, len(data), BLOCK_SIZE):
            block = data[offset:offset + BLOCK_SIZE]
            decrypted_block = decrypt_block(block, round_num)
            new_data.extend(decrypted_block)
        data = bytes(new_data)

    cdef unsigned int computed_checksum = simple_checksum(data)
    if computed_checksum != checksum:
        print("Checksum mismatch. File corrupted or tampered.")
        return

    cdef unsigned char padding_len = data[-1]
    if padding_len > 0 and padding_len <= BLOCK_SIZE:
        data = data[:-padding_len]

    try:
        code_str = data.decode('utf-8')
        code_str = base64.b64decode(code_str.encode('ascii')).decode('utf-8')
        code_obj = compile(code_str, filepath, 'exec')
        exec(code_obj, globals())
    except Exception as e:
        print("Execution error:", e)
</create_file>
