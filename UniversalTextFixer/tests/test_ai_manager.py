from src.settings.settings_manager import (
    set_provider,
    get_provider
)

from src.ai.manager import correct_text

set_provider("gemini")

print("Provider:", get_provider())

response = correct_text(
    "i am happy",
    "grammar"
)

print(response)