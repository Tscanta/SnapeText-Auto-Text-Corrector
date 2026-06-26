import os
from dotenv import load_dotenv
from google import genai

#Load the .env file
load_dotenv()

#Get the API key
api_key = os.getenv("GEMINI_API_KEY")

#Check if the key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY not found!")

#Create the Gemini client
client = genai.Client(api_key=api_key)

#Ask Gemini to correct grammar
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "Correct the spelling and grammar. Return ONLY the corrected sentence:\n\nhelo hwo are yuo"
)

#Printing the corrected text
print(response.text)