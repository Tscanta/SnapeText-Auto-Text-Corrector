import time
import pyautogui
import pyperclip

print("Highlight some text in Notepad...")
time.sleep(5)

pyautogui.hotkey("ctrl", "c")

time.sleep(0.5)

print(repr(pyperclip.paste()))