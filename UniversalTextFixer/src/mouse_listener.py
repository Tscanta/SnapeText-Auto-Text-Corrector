from pynput import mouse, keyboard
from src.ui import root
import src.popup_menu as popup_menu
from src.popup_menu import show_popup

# Keep track of whether Ctrl is being held
ctrl_pressed = False

keyboard_listener = None
mouse_listener = None


def on_press(key):
    global ctrl_pressed

    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_pressed = True


def on_release(key):
    global ctrl_pressed

    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_pressed = False


def on_click(x, y, button, pressed):

    # Close the popup if the user left-clicks outside it
    if (
        pressed
        and button == mouse.Button.left
        and popup_menu.popup_window
    ):

        x1 = popup_menu.popup_window.winfo_rootx()
        y1 = popup_menu.popup_window.winfo_rooty()

        x2 = x1 + popup_menu.popup_window.winfo_width()
        y2 = y1 + popup_menu.popup_window.winfo_height()

        inside = x1 <= x <= x2 and y1 <= y <= y2

        if not inside:
            root.after(
                0,
                lambda: popup_menu.close_popup(popup_menu.popup_window)
            )

        return

    # Open the popup
    if (
        pressed
        and button == mouse.Button.middle
        and ctrl_pressed
    ):
        print("Ctrl + Middle Click detected!")

        root.after(
            0,
            lambda: show_popup(x, y)
        )


def start_mouse_listener():
    global keyboard_listener
    global mouse_listener

    keyboard_listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )

    mouse_listener = mouse.Listener(
        on_click=on_click
    )

    keyboard_listener.start()
    mouse_listener.start()