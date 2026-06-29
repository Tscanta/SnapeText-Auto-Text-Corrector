from src.ai.providers import CURRENT_PROVIDER

from src.ai.gemini import correct_text as gemini_correct
from src.ai.ollama import correct_text as ollama_correct

def correct_text(text, mode):
    if CURRENT_PROVIDER == "gemini":
        return gemini_correct(text, mode)
    
    if CURRENT_PROVIDER == "ollama":
        return ollama_correct(text, mode)
    
    raise ValueError("Unknown AI provider")