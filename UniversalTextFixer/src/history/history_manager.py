# FUNCTIONS: 
# format_timestamp(), 
# load_history(),
# save_history(), 
# add_history()
# clear_history()

import json
from pathlib import Path
from datetime import datetime, timedelta

# Path to the history file
HISTORY_FILE = Path(__file__).parent / "history.json"


# Returns a human-readable time difference string
def format_timestamp(timestamp):
    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()

    if timestamp.date() == now.date(): # If the timestamp matches now's date, return "Today" with the time
        return f"Today • {timestamp.strftime('%I:%M %p')}"
    
    elif timestamp.date() == (now - timedelta(days=1)).date(): # If the timestamp matches yesterday's date, return "Yesterday" with the time
        return f"Yesterday • {timestamp.strftime('%I:%M %p')}"
    
    return timestamp.strftime("%b %d, %Y • %I:%M %p") # Otherwise, return the full date and time


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

# Clears the rewrite history.
def clear_history(): 
    save_history([])