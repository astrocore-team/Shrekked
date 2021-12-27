from __future__ import print_function
from playsound import playsound
import time
import tkinter, threading
from comtypes import CLSCTX_ALL
from tkinter import *
from tkvideo import tkvideo
from pynput.keyboard import Key,Controller
import time
import keyboard
import os
import sys
from win32com.client import Dispatch
import time
desktop = "%UserProfile%\\Desktop"

print(sys.path[0])

video = sys.path[0] + '\\MLG SHREK COMPILATION!.mp4'

def play():
   playsound('SHREK\\meme.mp3')

      

def volume():
    keyboard = Controller()

    while True:
     for i in range(1000):
         keyboard.press(Key.media_volume_up)
         keyboard.release(Key.media_volume_up)
         time.sleep(0.05)
     time.sleep(2)

def shutdown():
    root.destroy()
    quit()

def emergency():
  while True:
       keyboard.wait('ctrl+alt+enter')
       shutdown()

root = Tk()
root.attributes("-fullscreen", True)
root.attributes('-topmost',True)
my_label = Label(root)
my_label.pack()

threading.Thread(target=play).start()
threading.Thread(target=volume).start()
threading.Thread(target=emergency).start()

player = tkvideo(video, my_label, loop = 1, size = (1280,720))
player.play()

def on_closing():
   player = tkvideo(video, my_label, loop = 1, size = (1280,720))
   player.play()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()