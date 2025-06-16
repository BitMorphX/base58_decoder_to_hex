# 📎 RELEASE NOTES – base58_decoder_to_hex.py  
**Version:** 2.0.0  
**Release Date:** 2025-06-16

---

## 🚀 Overview

**Bitcoin Base58 to HEX Decoder** is a lightweight and interactive CLI utility for decoding Bitcoin Base58Check addresses into their raw hexadecimal structure.

This tool extracts:
- `Prefix` (address type),
- `Public Key Hash`,
- `Checksum`  
and verifies the integrity of the address using **double SHA-256** checksum matching.

Version **2.0.0** brings documentation polish, development tooling, and a visual demo to better showcase its behavior in action.

---

## 🆕 What's New in v2.0.0

- 🖼️ Added **animated terminal GIF demo**  
- 🧾 Full `README.md` rewrite with structured layout and usage details  
- ⚙️ Included `.vscode/` folder with:
  - `launch.json`, `tasks.json`, `extensions.json`, `settings.json`
- 🛠️ Windows launcher `.bat` script  
- 📦 Added `requirements.txt` with exact dependencies  
- 🔐 Updated LICENSE to Apache 2.0  
- 📣 New `RELEASE_v2.0.0.md` changelog file  
- 📜 Included `ETHICS.md` and `NOTICE` documents

---

## ✅ Included in v1.0.0

> These features existed in the original version and remain unchanged.

- ✅ Decodes Base58 Bitcoin addresses via `base58_decoder_to_hex.py`  
- ✅ Extracts:
  - Prefix (1 byte)  
  - Public key hash (20 bytes)  
  - Checksum (4 bytes)  
- ✅ Verifies checksum using double SHA-256  
- ✅ CLI prompt for address input  
- ✅ Uses `colorama` for terminal coloring  
- ✅ Error handling for malformed Base58 strings

---

## ⚠️ Notes

- Python 3.8+ is **recommended**  
- Required modules:
  - `base58`  
  - `colorama`  
- The tool performs **no blockchain/network operations**  
- Operates **100% offline**, ideal for audits, training, and research

---

## 📌 Project Files

- [README.md](./README.md) – Full documentation  
- [base58_decoder_to_hex.py](./base58_decoder_to_hex.py) – Main decoder script  
- [base58_decoder_to_hex.bat](./base58_decoder_to_hex.bat) – Windows launcher  
- [.vscode/](./.vscode/) – VS Code developer settings  
- [ETHICS.md](./ETHICS.md) – Ethical usage policy  
- [LICENSE](./LICENSE) – Apache 2.0 license  
- [NOTICE](./NOTICE) – Attribution & legal notes  
- [RELEASE_v2.0.0.md](./RELEASE_v2.0.0.md) – This changelog

---

## 📜 License  
Licensed under the [Apache 2.0 License](./LICENSE) by **BitMorphX**

---

## 🍱 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

**We also value early privacy coins such as:**  
★ **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

## 👤 Author & Contact

🔗 GitHub: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
