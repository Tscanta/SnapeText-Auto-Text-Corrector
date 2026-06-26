import os
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


# Function to correct text using Gemini
def correct_text(text):
    """
    Sends text to Gemini and returns the corrected version.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
Correct the spelling, grammar, and punctuation.

Return ONLY the corrected text.

{text}
"""
    )

    return response.text.strip()