
![Version](https://img.shields.io/badge/version-v0.7.1-blue)
![Python](https://img.shields.io/badge/python-3.11+-yellow)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<img width="100" height="100" alt="tray_icon_v0 6" src="https://github.com/user-attachments/assets/4050780e-c491-443b-a7f9-8a4196b98457" />


# 🖋 SnapeText

> A universal AI-powered writing assistant for Windows.

**Version:** v0.7.0

Snape is a desktop application that brings AI-powered writing assistance to **any Windows application**. Highlight text anywhere, invoke Snape with a global shortcut, choose a rewrite mode, and let AI instantly improve your writing without interrupting your workflow.

Unlike browser extensions, Snape is designed to work system-wide, making it useful in browsers, Microsoft Word, Notepad, Discord, VS Code, Slack, email clients, and virtually any application that supports text selection.

---

# 🚀 What's New in v0.7.0

- Added a fully functional Settings window.
- Added persistent user settings using `settings.json`.
- Added AI provider selection (Gemini / Ollama).
- Added Default Rewrite Mode selection.
- Added Theme preference system.
- Added About section displaying version, provider, model and developer.
- Added startup preference backend.
- Added reusable settings manager.
- Added AI context documentation (`AI_CONTEXT.md`).

## 🔧 Improvements

- Improved project organization with a dedicated Settings module.
- Refactored popup interactions with the Settings window.
- Improved provider persistence across sessions.
- Improved overall UI consistency.
- Cleaner modular architecture for future expansion.

## 🚧 Known Issues

- Windows Startup integration is not implemented yet.
- Theme engine is currently preference-only.
- Tray integration with Settings is still in development.
  
---

# ✨ Features

## AI Writing

- Grammar correction
- Professional rewriting
- Friendly rewriting
- Academic rewriting
- Simplify text
- Translation
- Summarization

## AI Providers

- Google Gemini
- Ollama (Local AI)
- Switch AI providers instantly
- Persistent provider selection

## Productivity

- Works in almost any Windows application
- Ctrl + Middle Mouse popup menu
- Global keyboard shortcuts
- Automatic clipboard management
- Automatic text replacement
- Borderless popup positioned near the cursor
- Loading popup with animated feedback
- Performance reporting

## Settings

- AI provider selection
- Default rewrite mode
- Theme preference
- Startup preference
- About page
- Persistent settings using JSON

## Developer

- Modular AI backend
- Secure API key storage
- Modular architecture
  
---

# ⚡ How It Works

1. Highlight text anywhere.
2. Press **Ctrl + Middle Mouse**.
3. Select an AI rewrite mode.
4. Snape copies the selected text.
5. Your selected AI provider processes the text.
6. Snape automatically pastes the rewritten version.

---

```text
SnapeText/

├── src/
│
├── ai/
│   ├── config.py
│   ├── gemini.py
│   ├── manager.py
│   ├── ollama.py
│   ├── prompts.py
│   └── providers.py
│
├── settings/
│   ├── settings.json
│   ├── settings.py
│   ├── settings_manager.py
│   └── settings_window.py
│
├── clipboard.py
├── corrector.py
├── hotkeys.py
├── loading_popup.py
├── main.py
├── mouse_listener.py
├── popup_menu.py
├── shutdown.py
├── tray.py
└── ui.py

tests/
testing_modules/

README.md
AI_CONTEXT.md
.gitignore
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

## v0.7.0 — Settings Update 🚧

- [x] Settings Window
- [x] Settings Manager
- [x] Provider Selection
- [x] Default Rewrite Mode
- [x] Theme Preference
- [x] Startup Preference Backend
- [x] About Section
- [ ] Tray Integration
- [ ] UI Polish

## v0.8.0 — Desktop Experience

- [ ] Theme engine
- [ ] Startup with Windows
- [ ] Custom hotkeys
- [ ] Rewrite history
- [ ] Windows notifications
- [ ] Better tray menu
- [ ] AI model selector

## v0.9.0 — Smart Features

- [ ] OCR support
- [ ] Voice input
- [ ] Screenshot translation
- [ ] Better local AI support

## v1.0.0 — Public Release

- [ ] Windows installer
- [ ] Standalone executable (.exe)
- [ ] Auto updater
- [ ] Documentation
- [ ] Public beta
      
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
