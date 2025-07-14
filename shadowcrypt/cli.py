import sys
import argparse
import os
from encryptor import encrypt
from runner import loader

def main():
    parser = argparse.ArgumentParser(prog='shadowcrypt', description='ShadowCrypt CLI - Author: 〲ɱ๏ɳᴀʳᴄʰ ⌾ғ sʜᴀᴅᵒʷˢ〴 [Monarch of Shadows]')
    subparsers = parser.add_subparsers(dest='command')

    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a Python file')
    encrypt_parser.add_argument('input', help='Input .py file')
    encrypt_parser.add_argument('-o', '--output', required=True, help='Output .shc file')

    run_parser = subparsers.add_parser('run', help='Run an encrypted .shc file')
    run_parser.add_argument('file', help='Encrypted .shc file to run')

    args = parser.parse_args()

    if args.command == 'encrypt':
        try:
            encrypt.encrypt_file(args.input, args.output)
        except Exception as e:
            print(f"Encryption failed: {e}")
            sys.exit(1)
    elif args.command == 'run':
        try:
            loader.run_shc(args.file)
        except Exception as e:
            print(f"Loader failed: {e}")
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
