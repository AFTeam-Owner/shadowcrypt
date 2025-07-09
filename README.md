<h1 align="center">
  🕶️ SHADOWCRYPT
</h1>

<p align="center">
  <i>Encrypt. Execute. Never Expose.</i><br/>
  The last encryption system you'll ever need for Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Security-Private%20Decryption%20Only-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/AI%20Safe-100%25-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Platform-All%20OS-green?style=flat-square"/>
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/shadowcrypt?style=social"/>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=YOUR_USERNAME.shadowcrypt"/>
</p>

---

## 🧠 What is ShadowCrypt?

> `shadowcrypt` is a **Python code encryptor** that turns `.py` files into **unreadable**, **uncrackable**, but still **executable** Python scripts.  
> Anyone can encrypt. Only **you** can decrypt.

---

## ⚙️ Features

- ✅ Encrypt `.py` into unreadable code
- ✅ Still works with `python encrypted.py`
- 🔒 Pure math encryption (no marshal, no base64, no eval)
- 🔐 Private decryption only — not even the encryptor can reverse it
- 🧠 Resistant to both AI and human reverse engineering
- 📱 Cross-platform: Windows, Linux, macOS, Android (Termux)

---

## 📦 Installation

```bash
pip install shadowcrypt
Or install from source:

```bash
git clone https://github.com/YOUR_USERNAME/shadowcrypt.git
cd shadowcrypt
pip install .
🔐 Encrypt your Python file

```bash
shadowcrypt encrypt yourfile.py -o locked.py
python locked.py
➡️ locked.py now runs like the original,
but no one can see or recover your source code.

🧪 Example

```bash
shadowcrypt encrypt ai_brain.py -o secret_run.py
python secret_run.py  # 🔥 Runs flawlessly


🛡 Security Design
⚠️ No base64, no marshal, no eval — only layered math

🔑 Randomized encryption per character

🔒 No decryptor or key ever included in public package

💥 Reverse engineering fails — always

Even if someone has the source code of the encryptor and encrypted file, they still can't decrypt it.

📜 License
MIT — Open-source and developer friendly
Built for creators who don’t want to be copied.

<p align="center"> <i>Crafted by</i><br/> 🧠 <b>Farhan Jihady</b><br/> 🔮 <code>The Cipher Architect</code> </p> ```
