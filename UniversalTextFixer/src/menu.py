from src.corrector import run_correction

def show_menu():

    print("\n==========================")
    print("        SNAPE")
    print("==========================")
    print("1. Grammar")
    print("2. Professional")
    print("3. Friendly")
    print("4. Academic")
    print("5. Simplify")
    print("6. Translate")
    print("7. Summarize")
    print("0. Cancel")
    print("==========================")
    choice = input("\nChoose an option: ")

    modes = {
        "1": "grammar",
        "2": "professional",
        "3": "friendly",
        "4": "academic",
        "5": "simplify",
        "6": "translate",
        "7": "summarize"
    }

    if choice == "0":
        print("Cancelled.")
        return

    if choice not in modes:
        print("Invalid option.")
        return

    run_correction(modes[choice])