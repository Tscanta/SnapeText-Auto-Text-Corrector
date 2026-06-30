from src.settings.settings import load_settings, save_settings

# Returns the value of a setting.
def get_setting(key):
    settings = load_settings()
    return settings.get(key)

# Changes the value of a setting and saves it.
def set_setting(key, value):
    settings = load_settings()
    settings[key] = value
    save_settings(settings)


# -----------------------------
# AI Provider
# -----------------------------

def get_provider():
    return get_setting("provider")


def set_provider(provider):
    set_setting(
        "provider",
        provider
    )


# -----------------------------
# Theme
# -----------------------------

def get_theme():
    return get_setting("theme")


def set_theme(theme):
    set_setting(
        "theme",
        theme
    )


# -----------------------------
# Default Rewrite Mode
# -----------------------------

def get_default_mode():
    return get_setting("default_mode")


def set_default_mode(mode):
    set_setting(
        "default_mode",
        mode
    )


# -----------------------------
# Startup
# -----------------------------

def get_startup():
    return get_setting("startup")


def set_startup(startup):
    set_setting(
        "startup",
        startup
    )