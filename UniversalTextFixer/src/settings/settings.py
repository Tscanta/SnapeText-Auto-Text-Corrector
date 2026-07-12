# FUNCTIONS:
#  load_settings(),
#  save_settings()

import json
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent / "settings.json" # Path to settings.json

# Load every setting from settings.json
def load_settings():
    with open(
        SETTINGS_FILE,
        "r",
        encoding="utf-8"
    )as file:
        return json.load(file)

# Save all settings back to settings.json
def save_settings(settings):

    with open(
        SETTINGS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            settings,
            file,
            indent=4
        )