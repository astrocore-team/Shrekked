
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
from pydub.playback import play
import subprocess

n = -1
I = 10

#audio = AudioSegment.from_file("C:/Users/Jake Gorham/Documents/GitHub/Shrekked/MEME.mp3") #your audio file
#play(audio * n)  #Play audio 2 times
root = Tk()
root.attributes("-fullscreen", True)
root.attributes('-topmost',True)
my_label = Label(root)
my_label.pack()
player = tkvideo("C:/Users/Jake Gorham/Documents/GitHub/Shrekked/MLG SHREK COMPILATION!.mp4", my_label, loop = 1, size = (1280,720))
player.play()

def on_closing():
    player = tkvideo("C:/Users/Jake Gorham/Documents/GitHub/Shrekked/MLG SHREK COMPILATION!.mp4", my_label, loop = 1, size = (1280,720))
    player.play()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

def set_master_volume(self, widget):
    val = self.volume
    val = float(int(100))
    proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
    proc.wait()
