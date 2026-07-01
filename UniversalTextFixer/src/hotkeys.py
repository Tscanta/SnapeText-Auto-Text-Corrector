# FUNCTIONS:
#  on_ctrl_press(),
#  on_ctrl_release(),
#  start_hotkey_listener().

import time
import keyboard
import pyautogui

from src.corrector import run_correction
from src.popup_menu import show_popup
from src.ui import root
from src.shutdown import shutdown

last_ctrl_release = 0.0 # Time of the previous Ctrl press
ctrl_is_down = False # True while Ctrl is currently held down
DOUBLE_CTRL_DELAY = 0.30 # Maximum time between two Ctrl presses

# Called when Ctrl is pressed
def on_ctrl_press(event):
    global ctrl_is_down

    # Ignore key repeats while the key is held
    if ctrl_is_down:
        return

    ctrl_is_down = True


# Called when Ctrl is released
def on_ctrl_release(event):
    global ctrl_is_down
    global last_ctrl_release

    ctrl_is_down = False

    current_time = time.time()

    # Second Ctrl tap detected
    if current_time - last_ctrl_release <= DOUBLE_CTRL_DELAY:

        x, y = pyautogui.position()

        root.after(
            0,
            lambda: show_popup(x, y)
        )

    last_ctrl_release = current_time

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
    print("Double Ctrl Press - Popup Menu")
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
    keyboard.on_press_key(
        "ctrl",
        on_ctrl_press
    )

    keyboard.on_release_key(
        "ctrl",
        on_ctrl_release
    )
    keyboard.add_hotkey(
        "esc",
        shutdown
    )

    # Keep the listener alive forever
    keyboard.wait()
    print("Snape has died.")