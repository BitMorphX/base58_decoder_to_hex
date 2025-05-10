> ⚠️ This project is deprecated. Please see [btc_address_analyzer](https://github.com/BitMorphX/btc_address_analyzer) instead.

# 📌 Bitcoin Base58 to HEX Decoder

**Version:** 1.0.0

## Project Description

**base58_decoder_to_hex.py** is a Python script that decodes any Bitcoin address (in Base58Check format) into its raw hexadecimal components.

This tool was created for **educational purposes**, helping to better understand the structure of Bitcoin addresses.

---

## Features

- 🧠 Decodes Base58Check-encoded Bitcoin addresses
- 🛠️ Extracts Prefix, Public Key Hash (hash160), and Checksum
- ✅ Verifies checksum validity using double-SHA256
- 🎯 Supports CLI argument or interactive input
- 🎨 Terminal output with color highlights (cross-platform)

---

## Requirements

- 🐍 Python 3.6+

Install dependencies:

```bash
pip install base58 colorama
```

---

## Usage

### Run from terminal:

```bash
python base58_decoder_to_hex.py
```

---

## Output Example

```
📦 Decoded Bitcoin Address:
├─ Prefix (HEX):           00
├─ Public Key Hash (HEX):  <decoded_hash160_here>
├─ Checksum (HEX):         <checksum_here>
└─ Checksum Status:        ✓ Valid
```

---

## License

This project is released under the [MIT License](LICENSE).

You may:
- 📖 Use it freely
- 📝 Modify and adapt
- 📤 Share with proper credit

---

## Disclaimer

- 🚫 This tool is intended **for educational and research use only**
- ⚠️ Do not use it for any unauthorized or malicious purposes
- ❗ The author assumes no liability for misuse or data loss

---

## 🎁 Support

If you'd like to support future development and research:

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

---

We also acknowledge early privacy coins like **Bytecoin (BCN)**:

`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

---

🛡️ Licensed under MIT  
“**I morph bits, not to break, but to understand.**”  
— BitMorphX
