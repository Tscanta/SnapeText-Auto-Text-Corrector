import time

from src.window_manager import (
    save_active_window,
    restore_active_window
)

print("Click Notepad.")

time.sleep(5)

save_active_window()

print("Click another window.")

time.sleep(5)

print("Returning to Notepad...")

restore_active_window()