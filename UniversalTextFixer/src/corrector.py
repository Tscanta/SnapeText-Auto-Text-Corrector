import time
from src.ai import correct_text
from src.clipboard import get_selected_text, replace_selected_text


# COMPLETE AI CORRECTION PIPELINE
def run_correction(mode="grammar", original_text=None):

    print()
    print(f"Running mode: {mode}")

    # If no text was supplied, copy the current selection
    if original_text is None:

        print()
        print("📋 Copying selected text...")

        original_text = get_selected_text()

    # Stop if nothing was selected
    if not original_text.strip():
        print("No text selected.")
        return

    print()
    print("Original:", original_text)

    print()
    print("🤖 Sending text to Gemini...")

    start = time.perf_counter()
    corrected_text = correct_text(original_text, mode)
    elapsed = time.perf_counter() - start
    print(f"⚡ Gemini took {elapsed:.2f} seconds") # Prints how long it took gemini to complete the request

    if corrected_text is None:
        print()
        print("❌ Correction failed.")
        return

    replace_selected_text(corrected_text)

    print()
    print("✅ Done!")