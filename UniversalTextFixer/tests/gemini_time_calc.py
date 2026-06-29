import time

from src.ai.gemini import correct_text

original_text = "helo hwo are yuo"
mode = "grammar"

start = time.time()

corrected_text = correct_text(original_text, mode)

print(corrected_text)
print(f"Gemini took {time.time() - start:.2f} seconds")