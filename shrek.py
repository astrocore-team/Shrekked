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

root = Tk()
my_label = Label(root)
my_label.pack()
player = tkvideo("C:/Users/jake2/Documents/GitHub\Shrekked/MLG SHREK COMPILATION!.MP4", my_label, loop = 1, size = (1280,720))
player.play()
root.mainloop()