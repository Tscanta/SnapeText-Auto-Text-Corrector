# FUNCTIONS:
# register_window(),
# unregister_window(),
# refresh_theme()

windows = []

# Registers a window for theme updates
def register_window(window, refresh_function):

    windows.append(
        (window, refresh_function)
    )

# Removes a closed window
def unregister_window(window):

    global windows

    windows = [
        (w, func)
        for w, func in windows
        if w != window
    ]

# Refreshes every registered window
def refresh_theme():

    for window, refresh_function in windows:

        if window.winfo_exists():

            refresh_function()