# 📝 Auto Grammar Corrector

> A universal AI-powered writing assistant that works across Windows applications.

Auto Grammar Corrector is a desktop application designed to automatically detect and correct spelling mistakes, grammar, punctuation, and writing style in **any text field**, whether you're typing in a browser, Microsoft Word, Notepad, Discord, Slack, or other desktop applications.

The long-term goal is to provide a lightweight, fast, and privacy-conscious writing assistant that works everywhere instead of being limited to browser extensions.

---

##  Planned Features

*  Works in any desktop application
*  Automatic spelling correction
*  Grammar and punctuation correction
*  AI-powered text rewriting
*  Multi-language support
*  Professional, casual, and academic writing modes
*  Global keyboard shortcut
*  Privacy-focused with optional local AI models
*  Lightweight background application
*  System tray integration

---

##  Current Progress

###  Phase 1 – Desktop Automation Fundamentals

Completed:

* Clipboard read and write
* Global hotkey detection
* Automatic keyboard typing
* Copying selected text from any application

These experiments provide the foundation required for building a universal text correction tool.

---

##  Tech Stack

* Python
* PyAutoGUI
* Pyperclip
* Keyboard
* Git & GitHub

### Planned

* Tauri
* Rust
* SQLite
* OpenAI API / Ollama
* Windows API

---

##  Project Structure

```
AutoGrammarCorrector/
│
├── tests/
│   ├── clipboard_test.py
│   ├── hotkey_test.py
│   ├── auto_type_test.py
│   └── copy_selected_text.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🎯 Roadmap

* [x] Clipboard interaction
* [x] Global hotkeys
* [x] Keyboard automation
* [x] Copy selected text
* [ ] Replace selected text
* [ ] Basic grammar correction engine
* [ ] AI integration
* [ ] Background system tray application
* [ ] Windows installer
* [ ] Multi-language support
* [ ] Local AI support
* [ ] Public beta release

---

## 💡 Vision

Instead of opening a website or browser extension to fix text, Auto Grammar Corrector aims to become a universal writing layer for Windows.

Highlight text anywhere, press a shortcut, and instantly receive corrected, polished writing without interrupting your workflow.

---

## 🤝 Contributing

Contributions, ideas, and feedback are always welcome.

---

## 📄 License

This project is licensed under the MIT License.
