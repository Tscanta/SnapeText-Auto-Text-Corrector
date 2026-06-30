# A popup menu for the hotkeys menu using TKINTER a built-in python GUI creator
import tkinter as tk

from src.corrector import run_correction
from src.clipboard import get_selected_text
from src.settings.settings_manager import (
    get_provider,
    set_provider
)
from src.ui import root
from src.settings.settings_window import open_settings

# True if the popup is already open
popup_open = False
popup_window = None
gemini_button = None
ollama_button = None


# Highlighting the selected AI provider
def refresh_provider_buttons():

    global gemini_button
    global ollama_button

    if not gemini_button or not ollama_button:
        return
    
    if get_provider() == "gemini":
        gemini_button.config(
            bg=ACCENT,
            fg="white"
        )
        ollama_button.config(
            bg=CARD,
            fg=TEXT
        )
    else:
        ollama_button.config(
            bg=ACCENT,
            fg="white"
        )

        gemini_button.config(
            bg=CARD,
            fg=TEXT
        )
    

# Runs the selected AI mode and closes the popup.
def on_button_click(window, text, mode):
    global popup_open
    global popup_window

    popup_open = False
    popup_window = None

    window.destroy() # Close the popup window
    run_correction(mode, text) # Run the selected AI mode


def close_popup(window):
    global popup_open
    global popup_window

    popup_open = False
    popup_window = None
    
    window.destroy()

BG = "#1E1E1E"
CARD = "#252526"
HOVER="#3E3E42"
TEXT = "#FFFFFF"
SUBTEXT = "#AAAAAA"
ACCENT = "#4F8EF7"

# Displaying the menu pop-up
def show_popup(mouse_x,  mouse_y):
    global popup_open

    # Don't create another popup if one already exists
    if popup_open:
        return

    popup_open = True

    # Copy the selected text BEFORE opening the popup
    selected_text = get_selected_text()

    # Stop if nothing is selected
    if not selected_text.strip():
        popup_open = False
        print("No text selected.")
        return

    window = tk.Toplevel(root) # Create the window
    window.overrideredirect(True) # Remove the normal title bar
    window.attributes("-topmost", True) # Keep it above other windows
    window.update_idletasks() # Update the window so its size is calculated

    window.configure(
    bg=BG
    )

    global popup_window
    popup_window = window

    # WINDOW SETTINGS
    window.title("SnapeText") # Window title
    window.geometry("350x750") # Window size
    window.resizable(True, True) # Resizing

    window.focus_force()

    window.update_idletasks()

    # If the user presses ESC, close the popup
    window.bind(
        "<Escape>",
        lambda event: close_popup(window)
    )

    # If the user clicks the X button
    window.protocol(
        "WM_DELETE_WINDOW",
        lambda: close_popup(window)
    )


    #MOUSE STUFF
    # Get the current mouse position
    popup_width = 350
    popup_height = 750

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Default: open to the bottom-right
    x = mouse_x + 10
    y = mouse_y + 10

    # If near the right edge, open to the left
    if x + popup_width > screen_width:
        x = screen_width - popup_width - 10

    # If near the bottom edge, open above
    if y + popup_height > screen_height:
        y = screen_height - popup_height - 10

    window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")


    # HEADER FRAME
    header = tk.Frame(
        window,
        bg=BG
    )
    header.pack(
        fill="x",
        pady=(20,15)
    )

    # TITLE
    title = tk.Label(
        header,
        text = "🖋 SnapeText",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 20, "bold")
    )
    title.pack(pady=15)

    # SUBTITLE
    subtitle = tk.Label(
        header,
        text="Choose a rewrite mode",
        fg=SUBTEXT,
        bg=BG,
        font=("Segoe UI", 10),
        
    )
    subtitle.pack(pady=(0, 20))


    # SEPARATOR
    separator = tk.Frame(
    window,
    bg="#3c3c3c",
    height=1
    )   
    separator.pack(
        fill="x",
        padx=25,
        pady=(0,15)
    )

    # BUTTON FRAME
    button_frame = tk.Frame(
        window,
        bg=BG
    )
    button_frame.pack()

    # ---------------------------------------
    # List of all buttons
    #
    # Format:
    # ("Button Text", "Mode")
    # ---------------------------------------
    buttons = [

        ("📝 Grammar", "grammar"),

        ("💼 Professional", "professional"),

        ("😊 Friendly", "friendly"),

        ("🎓 Academic", "academic"),

        ("✨ Simplify", "simplify"),

        ("🌍 Translate", "translate"),
 
        ("📄 Summarize", "summarize")
    ]

    # Create every button automatically
    for text, mode in buttons:
        button = tk.Button(
            button_frame,
            text=text,
            bg=CARD,
            fg=TEXT,
            activebackground=HOVER,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            padx=20,
            pady=12,
            font=("Segoe UI", 11),
            anchor="w",
            cursor="hand2",
            width=24,
            command=lambda m=mode: 
                on_button_click(window, selected_text, m) # Linking the buttons
        ) 
        button.pack(
            fill="x",
            padx=25,
            pady=6
        )

        button.bind(
            "<Enter>",
            lambda e, b=button:
                b.config(bg=HOVER)
        )

        button.bind(
            "<Leave>",
            lambda e, b=button:
                b.config(bg=CARD)
        )

    # SETTINGS BUTTON
    settings_button = tk.Button(
        window,
        text="⚙ Settings",
        bg=CARD,
        fg=TEXT,
        activebackground=HOVER,
        activeforeground=TEXT,
        relief="flat",
        bd=0,
        padx=20,
        pady=12,
        font=("Segoe UI", 11),
        cursor="hand2",
        command=lambda: open_settings(window)
    )
    settings_button.pack(
        fill="x",
        padx=25,
        pady=(15, 20)
    )


    # AI PROVIDER FRAME
    provider_frame = tk.Frame(
        window,
        bg=BG
        )

    provider_frame.pack(
        pady=(0, 15)
    )

    # Gemini Button
    global gemini_button 

    gemini_button = tk.Button(
        provider_frame,
        text="🟣 Gemini",
        command=lambda: (
            print("Using Gemini"),
            set_provider("gemini"),
            refresh_provider_buttons()
        )
    )
    gemini_button.pack(
        side="left",
        padx=5
    )

    # OLLAMA BUTTON
    global ollama_button

    ollama_button = tk.Button(
        provider_frame,
        text="⚫ Ollama",
        command=lambda: (
            print("Using Ollama"),
            set_provider("ollama"),
            refresh_provider_buttons()
        )
    )
    ollama_button.pack(
        side="left",
            padx=5
    )

    # Refresh once after both buttons exist
    refresh_provider_buttons()
