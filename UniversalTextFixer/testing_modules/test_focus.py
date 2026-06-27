import time

from src.window_manager import (
    save_active_window,
    restore_active_window
)

print("Click Notepad within 5 seconds...")
time.sleep(5)

save_active_window()

print("Now click Chrome.")
time.sleep(5)

restore_active_window()