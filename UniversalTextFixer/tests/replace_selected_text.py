import pyautogui
import pyperclip
import time

print("Highlight some text. You have 5 seconds...")
time.sleep(5)

# Copy selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(0.2)

# Read clipboard
text = pyperclip.paste()

print("Original:", text)

#A dictionary for all the possible typos for the sentence "hello how are you"
corrections = {
    "helo": "hello",
    "hwo": "how",
    "yuo": "you",
    "teh": "the",
    "adn": "and"
}

# Simple corrections
for wrong, correct in corrections.items():
    text = text.replace(wrong, correct)

# Copy corrected text
pyperclip.copy(text)

# Replace selected text
pyautogui.hotkey("ctrl", "v")

print("Done!Your mistakes have been erased (am talking bout your typo not you lol)")