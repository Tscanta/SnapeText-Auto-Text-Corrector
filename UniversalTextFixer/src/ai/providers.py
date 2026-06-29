# Current AI provider
CURRENT_PROVIDER = "gemini"

def set_provider(provider):
    global CURRENT_PROVIDER

    if provider not in ("gemini", "ollama"):
        raise ValueError(f"Unknown provider: {provider}")

    CURRENT_PROVIDER = provider