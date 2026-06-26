import os
import time
import pyautogui
import pyperclip
from dotenv import load_dotenv
from google import genai


# Load the API key from the .env file
load_dotenv()


# Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


# Stop the program if no API key is found
if not api_key:
    raise ValueError("GEMINI_API_KEY not found!")


# Create the Gemini client
client = genai.Client(api_key=api_key)


# Give the user time to highlight the text
print("Highlight the text you want to correct.")
print("You have 5 seconds...")
time.sleep(5)


# Copy the highlighted text (Ctrl + C)
pyautogui.hotkey("ctrl", "c")

# Wait for Windows to update the clipboard
time.sleep(0.2)

# Read the copied text from the clipboard
text = pyperclip.paste()


# Check if anything was copied
if not text.strip():
    print("No text was selected.")
    exit()

print("\nOriginal text:")
print(text)



# Send the text to Gemini for correction
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
Correct the spelling, grammar, and punctuation.

Return ONLY the corrected text.

{text}
"""
)

# Save Gemini's response
corrected_text = response.text.strip()

print("\nCorrected text:")
print(corrected_text)



# Replace the selected text and copy the corrected text to the clipboard
pyperclip.copy(corrected_text)

# Small delay before pasting
time.sleep(0.2)

# Paste the corrected text (Ctrl + V)
pyautogui.hotkey("ctrl", "v")

print("\nDone!")