import sys
import pystray
from PIL import Image, ImageDraw
from src.settings.settings_window import open_settings
from src.shutdown import shutdown

#CREATING THE ICON THAT WILL APPEAR IN THE SYSTEM TRAY
def create_icon():

    # Create a blank 64x64 white image
    image = Image.new("RGB", (64, 64), "white")

    # Allows us to draw on the image
    draw = ImageDraw.Draw(image)

    # Draw a black square in the middle
    draw.rectangle((16, 16, 48, 48), fill="black")

    # Return the finished icon
    return image

# STOPS RUNNING WHEN THE USER CLICKS 'ESC'/'EXIT'
def on_exit(icon, item):
    print("Closing Snape...")
    sys.exit(0)

# Opens the settings window
def on_open_settings(icon, item):
    open_settings()

# CREATING THE SYSTEM TRAY APPLICATION
def run_tray():
    global TRAY_ICON

    # Create a new tray icon
    icon = pystray.Icon("Snape")

    # Set the tray icon image
    icon.icon = create_icon()

    # Tooltip shown when hovering over the icon
    icon.title = "Snape"

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
            shutdown
        )
    )

    print("Snape is running in the system tray.")
    # Keep the tray application running
    icon.run()
   
