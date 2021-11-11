from ctypes import cast, POINTER
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

video_name = "test.mkv" #This is your video file path
video = imageio.get_reader(video_name)

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume 
currentVolumeDb = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(currentVolumeDb + 10.1, None)
# NOTE: -6.0 dB = half volume !