from ctypes import cast, POINTER
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
player = tkvideo("C:\Users\jake2\Documents\GitHub\Shrekked\MLG SHREK COMPILATION!", my_label, loop = 1, size = (1280,720))
player.play()

root.mainloop()

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume 
currentVolumeDb = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(currentVolumeDb + 10.1, None)
# NOTE: -6.0 dB = half volume !