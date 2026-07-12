# FUNCTIONS:
#  correct_text()

from src.settings.settings_manager import get_provider

from src.ai.gemini import correct_text as gemini_correct
from src.ai.ollama import correct_text as ollama_correct

def correct_text(text, mode):

    print(f"🤖 AI Provider: {get_provider()}")

    if get_provider() == "gemini":
        return gemini_correct(text, mode)
    
    if get_provider() == "ollama":
        return ollama_correct(text, mode)
    
    raise ValueError("Unknown AI provider")