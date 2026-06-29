import tkinter as tk
from src.ui import root
loading_window = None

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
    loading_window.focus_force()

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

    status = tk.Label(
        frame,
        text = "🤖Correcting text...",
        bg="#1e1e1e",
        fg = "white",
        font=("Segoe UI", 12)
    )
    status.pack(
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
    loading_window.update()

def hide_loading():
    global loading_window

    if loading_window:
        loading_window.destroy()
        loading_window = None

        
    




 