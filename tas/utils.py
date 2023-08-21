from pynput.keyboard import Key
from gui import gui

def get_special_key(key_name):
    if hasattr(Key, key_name):
        return getattr(Key, key_name)
    return key_name

def LaunchGUI():
    return gui.TASRecorderGUI()
