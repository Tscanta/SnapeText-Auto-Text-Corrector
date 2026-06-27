import os
import keyboard

from src.ui import root
from src import mouse_listener

def shutdown():

    print("Shutting down...")

    keyboard.unhook_all()

    if mouse_listener.keyboard_listener:
        mouse_listener.keyboard_listener.stop()

    if mouse_listener.mouse_listener:
        mouse_listener.mouse_listener.stop()

    root.quit()

    os._exit(0)