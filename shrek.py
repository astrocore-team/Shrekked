
from __future__ import print_function
import volume
from ctypes import cast, POINTER
import time, os, ctypes, tkinter as tk, random, winsound
from threading import Thread
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from tkinter import *
from tkvideo import tkvideo
from pydub import AudioSegment
from pydub import AudioSegment
from pydub.playback import play
import subprocess


n = -1
I = 10

os.system('volume.py')
root = Tk()
root.attributes("-fullscreen", True)
root.attributes('-topmost',True)
my_label = Label(root)
my_label.pack()
player = tkvideo("C:/Users/Jake Gorham/Documents/GitHub/Shrekked/MLG SHREK COMPILATION!.mp4", my_label, loop = 1, size = (1280,720))
player.play()

#song = AudioSegment.from_mp3("C:/Users/Jake Gorham/Documents/GitHub/Shrekked/MEME.mp3")
#play(song)


#def on_closing():
#    player = tkvideo("C:/Users/Jake Gorham/Documents/GitHub/Shrekked/MLG SHREK COMPILATION!.mp4", my_label, loop = 1, size = (1280,720))
#    player.play()

#root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
