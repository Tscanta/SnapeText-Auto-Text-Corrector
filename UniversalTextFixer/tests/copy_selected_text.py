import pyautogui
import pyperclip
import time

#Get the current text from the clipboard
print("Highlight some text. You have 5 seconds...")
time.sleep(5)

#Simulate pressing 'Ctrl + C' to copy the highlighted text
pyautogui.hotkey('ctrl', 'c')

#Give the system a moment to process the copy command
time.sleep(0.2)

#Read the text from the clipboard
selected_text = pyperclip.paste()

#Print the copied text
print("\nSelected text:")
print(selected_text)