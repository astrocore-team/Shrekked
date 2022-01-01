from __future__ import print_function
from genericpath import exists
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
from win32com.client import Dispatch
import time
from urllib.request import urlopen
import pyautogui
from pathlib import Path

pyautogui.FAILSAFE = False

# Find monitor width/height

width, height= pyautogui.size()

# Lock mouse

def mouse():
 while True:
    if keyboard.is_pressed('ctrl+alt+enter'):
        break
    else:
        pyautogui.moveTo(width/2, height/2)

threading.Thread(target=mouse).start()

# Create Reference to desktop

desktop = "%UserProfile%\\Desktop"

# Create References to Downloads and Path

path = "C:/Shrek_Files"
url = "https://astrocore.net/gallery/meme.mp3"
url2 = "https://astrocore.net/gallery/meme-ts1640990550.mp4"

file1 = Path('C:/Shrek_Files/meme.mp4')
file2 = Path('C:/Shrek_Files/meme.mp3')

# Create the Directory for virus files

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    print ("(Does it already exist?)")
else:
    print ("Successfully created the directory %s " % path)

print("Preparing for launch.")

# Path to files

video = "C:/Shrek_Files/meme.mp4"
sound = "C:/Shrek_Files/meme.mp3"

# Download files if non-existing

if file2.exists():
    print("File exists. Skipping Download")
else:
    print("Downloading " + url)
    with open("C:/Shrek_Files/meme.mp3", 'wb') as local:
        with urlopen(url) as remote:
            local.write(remote.read())

if file1.exists():
    print("File exists. Skipping Download")
else:
    print("Downloading " + url2)
    with open("C:/Shrek_Files/meme.mp4", 'wb') as local:
        with urlopen(url2) as remote:
            local.write(remote.read())

# Countdown

time.sleep(1)
print('Starting in 3')
time.sleep(1)
print('Starting in 2')
time.sleep(1)
print('Starting in 1')

# Play audio

def play():
 while True:
       playsound(sound)

# Change volume

def volume():
    keyboard = Controller()

    while True:
     for i in range(1000):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            time.sleep(0.05)
     time.sleep(2)

# Shutdown function

def shutdown():
    root.destroy()
    quit()

# Waiting For ctrl+alt+enter shortcut

def emergency():
  while True:
       keyboard.wait('ctrl+alt+enter')
       shutdown()

# Create video

root = Tk()
root.attributes("-fullscreen", True)
root.attributes('-topmost',True)
my_label = Label(root)
my_label.pack()

# Start all threads

threading.Thread(target=play).start()
threading.Thread(target=volume).start()
threading.Thread(target=emergency).start()

# Start playing video

player = tkvideo(video, my_label, loop = 1, size = (width, height))
player.play()

# Stop window from being closable

def on_closing():
   player = tkvideo(video, my_label, loop = 1, size = (width, height))
   player.play()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Showing How to stop virus

print("Close this console to shutdown Virus!")

root.mainloop()