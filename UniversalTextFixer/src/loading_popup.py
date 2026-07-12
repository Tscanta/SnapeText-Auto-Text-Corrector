# FUNCTIONS:
#  show_loading(),
#  animate_loading(),
#  hide_loading()

import tkinter as tk
from src.ui import root

loading_window = None
status_label = None # Points to the "correcting..." label
animation_step = 0

# SHOWING THE LOADING POPUP
def show_loading(mode):
    global loading_window

    if loading_window:
        return
  
    loading_window = tk.Toplevel(root) # Create the loading window
    loading_window.overrideredirect(True) # Removes the titlebar, min/max, exit button
    
    loading_window.configure(
    bg="#1e1e1e"
    )

    # Frame creation
    frame = tk.Frame(
        loading_window,
        bg="#1e1e1e"
    )
    frame.pack(
        expand=True,
        fill="both"
    )   

    loading_window.geometry("250x140") # Size of the window
    loading_window.resizable(False, False) # Cannot resize the window
    loading_window.attributes("-topmost", True) # Keep it above other windows
    loading_window.lift() # Making the window appear immediately

    popup_width = 250
    popup_height = 140

    # Centering it on the monitor
    screen_width = loading_window.winfo_screenwidth()
    screen_height = loading_window.winfo_screenheight()

    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2

    loading_window.geometry(
        f"{popup_width}x{popup_height}+{x}+{y}"
    )

    # Contents inside the window
    title = tk.Label(
        frame,
        text="🖋 SnapeText", 
        bg="#1e1e1e",
        fg = "white",
        font=("Segoe UI", 18, "bold")
    )
    title.pack(
        pady=(20,10)
    )

    global status_label
    status_label = tk.Label(
        frame,
        text = "🤖Correcting...",
        bg="#1e1e1e",
        fg = "white",
        font=("Segoe UI", 12)
    )
    status_label.pack(
        pady = (0,5)
    )

    mode_label = tk.Label(
        frame,
        text=f"{mode.capitalize()} Mode",
        bg="#1e1e1e",
        fg="#bbbbbb",
        font=("Segoe UI", 10)
    )
    mode_label.pack(
        pady=(8,0)
        )

    loading_window.update_idletasks() # tells tkinter, "Finish laying out all the widgets first."
    animate_loading()


# ANIMATION FOR THE LOADING DOTS
def animate_loading():
    global animation_step

    #If the popup has been closed then dont animate
    if not loading_window:
        return
    
    dots = "." * ((animation_step % 3) + 1)

    status_label.config(
        text=f"🤖 Correcting{dots}"
    )
    animation_step += 1

    loading_window.after(
        350,
        animate_loading
    )

# HIDING THE LOADING LABEL
def hide_loading():
    global loading_window
    global animation_step

    if loading_window:
        loading_window.destroy()
        loading_window = None
        animation_step = 0