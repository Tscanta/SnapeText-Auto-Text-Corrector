# FUNCTIONS:
#  create_separator(),
#  create_section_title(),
#  create_section(),
#  save_settings(),
#  open_settings(),
#  close_settings()


import tkinter as tk
from tkinter import ttk
from src.ui import root
from src.theme import get_theme_colors
from src.settings.settings_manager import (
    get_provider,
    set_provider,
    get_default_mode,
    set_default_mode,
    get_theme,
    set_theme,
    get_startup,
    set_startup
)
from src.ai.config import (
    GEMINI_MODEL,
    OLLAMA_MODEL,
    VERSION
)

settings_window = None
popup_parent = None

MODES = [
    "grammar",
    "professional",
    "friendly",
    "academic",
    "simplify",
    "translate",
    "summarize"
]

# SEPERATOR HELPER
def create_separator(parent, color):

    separator = tk.Frame(
        parent,
        bg=color,
        height=1
    )
    separator.pack(
        fill="x",
        padx=30,
        pady=20
    )

# TITLE HELPER
def create_section_title(parent, text, bg, fg):
    label = tk.Label(
        parent,
        text=text,
        bg=bg,
        fg=fg,
        font=("Segoe UI", 16, "bold")
    )
    label.pack(
        anchor="w",
        padx=30,
        pady=(0, 12)
    )
    return label

# SECTION FRAME HELPER
def create_section(parent, bg):
    frame = tk.Frame(
        parent,
        bg=bg
    )
    frame.pack(
        fill="x",
        padx=30
    )
    return frame


# Save all the settings and close the window
def save_settings(provider_var, mode_var, theme_var, startup_var):

    # Save provider
    set_provider(
        provider_var.get()
    )
    # Save default rewrite mode
    set_default_mode(
        mode_var.get()
    )
    # Save the theme
    set_theme(
    theme_var.get()
    )
    # Launch on startup?
    set_startup(
        startup_var.get()
    )

    print(f"Provider saved: {provider_var.get()}")
    print(f"Default mode saved: {mode_var.get()}")
    print(f"Default theme saved: {theme_var.get()}")

    close_settings()

    if popup_parent and popup_parent.winfo_exists(): # Check if the parent popup exists
        popup_parent.lift()
    
