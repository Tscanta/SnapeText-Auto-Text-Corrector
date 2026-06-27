import win32gui
import win32con
import win32process
import win32api
import win32com.client
import ctypes

previous_window = None


def save_active_window():
    global previous_window
    previous_window = win32gui.GetForegroundWindow()
    print(f"Saved window: {previous_window}")


def restore_active_window():
    global previous_window

    if previous_window is None:
        return

    shell = win32com.client.Dispatch("WScript.Shell")

    # Trick Windows into allowing focus change
    shell.SendKeys("%")

    win32gui.ShowWindow(previous_window, win32con.SW_RESTORE)

    win32gui.SetForegroundWindow(previous_window)

    print("Restored:", previous_window)