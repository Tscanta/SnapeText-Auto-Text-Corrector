import time
import threading

from src.ai.manager import correct_text
from src.clipboard import get_selected_text, replace_selected_text
from src.loading_popup import show_loading, hide_loading
from src.ui import root
from src.error_handler import show_error
from src.settings.settings_manager import get_provider
from src.history.history_manager import add_history


# COMPLETE AI CORRECTION PIPELINE
def run_correction(mode="grammar", original_text=None):

    threading.Thread(
        target=run_correction_worker,
        args=(mode, original_text),
        daemon=True
    ).start()


def run_correction_worker(mode="grammar", original_text=None):

    provider_name = get_provider().capitalize()

    total_start = time.perf_counter()

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

    character_count = len(original_text)
    word_count = len(original_text.split())

    print()
    print("Original:", original_text)

    print()
    print(f"🤖 Sending text to {provider_name}...")
    print()

    # Show the loading popup
    root.after(
        0,
        lambda: show_loading(mode)
    )

    start = time.perf_counter()

    try:

        corrected_text = correct_text(
            original_text,
            mode
        )

    except Exception as e:

        # Hide the loading popup
        root.after(
            0,
            hide_loading
        )

        print()
        print("❌ AI Error")
        print(e)

        show_error(
            "SnapeText Error",
            "Unable to process your request.\n\nPlease check your AI provider and try again."
        )

        return

    ai_time = time.perf_counter() - start

    total_time = time.perf_counter() - total_start

    # Hide the loading popup
    root.after(
        0,
        hide_loading
    )

    time.sleep(0.1)  # Give Tkinter a tiny moment to destroy the popup

    # Save the rewrite to history
    add_history(
        original=original_text,
        rewritten=corrected_text,
        mode=mode,
        provider=get_provider()
    )

    # Paste the corrected text
    replace_selected_text(corrected_text)

    print()
    print("=========================================")
    print("📊 Snape Performance Report")
    print("=========================================")

    print(f"Mode        : {mode.capitalize()}")
    print(f"Characters  : {character_count} chars")
    print(f"Words       : {word_count} words")

    print()

    print(f"{provider_name} Time : {ai_time:.2f} s")
    print(f"Total Time  : {total_time:.2f} s")

    print("=========================================")

    print()
    print("✅ Done!")