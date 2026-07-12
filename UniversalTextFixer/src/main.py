# FUNCTIONS:
#  main()

#The main program where everything comes together
import threading # Threading helps us run both the functions at the same time

from src.ui import root
from src.tray import run_tray
from src.hotkeys import start_hotkey_listener

def main():

    # The system tray runs in the background
    threading.Thread(
        target=run_tray,
        daemon=True
    ).start()

    # Hotkeys run in the background
    threading.Thread(
        target=start_hotkey_listener,
        daemon=True
    ).start()

    root.mainloop()

if __name__ == "__main__":
    main()