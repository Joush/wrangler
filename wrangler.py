import time
import random
from pynput.keyboard import Key, Controller 

keyboard = Controller()

def type_string_with_delay(character="esc"):
    while(True):
        keyboard.press(Key.esc)
        delay = 120
        time.sleep(delay)

type_string_with_delay()