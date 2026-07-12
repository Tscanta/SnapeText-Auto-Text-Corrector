# FUNCTIONS:
#  shutdown()

import os
import keyboard

from src.ui import root

# Shut down SnapeText cleanly.
def shutdown(icon=None):

    print("Shutting down...")

    # Remove all keyboard hooks
    keyboard.unhook_all()

    if icon is not None:
        icon.stop()

    # Stop the Tkinter event loop
    root.quit()

    # Forcefully exit the process
    os._exit(0)