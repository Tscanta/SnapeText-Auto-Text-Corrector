import time
import pyautogui
import pyperclip
from src.config import CLIPBOARD_DELAY

#Copies the user's selected text and returns it.
def get_selected_text():
    
    time.sleep(0.2)
    # Copy the highlighted text
    pyautogui.hotkey("ctrl", "c")

    # Give Windows time to update the clipboard
    time.sleep(CLIPBOARD_DELAY)

    # Return the copied text
    return pyperclip.paste()


#Replaces the highlighted text with the given text.
def replace_selected_text(text):

    # Copy the corrected text to the clipboard
    pyperclip.copy(text)

    # Small delay before pasting
    time.sleep(CLIPBOARD_DELAY)

    # Paste the corrected text
    pyautogui.hotkey("ctrl", "v")