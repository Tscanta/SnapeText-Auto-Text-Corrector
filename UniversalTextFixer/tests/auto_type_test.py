import pyautogui
import time

print("Starting the auto type test....Click inside Notepad. You have 5 seconds...")
time.sleep(5)  # Wait for 5 seconds to allow the user to click inside Notepad

# Type the text with a slight delay between each character
pyautogui.write(
    "Hello, this computer is typing by itself 😎\n"
    "My name is Anton The Autotyper\n"
    "Nice to meet you",
    interval=0.04
)

