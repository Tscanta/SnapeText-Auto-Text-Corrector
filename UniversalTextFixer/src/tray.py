# FUNCTIONS:
#  on_open_settings(),
#  run_tray()

import os 
import sys
import subprocess
from PIL import Image
import pystray

from src.settings.settings_window import open_settings
from src.shutdown import shutdown


# Opens the settings window
def on_open_settings(icon, item):
    open_settings()

# Restarts SnapeText
def on_restart(icon, item):
    print("Restarting SnapeText...")

    icon.stop()

    subprocess.Popen(
        [sys.executable, "-m", "src.main"]
    )

    os._exit(0)

# CREATING THE SYSTEM TRAY APPLICATION
def run_tray():

    # Create a new tray icon
    icon = pystray.Icon("SnapeText")

    # Set the tray icon image
    icon.icon = Image.open("assets/snape_tray_icon_v0.8.ico")

    # Tooltip shown when hovering over the icon
    icon.title = "SnapeText"

    # Right-click menu
    icon.menu = pystray.Menu(

        # Open settings button
        pystray.MenuItem(
            "Settings",
            on_open_settings
        ),

        # Restart SnapeText
        pystray.MenuItem(
            "Restart SnapeText",
            on_restart
        ),

        pystray.Menu.SEPARATOR,

        # Exit button
        pystray.MenuItem(
            "Exit",
            lambda icon, item: shutdown(icon)
        )
    )

    print("SnapeText is running in the system tray.")

    # Keep the tray application running
    icon.run()