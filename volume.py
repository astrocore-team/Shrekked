from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from pynput.keyboard import Key,Controller
keyboard = Controller()
import time

while True:
    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.1)
    time.sleep(2)
