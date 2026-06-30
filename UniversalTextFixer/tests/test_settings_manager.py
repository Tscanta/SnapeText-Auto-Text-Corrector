from src.settings.settings_manager import (
    get_provider,
    set_provider
)

print("Current:", get_provider())

set_provider("ollama")
print("Changed to:", get_provider())
