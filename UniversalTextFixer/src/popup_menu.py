# A popup menu for the hotkeys menu using TKINTER a built-in python GUI creator
import tkinter as tk

from src.corrector import run_correction
from src.clipboard import get_selected_text
from src.ui import root

# True if the popup is already open
popup_open = False
popup_window = None

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

    global popup_window
    popup_window = window

    # WINDOW SETTINGS
    window.title("SnapeText") # Window title
    window.geometry("350x550") # Window size
    window.resizable(True, True) # Prevent resizing

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
    popup_height = 550

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
    header = tk.Frame(window)
    header.pack(pady=15)

    # TITLE
    title = tk.Label(
        header,
        text = "🖋 SnapeText",
        font=("Segoe UI", 18, "bold")
    )
    title.pack(pady=15)

    # SUBTITLE
    subtitle = tk.Label(
        header,
        text="Choose a rewrite mode",
        font=("Segoe UI", 10)
    )
    subtitle.pack(pady=(0, 20))


    # BUTTON FRAME
    button_frame = tk.Frame(window)
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
            width=28,
            font=("Segoe UI", 10),
            command=lambda m=mode: on_button_click(window, selected_text, m) # Linking the buttons
        ) 

        button.pack(pady=4)