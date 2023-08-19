import json
import time

from pynput.mouse import Listener as MouseListener, Controller as MouseController, Button as MouseButton
from pynput.keyboard import Listener as KeyboardListener, Key
from .constants import PLAYBACK_SPEED, RECORDING_SPEED, INCLUDE_MOUSE, FILE_NAME

def record(output_file=FILE_NAME, include_mouse = INCLUDE_MOUSE):
    data = []
    start_time = time.perf_counter()
    last_time = start_time
    
    # Mouse event callback
    def on_click(x, y, button, pressed):
        if not include_mouse: return # if you're not planning to use the mouse just return
        
        nonlocal last_time
        
        current_time = time.perf_counter()
        elapsed_time = current_time - last_time
        
        mouse_button = 'l' if button == MouseButton.left else 'r' if button == MouseButton.right else 'm'
        action = 'd' if pressed else 'u'
        data.extend([elapsed_time, f"m{mouse_button}{x},{y}{action}"])

        last_time = current_time

    def on_key(key, action):
        nonlocal last_time
        
        current_time = time.perf_counter()
        elapsed_time = current_time - last_time
        
        # Handle special keys
        if hasattr(key, 'char') and key.char is not None:
            key_name = key.char
        elif hasattr(key, 'name'):
            key_name = key.name
        else:
            key_name = str(key)
            
        action_type = 'd' if action else 'u'
        data.extend([elapsed_time, f"{key_name}{action_type}"])

        last_time = current_time
        
        # Stop recording if ESC is pressed
        if key == Key.esc:
            return False
    
    #print("Recording... Press ESC to stop.")
    
    with MouseListener(on_click=on_click) as mouse_listener, \
    KeyboardListener(on_press=lambda key: on_key(key, True), on_release=lambda key: on_key(key, False)) as key_listener:
        # we're handling all of the data code in the callback functions
        key_listener.join()

    data = data[0:-2]

    with open(output_file, "w") as f:
        json.dump(data, f)

    #print(f"Recording saved to {output_file}")