# Opens the Settings window
def open_settings(parent_popup=None):
    global settings_window
    global popup_parent

    THEME = get_theme_colors()
    BG = THEME["BG"]
    CARD = THEME["CARD"]
    HOVER = THEME["HOVER"]
    TEXT = THEME["TEXT"]
    SUBTEXT = THEME["SUBTEXT"]
    ACCENT = THEME["ACCENT"]

    popup_parent = parent_popup

    # Prevent multiple settings windows
    if settings_window:
        settings_window.deiconify() # Restore if minimized
        settings_window.lift() # Bring to front
        settings_window.focus_force() # Force focus
        return
    
    settings_window = tk.Toplevel(root)
    settings_window.title("Snape Settings")
    settings_window.geometry("600x800")
    settings_window.resizable(False, False)
    settings_window.configure(
        bg=BG
    )

   
    # TITLE
    title = tk.Label(
        settings_window,
        text="⚙ Snape Settings",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 24, "bold")
    )
    title.pack(
        pady=(20, 25)
    )
    
    # PROVIDER SECTION
    provider_frame = create_section(settings_window, BG)
    provider_frame.pack(
        fill="x",
        padx=30
    )
    provider_label = tk.Label( # LABELS
        provider_frame,
        text="AI Provider",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 15, "bold")
    )
    provider_label.pack(
        anchor="w",
        pady=(0, 10)
    )
    provider_var = tk.StringVar( # StringVar - a shared variable that Tkinter watches.
        value=get_provider()
    )
    
    # GEMINI RADIO BUTTON
    gemini_radio = tk.Radiobutton(
        provider_frame,
        text="Gemini",
        value="gemini",
        variable=provider_var,
        bg=BG,
        fg=TEXT,
        selectcolor=BG,
        activebackground=BG,
        activeforeground=TEXT,
        font=("Segoe UI", 14)
    )
    gemini_radio.pack(
        anchor="w"
    )

    # OLLAMA RADIO BUTTON
    ollama_radio = tk.Radiobutton(
        provider_frame,
        text="Ollama",
        value="ollama",
        variable=provider_var,
        bg=BG,
        fg=TEXT,
        selectcolor=BG,
        activebackground=BG,
        activeforeground=TEXT,
        font=("Segoe UI", 14)
    )

    ollama_radio.pack(
        anchor="w"
    )

    create_separator(settings_window, HOVER)

    # DEFAULT MODE SELECTOR
    create_section_title(
        settings_window,
        "Default Rewrite Mode",
        BG,
        TEXT
    )
    mode_var = tk.StringVar(
        value=get_default_mode()
    )
    mode_box = ttk.Combobox(
        settings_window,
        textvariable=mode_var,
        values=MODES,
        state="readonly",
        width=25,
        font=("Segoe UI", 14)
    )
    mode_box.pack(
        padx=30,
        anchor="w"
    )

    create_separator(settings_window, HOVER)

    create_section_title(
        settings_window,
        "🎨 Appearance",
        BG,
        TEXT
    )
    theme_var = tk.StringVar( # Theme variable
        value=get_theme()
    )
    dark_radio = tk.Radiobutton( # DARK MODE
        settings_window,
        text="Dark",
        value="dark",
        variable=theme_var,
        bg=BG,
        fg=TEXT,
        selectcolor=BG,
        activebackground=BG,
        activeforeground=TEXT,
        font=("Segoe UI", 14)
    )
    dark_radio.pack(
        anchor="w",
        padx=30
    )
    light_radio = tk.Radiobutton( # LIGHT MODE
        settings_window,
        text="Light",
        value="light",
        variable=theme_var,
        bg=BG,
        fg=TEXT,
        selectcolor=BG,
        activebackground=BG,
        activeforeground=TEXT,
        font=("Segoe UI", 14)
    )
    light_radio.pack(
        anchor="w",
        padx=30
    )

    create_separator(settings_window ,HOVER)

    # LAUNCH ON STARTUP?
    startup_var = tk.BooleanVar(
        value=get_startup()
    )
    startup_checkbox = tk.Checkbutton(
        settings_window,
        text="Launch SnapeText when Windows starts",
        variable=startup_var,
        bg=BG,
        fg=TEXT,
        selectcolor=BG,
        activebackground=BG,
        activeforeground=TEXT,
        font=("Segoe UI", 14)
    )
    startup_checkbox.pack(
        anchor="w",
        padx=30
    )

    create_separator(settings_window ,HOVER)

    #THE ABOUT SECTION
    create_section_title(
        settings_window,
        "ℹ️ About",
        BG,
        TEXT
    )
    provider = get_provider()

    model = (
        GEMINI_MODEL
        if provider == "gemini"
        else OLLAMA_MODEL
    )
    about = tk.Label(
        settings_window,
        text=(
            f"Version : {VERSION}\n"
            f"Provider : {provider.capitalize()}\n"
            f"Model : {model}\n"
            f"Founder : tscanta"
        ),
        justify="left",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 13)
    )
    about.pack(
        anchor="w",
        padx=30
    )

     # SAVE BUTTON
    save_button = tk.Button(
        settings_window,
        text="Save",
        bg=ACCENT,
        fg=TEXT,
        font=("Segoe UI", 14, "bold"),
        relief="flat",
        padx=25,
        pady=8,
        cursor="hand2",
        command=lambda: save_settings(
            provider_var,
            mode_var, 
            theme_var,
            startup_var
        )
    )
    save_button.pack(
        pady=30
    )

    settings_window.protocol(
        "WM_DELETE_WINDOW",
        close_settings
    )

def close_settings():
    global settings_window

    if settings_window:
        settings_window.destroy()
        settings_window = None