import time
from src.clipboard import get_selected_text

print("Highlight text. You have 5 seconds...")
time.sleep(5)

text = get_selected_text()

from src.clipboard import get_selected_text
import time

print("Highlight some text. You have 5 seconds...")
time.sleep(5)

text = get_selected_text()

print("Selected text:")
print(text)
