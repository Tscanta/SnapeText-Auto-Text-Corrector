import os
import keyboard

from src.corrector import run_correction
from src.ui import root
from src.shutdown import shutdown


# Starts listening for global hotkeys.
def start_hotkey_listener():

    print("===========================")
    print("Snape is Running")
    print("===========================")
    print("Ctrl + Shift + G - Grammar")
    print("Ctrl + Shift + P - Professional")
    print("Ctrl + Shift + F - Friendly")
    print("Ctrl + Shift + A - Academic")
    print("Ctrl + Shift + S - Simplify")
    print("Ctrl + Shift + T - Translate")
    print("Ctrl + Shift + M - Summarize")
    print("Ctrl + Middle Mouse - Popup Menu")
    print("===========================")

    keyboard.add_hotkey(
        "ctrl+shift+g",
        lambda: run_correction("grammar")
    )

    keyboard.add_hotkey(
        "ctrl+shift+p",
        lambda: run_correction("professional")
    )

    keyboard.add_hotkey(
        "ctrl+shift+f",
        lambda: run_correction("friendly")
    )

    keyboard.add_hotkey(
        "ctrl+shift+a",
        lambda: run_correction("academic")
    )

    keyboard.add_hotkey(
        "ctrl+shift+s",
        lambda: run_correction("simplify")
    )

    keyboard.add_hotkey(
        "ctrl+shift+t",
        lambda: run_correction("translate")
    )

    keyboard.add_hotkey(
        "ctrl+shift+m",
        lambda: run_correction("summarize")
    )
    keyboard.add_hotkey(
    "esc",
    shutdown
)

    # Keep the listener alive forever
    keyboard.wait()
    print("Snape has died.")