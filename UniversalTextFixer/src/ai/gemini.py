import os

from dotenv import load_dotenv
from google import genai

from src.ai.config import GEMINI_MODEL
from src.ai.prompts import PROMPTS


# Load the environment variables from the .env file
load_dotenv()

# Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Stop the program if the API key is missing
if not api_key:
    raise ValueError("GEMINI_API_KEY not found!")

# Create the Gemini client
client = genai.Client(api_key=api_key)


# --------------------------------------------------
# Sends text to Gemini and returns the AI response.
#
# Modes:
# - grammar
# - professional
# - friendly
# - academic
# - simplify
# - summarize
# - translate
# --------------------------------------------------

def correct_text(text, mode="grammar"):

    print(f"Using Gemini model: {GEMINI_MODEL}")

    # Check whether the requested mode exists
    if mode not in PROMPTS:
        raise ValueError(f"Unknown mode: {mode}")

    # Build the complete prompt for Gemini
    prompt = f"""
{PROMPTS[mode]}

{text}
"""

    # Send the prompt to Gemini
    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        # Return only the generated text
        return response.text.strip()

    except Exception as e:

        print("\n❌ AI Error")
        print(e)

        raise e