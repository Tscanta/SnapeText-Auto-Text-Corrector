# FUNCTIONS:
#  get_theme_colors()

from src.settings.settings_manager import get_theme

DARK = {
    "BG": "#1E1E1E",
    "CARD": "#252526",
    "HOVER": "#3E3E42",
    "TEXT": "#FFFFFF",
    "SUBTEXT": "#AAAAAA",
    "ACCENT": "#4F8EF7"
}

LIGHT = {
    "BG": "#F5F5F5",
    "CARD": "#FFFFFF",
    "HOVER": "#E8E8E8",
    "TEXT": "#202020",
    "SUBTEXT": "#666666",
    "ACCENT": "#4F8EF7"
}

# Returns the colors for the selected theme
def get_theme_colors():
    if get_theme() == "light":
        return LIGHT
    
    return DARK