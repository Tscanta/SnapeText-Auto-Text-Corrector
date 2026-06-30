import ollama
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

    print(f"Using Ollama model: {OLLAMA_MODEL}")

    # Check whether the requested mode exists
    if mode not in PROMPTS:
        raise ValueError(f"Unknown mode: {mode}")

    # Build the complete prompt
    prompt = f"""
{PROMPTS[mode]}

{text}
"""
    print("Connecting to Ollama...")
    print()
    print(f"Model: {OLLAMA_MODEL}")
    print(f"Prompt length: {len(prompt)}")

    try:

        response = ollama.chat(
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
        print(type(e).__name__)
        print(e)

        return None