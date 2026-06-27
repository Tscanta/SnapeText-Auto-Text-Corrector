import time
from src.corrector import run_correction
from src.config import COUNTDOWN

print("Highlight some text...")
print("You have 5 seconds.")

time.sleep(COUNTDOWN)

run_correction()