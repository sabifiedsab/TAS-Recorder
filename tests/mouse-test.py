from pynput.mouse import Controller, Button
import time

mouse = Controller()

# Test move to position
mouse.position = (1197,1060)
time.sleep(1)

# Test click
mouse.click(Button.left)