import json
import time

from pynput.mouse import Controller as MouseController, Button as MouseButton
from pynput.keyboard import Controller as KeyboardController, Key
from .constants import PLAYBACK_SPEED, RECORDING_SPEED, FILE_NAME

def play(filename = FILE_NAME, playback_speed = PLAYBACK_SPEED, recording_speed = RECORDING_SPEED):
    mouse = MouseController()
    keyboard = KeyboardController()
    
    with open(filename, "r") as f:
        data = json.load(f)
    
    if playback_speed != PLAYBACK_SPEED:
        speed = playback_speed / recording_speed if recording_speed > 0 else playback_speed
    else:
        speed = playback_speed
    
    SPECIAL_KEYS = {
        "enter": Key.enter,
        "space": Key.space,
        "shift": Key.shift,
        "left": Key.left,
        "right": Key.right,
        "up": Key.up,
        "down": Key.down,
        # "key_name": Key.key
    }

    start_time = time.perf_counter()

    for i in range(0, len(data), 2):
        wait_time = data[i] / speed
        while time.perf_counter() - start_time < wait_time:
            pass  # Busy wait

        start_time += wait_time
        
        # mouse input
        if data[i+1][0] == "m":
            mouse_action_string = data[i+1]
            mouse_button = \
            MouseButton.left if mouse_action_string[1] == 'l' \
            else MouseButton.right if mouse_action_string[1] == 'r' \
            else MouseButton.middle
            
            action = mouse_action_string[-1]
            x, y = mouse_action_string[2:-1].split(',')
            x, y = int(x), int(y)
            
            mouse.position = (x, y)
            if action == 'd':
                mouse.press(mouse_button)
            else:
                mouse.release(mouse_button)
        else:
            key, action = data[i+1][0:-1], data[i+1][-1]
            key = SPECIAL_KEYS.get(key, key)  # get special key
            if action == 'd':
                keyboard.press(key)
            else:
                keyboard.release(key)

    #print("Playback finished.")