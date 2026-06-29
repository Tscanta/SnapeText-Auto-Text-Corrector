# 📝 SnapeText

> A universal AI-powered writing assistant for Windows.

Snape is a desktop application that brings AI-powered writing assistance to **any Windows application**. Highlight text anywhere, invoke Snape with a global shortcut, choose a rewrite mode, and let AI instantly improve your writing without interrupting your workflow.

Unlike browser extensions, Snape is designed to work system-wide, making it useful in browsers, Microsoft Word, Notepad, Discord, VS Code, Slack, email clients, and virtually any application that supports text selection.

---

#  Features

*  Works in almost any Windows application
*  Powered by Google Gemini
*  Grammar correction
*  Professional rewriting
*  Friendly rewriting
*  Academic rewriting
*  Simplify text
*  Translation
*  Summarization
*  Ctrl + Middle Mouse popup menu
*  Global keyboard shortcuts
*  Automatic clipboard management
*  Borderless popup positioned near the cursor
*  Fast AI response (~1–2 seconds)
*  API key stored securely using environment variables

---

#  How It Works

1. Highlight text in any application.
2. Press **Ctrl + Middle Mouse**.
3. Choose an AI mode.
4. Snape copies the selected text.
5. Gemini generates the improved version.
6. Snape pastes the rewritten text back automatically.

---

# 📂 Project Structure

```text
UniversalTextFixer/
│
├── src/
│   ├── ai.py
│   ├── clipboard.py
│   ├── config.py
│   ├── corrector.py
│   ├── hotkeys.py
│   ├── main.py
│   ├── mouse_listener.py
│   ├── popup_menu.py
│   ├── prompts.py
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

# 🛠️ Tech Stack

## Languages

* Python

## Libraries

* Tkinter
* Google Gemini API
* PyAutoGUI
* Pyperclip
* Keyboard
* Pynput
* Python-dotenv
* PyWin32

## Tools

* Git
* GitHub
* VS Code

---

# 🎯 Current Progress

## ✅ Completed

* Global keyboard shortcuts
* Global mouse shortcut
* Clipboard automation
* Automatic copy & paste
* AI integration with Gemini
* Seven AI rewrite modes
* Popup menu UI
* Popup positioning near cursor
* Popup closes automatically
* Modular project architecture
* Configuration system
* Prompt management
* Testing modules
* Secure API key loading

---

# 🗺️ Roadmap

## Phase 1 — Core Application ✅

* [x] Clipboard automation
* [x] Global hotkeys
* [x] Global mouse listener
* [x] Replace selected text
* [x] AI correction pipeline
* [x] Popup menu
* [x] Multiple AI modes

## Phase 2 — Desktop Polish 🚧

* [ ] Loading animation
* [ ] Windows notifications
* [ ] System tray controls
* [ ] Settings window
* [ ] Custom hotkeys
* [ ] Theme support
* [ ] Startup with Windows

## Phase 3 — Advanced Features

* [ ] Local AI (Ollama)
* [ ] Multiple AI providers
* [ ] Plugin system
* [ ] OCR support
* [ ] Voice input
* [ ] Custom prompts
* [ ] Rewrite history

## Phase 4 — Release

* [ ] Windows installer
* [ ] Auto updater
* [ ] Executable (.exe)
* [ ] Documentation
* [ ] Public beta

---

# 💡 Vision

Snape aims to become the AI writing layer for Windows.

Instead of opening websites or relying on browser extensions, users should be able to improve writing anywhere with a single shortcut.

The long-term goal is to build a lightweight, fast, privacy-conscious assistant that feels like a native part of the operating system.

---

# 🤝 Contributing

Contributions, ideas, feature requests, and bug reports are welcome.

If you'd like to improve Snape, feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.
