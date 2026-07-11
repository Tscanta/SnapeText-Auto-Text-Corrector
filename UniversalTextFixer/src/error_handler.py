# FUNCTIONS:
# show_error(),
# show_warning(),
# show_info()

import tkinter.messagebox as messagebox

# Shows an error dialog
def show_error(title, message):
    messagebox.showerror(title, message)

# Shows a warning dialog
def show_warning(title, message):
    messagebox.showwarning(title, message)

# Shows an info dialog
def show_info(title, message):
    messagebox.showinfo(title, message)