from src.spell_checker import correct_spelling


def test_correct_spelling_catches_common_typos():
    text = "helo hwo are yuo"
    corrected = correct_spelling(text)
    assert corrected == "hello how are you"
