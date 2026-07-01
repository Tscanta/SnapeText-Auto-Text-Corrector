from PIL import Image
import pystray

from src.settings.settings_window import open_settings
from src.shutdown import shutdown


# Opens the settings window
def on_open_settings(icon, item):
    open_settings()


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