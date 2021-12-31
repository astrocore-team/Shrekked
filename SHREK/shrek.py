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
import urllib
from urllib.request import urlopen

desktop = "%UserProfile%\\Desktop"

path = "C:/Shrek_Files"
url = "https://astrocore.net/gallery/meme.mp3"
url2 = "https://astrocore.net/gallery/meme-ts1640990550.mp4"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    print ("(Does it already exist?)")
else:
    print ("Successfully created the directory %s " % path)


video = "C:/Shrek_Files/meme.mp4"
sound = "C:/Shrek_Files/meme.mp3"

with open("C:/Shrek_Files/meme.mp3", 'wb') as local:
  with urlopen(url) as remote:
    local.write(remote.read())

with open("C:/Shrek_Files/meme.mp4", 'wb') as local:
  with urlopen(url2) as remote:
    local.write(remote.read())

time.sleep(5)

def play():
 while True:
      playsound(sound)

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