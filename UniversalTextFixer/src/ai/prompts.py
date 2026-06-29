# Stores every prompt used by Snape.

PROMPTS = {
    # GRAMMAR MODE
    "grammar": """
You are an expert English editor.

Correct:
- Spelling
- Grammar
- Punctuation

Preserve:
- Meaning
- Formatting

Return ONLY the corrected text.
""",

    # PROFESSIONAL MODE
    "professional": """
Rewrite the text professionally.

Keep the original meaning.

Return ONLY the rewritten text.
""",

    # FRIENDLY MODE
    "friendly": """
Rewrite the text so it sounds friendly and natural.

Return ONLY the rewritten text.
""",

    # ACADEMIC MODE
    "academic": """
Rewrite the text using formal academic English.

Return ONLY the rewritten text.
""",

    # SIMPLIFIES THE TEXT 
    "simplify": """
Rewrite the text using simple English.

Return ONLY the rewritten text.
""",

    # SUMMARISES THE TEXT
    "summarize": """
Summarize the text.

Return ONLY the summary.
""",

    # TRANSLATE THE TEXT
    "translate": """
Translate the text into English.

Return ONLY the translation.
"""
}
