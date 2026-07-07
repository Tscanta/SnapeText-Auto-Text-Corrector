import json
from pathlib import Path
from datetime import datetime

# Path to the history file
HISTORY_FILE = Path(__file__).parent / "history.json"

# Loads the rewrite history.
def load_history(): 
    if not HISTORY_FILE.exists():
        return []
    
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
# Saves the rewrite history.
def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            history, 
            file,
            indent=4,
            ensure_ascii=False
        )

# Adds a new rewrite to the history.
def add_history(original, rewritten, mode, provider):

    history = load_history()

    history.insert(
        0,
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mode": mode,
            "provider": provider,
            "original": original,
            "rewritten": rewritten
        }
    )

    save_history(history)