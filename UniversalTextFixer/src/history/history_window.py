# FUNCTIONS: 
# on_canvas_configure(),
# create_separator(),
# on_clear_history(),
# open_history(),
# close_history(), 
# is_history_open()


import tkinter as tk
from tkinter import messagebox
from src.ui import root
from src.history.history_manager import format_timestamp, load_history, clear_history

history_window = None
popup_parent = None
canvas = None
canvas_window = None

BG = "#1E1E1E"
CARD = "#252526"
HOVER = "#3E3E42"
TEXT = "#FFFFFF"
SUBTEXT = "#AAAAAA"
ACCENT = "#4F8EF7"

# Binds the canvas width to the scrollable frame width
def on_canvas_configure(event):
    canvas.itemconfig(
        canvas_window,
        width=event.width
    )


# Creates a separator line
def create_separator(card):
    separator = tk.Frame(
        card, 
        bg="#3A3A3C",
        height=1
    )
    separator.pack(
        fill="x",
        pady=(0, 12)
    )
    return separator

def on_clear_history():
    if not messagebox.askyesno(
        "Clear history",
        "Are you sure you want to clear all rewrite history?"
    ):
        return
    
    clear_history()
    close_history()
    open_history()

# Opens the History window
def open_history(parent_popup=None):
    global history_window, popup_parent, canvas, canvas_window

    popup_parent = parent_popup

    # Preventing multiple history windows from opening
    if history_window:
        return
    
    history_window = tk.Toplevel(root) # Creating a new window
    history_window.title("Rewrite History") # Title of the window
    history = load_history() # Loading the rewrite history
    history_window.geometry("700x800") # Size of the window
    history_window.resizable(True, True) 
    history_window.configure(bg=BG) # Background color of the window

    # TITLE
    title = tk.Label(
        history_window,
        text="📜 Rewrite History",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 20, "bold")
    )
    title.pack(
        pady=(20, 25)
    )

    # MAIN CONTAINER
    container = tk.Frame(
        history_window,
        bg=BG
    )
    container.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )

    # BUTTON FRAME
    button_frame = tk.Frame(
        history_window,
        bg=BG
    )
    button_frame.pack(
        fill="x",
        pady=(10, 20)
    )

    # CANVAS
    canvas = tk.Canvas(
        container,
        bg=BG,
        highlightthickness=0,
        bd=0
    )
    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    # SCROLLBAR
    scrollbar = tk.Scrollbar(
        container,
        orient="vertical",
        command=canvas.yview
    )
    scrollbar.pack(
        side="right",
        fill="y"
    )
    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    # SCROLLABLE FRAME
    scrollable_frame = tk.Frame(
        canvas,
        bg=BG
    )
    canvas_window = canvas.create_window(
        (0, 0),
        window=scrollable_frame,
        anchor="nw"
    )

    # Bind canvas resize to stretch the inner frame horizontally
    canvas.bind(
        "<Configure>",
        on_canvas_configure
    )

    # Updating the scroll region whenever the frame changes size
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    # Placeholder
    if not history:
        empty = tk.Label(
            scrollable_frame,
            text="No history available.",
            bg=BG,
            fg=SUBTEXT,
            font=("Segoe UI", 11)
        )
        empty.pack(
            pady=30
        )
    else:

        # Create one card for each history entry
        for item in history:
            # CARD
            card = tk.Frame(
                scrollable_frame,
                bg=CARD,
                padx=20,
                pady=15
            )
            card.pack(
                fill="x",
                padx=20,
                pady=5
            )

            # HEADER FRAME
            header_frame = tk.Frame(
                card,
                bg=CARD
            )
            header_frame.pack(
                fill="x"
            )

            # Mode
            mode_label = tk.Label(
                header_frame,
                text=f"📝 {item['mode'].capitalize()}",
                bg=CARD,
                fg=TEXT,
                font=("Segoe UI", 12, "bold")
            )
            mode_label.pack(
                side="left"
            )
            # Provider
            provider_label = tk.Label(
                header_frame,
                text=item["provider"].capitalize(),
                bg=ACCENT,
                fg="white",
                font=("Segoe UI", 9, "bold"),
            )
            provider_label.pack(
                side="left",
                padx=(8, 0)
            )
            # Time Stamp
            timestamp = tk.Label(
                card,
                text=f"🕒 {format_timestamp(item['timestamp'])}",
                bg=CARD,
                fg=SUBTEXT,
                font=("Segoe UI", 9)
            )
            timestamp.pack(
                anchor="w",
                pady=(6, 10)
            )

            create_separator(card)

            # BEFORE
            before_title = tk.Label(
                card,
                text="Before",
                bg=CARD,
                fg=TEXT,
                font=("Segoe UI", 10, "bold")
            )
            before_title.pack(
                anchor="w",
                pady=(10, 2)
            )
            before = tk.Label(
                card,
                text=item["original"],
                bg=CARD,
                fg=TEXT,
                justify="left",
                wraplength=600,
                font=("Segoe UI", 10)
            )
            before.pack(
                anchor="w"
            )

            create_separator(card)

            # AFTER
            after_title = tk.Label(
                card,
                text="After",
                bg=CARD,
                fg=TEXT,
                font=("Segoe UI", 10, "bold")
            )
            after_title.pack(
                anchor="w",
                pady=(12, 2)
            )
            after = tk.Label(
                card,
                text=item["rewritten"],
                bg=CARD,
                fg=TEXT,
                justify="left",
                wraplength=600,
                font=("Segoe UI", 10)
            )
            after.pack(
                anchor="w"
            )

    # Bind mouse wheel for scrolling
    canvas.bind_all(
        "<MouseWheel>",
        on_mouse_wheel
    )

    # Clear history button
    clear_button = tk.Button(
        button_frame,
        text="🗑 Clear History",
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
        command=on_clear_history
    )

    clear_button.pack(
        padx=20
    )

    # Close button
    history_window.protocol(
        "WM_DELETE_WINDOW",
        close_history
    )


# Scroll using the mouse wheel
def on_mouse_wheel(event):
    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )

# Closes the History window
def close_history():
    global history_window

    if history_window:
        history_window.unbind_all("<MouseWheel>") # Unbinding the mouse wheel from the canvas
        history_window.destroy()
        history_window = None

# Returns True if the History window is open
def is_history_open():
    return history_window is not None