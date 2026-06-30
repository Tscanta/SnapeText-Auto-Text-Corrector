# 🖋 SnapeText

> A universal AI-powered writing assistant for Windows.

**Version:** v0.6.0

Snape is a desktop application that brings AI-powered writing assistance to **any Windows application**. Highlight text anywhere, invoke Snape with a global shortcut, choose a rewrite mode, and let AI instantly improve your writing without interrupting your workflow.

Unlike browser extensions, Snape is designed to work system-wide, making it useful in browsers, Microsoft Word, Notepad, Discord, VS Code, Slack, email clients, and virtually any application that supports text selection.

---

# 🚀 What's New in v0.6.0

## ✨ New Features

- Introduced a modular AI provider architecture.
- Added Google Gemini backend.
- Added Ollama backend (integration in progress).
- Added AI Manager for backend routing.
- Added provider management system.
- Added loading popup with animated status.
- Added performance metrics for AI requests.
- Redesigned popup menu with a modern dark interface.

## 🔧 Improvements

- Refactored the project into a cleaner modular architecture.
- Improved threading for a smoother user experience.
- Improved popup interactions and window handling.
- Separated AI providers for easier future expansion.

## 🚧 Known Issues

- Ollama integration is currently being finalized.
- Provider selection UI is under development.
- Settings window is planned for the next release.

---

# ✨ Features

- Works in almost any Windows application
- Google Gemini support
- Ollama support *(work in progress)*
- Grammar correction
- Professional rewriting
- Friendly rewriting
- Academic rewriting
- Simplify text
- Translation
- Summarization
- Ctrl + Middle Mouse popup menu
- Global keyboard shortcuts
- Automatic clipboard management
- Borderless popup positioned near the cursor
- Loading popup with animated feedback
- Performance reporting
- Modular AI backend
- Secure API key storage using environment variables

---

# ⚡ How It Works

1. Highlight text anywhere.
2. Press **Ctrl + Middle Mouse**.
3. Select an AI rewrite mode.
4. Snape copies the selected text.
5. Your selected AI provider processes the text.
6. Snape automatically pastes the rewritten version.

---

# 📂 Project Structure

```text
UniversalTextFixer/
│
├── src/
│   ├── ai/
│   │   ├── config.py
│   │   ├── gemini.py
│   │   ├── manager.py
│   │   ├── ollama.py
│   │   ├── prompts.py
│   │   └── providers.py
│   │
│   ├── clipboard.py
│   ├── corrector.py
│   ├── hotkeys.py
│   ├── loading_popup.py
│   ├── main.py
│   ├── mouse_listener.py
│   ├── popup_menu.py
│   ├── shutdown.py
│   ├── tray.py
│   ├── ui.py
│   └── window_manager.py
│
├── testing_modules/
├── tests/
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

## Languages

- Python

## Libraries

- Tkinter
- Google Gemini API
- Ollama
- PyAutoGUI
- Pyperclip
- Keyboard
- Pynput
- python-dotenv
- PyWin32

## Tools

- Git
- GitHub
- VS Code

---

# 📈 Current Progress

## ✅ Completed

- Global keyboard shortcuts
- Global mouse shortcut
- Clipboard automation
- Automatic copy & paste
- Gemini AI backend
- Ollama backend architecture
- AI Provider Manager
- Seven AI rewrite modes
- Prompt management system
- Loading popup with animation
- Performance reporting
- Popup menu UI
- Modern dark theme
- Popup positioning
- Modular architecture
- Configuration system
- Background threading
- Secure API key loading
- Testing modules

---

# 🗺 Roadmap

## Phase 1 — Core Application ✅

- [x] Clipboard automation
- [x] Global hotkeys
- [x] Global mouse listener
- [x] Replace selected text
- [x] AI correction pipeline
- [x] Popup menu
- [x] Multiple rewrite modes

## Phase 2 — Multi AI 🚧

- [x] Gemini backend
- [x] AI Manager
- [x] Provider architecture
- [x] Ollama backend
- [ ] Complete Ollama integration
- [ ] Provider selection UI

## Phase 3 — Desktop Polish

- [ ] Settings window
- [ ] Theme support
- [ ] Startup with Windows
- [ ] Custom hotkeys
- [ ] Windows notifications
- [ ] System tray controls
- [ ] Saved user preferences

## Phase 4 — Advanced Features

- [ ] OCR support
- [ ] Voice input
- [ ] Rewrite history
- [ ] Custom prompts
- [ ] Plugin system
- [ ] Multiple local models

## Phase 5 — Release

- [ ] Windows installer
- [ ] Standalone executable (.exe)
- [ ] Auto updater
- [ ] Documentation
- [ ] Public beta
- [ ] Version 1.0 release

---

# 💡 Vision

Snape aims to become the AI writing layer for Windows.

Instead of opening websites or relying on browser extensions, users should be able to improve writing anywhere with a single shortcut.

The long-term goal is to build a lightweight, fast, privacy-conscious assistant that feels like a native part of the operating system while giving users the freedom to choose between cloud AI and local AI.

---

# 🤝 Contributing

Contributions, ideas, feature requests, and bug reports are always welcome.

Feel free to fork the project, open an issue, or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.
