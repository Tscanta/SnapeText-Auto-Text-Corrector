import pyperclip

#Get the current text from the clipboard
clipboard_text = pyperclip.paste()

#Print the current text from the clipboard
print("Current clipboard text:")
print(clipboard_text)

pyperclip.copy("This text was copied by Python!")

print("\nClipboard has now been updated!")