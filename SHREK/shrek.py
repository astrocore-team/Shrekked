from __future__ import print_function
from playsound import playsound
from ctypes import cast, POINTER
import time, os, tkinter as tk
from threading import Thread
import tkinter as tk, threading
from comtypes import CLSCTX_ALL
from tkinter import *
from tkvideo import tkvideo
from pynput.keyboard import Key,Controller
import time
import keyboard
import os
from win32com.client import Dispatch
import shutil
import time
import subprocess
desktop = "%UserProfile%\\Desktop"

src = "SHREK"

dest = "C:/SHREK"

destination = shutil.copytree(src, dest) 
print('File copied.')

time.sleep(1)

n = -1
I = 10

def play():
 for i in range(1000):
     playsound("C:/SHREK/meme.mp3")

      

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
    exit("shrek.py")

def emergency():
  while True:
       keyboard.wait('ctrl+alt+enter')
       shutdown()

root = Tk()
root.attributes("-fullscreen", True)
root.attributes('-topmost',True)
my_label = Label(root)
my_label.pack()

threading.Thread(target=volume).start()
threading.Thread(target=play).start()
threading.Thread(target=emergency).start()

player = tkvideo("C:/SHREK/MLG SHREK COMPILATION!.mp4", my_label, loop = 1, size = (1280,720))
player.play()

def on_closing():
   player = tkvideo("C:/SHREK/MLG SHREK COMPILATION!.mp4", my_label, loop = 1, size = (1280,720))
   player.play()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()