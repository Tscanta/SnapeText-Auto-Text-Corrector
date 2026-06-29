from ollama import chat
from src.ai.prompts import PROMPTS
from src.ai.config import OLLAMA_MODEL

# --------------------------------------------------
# Sends text to Ollama and returns the AI response.
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

    # Check whether the requested mode exists
    if mode not in PROMPTS:
        raise ValueError(f"Unknown mode: {mode}")

    # Build the complete prompt
    prompt = f"""
{PROMPTS[mode]}

{text}
"""

    try:

        response = chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content.strip()

    except Exception as e:

        print("\n❌ Ollama Error")
        print(e)

        return None