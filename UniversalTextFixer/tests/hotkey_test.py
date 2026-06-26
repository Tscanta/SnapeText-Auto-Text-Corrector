import keyboard
import pyperclip

print("Press 'Ctrl + Shift + F' to copy the current clipboard text.")

keyboard.add_hotkey(
    'ctrl+shift+f',
      lambda: print("Hotkey Detected! Current clipboard text:\n", pyperclip.paste())
)

keyboard.wait('esc')  # Wait for the 'esc' key to exit the program