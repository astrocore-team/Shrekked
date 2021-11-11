from ctypes import cast, POINTER
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import os
import sys
import Tkinter as tkinter
import gobject
import gst

video_name = "C:\Users\jake2\Documents\GitHub\Shrekked\MLG SHREK COMPILATION!.MKV"

def on_sync_message(bus, message, window_id):
        if not message.structure is None:
            if message.structure.get_name() == 'prepare-xwindow-id':
                image_sink = message.src
                image_sink.set_property('force-aspect-ratio', True)
                image_sink.set_xwindow_id(window_id)

gobject.threads_init()

window = tkinter.Tk()
window.geometry('500x400')

video = tkinter.Frame(window, bg='#000000')
video.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)

window_id = video.winfo_id()

player = gst.element_factory_make('playbin2', 'player')
player.set_property('video-sink', None)
player.set_property('uri', 'C:\Users\jake2\Documents\GitHub\Shrekked\MLG SHREK COMPILATION!.MKV' % (os.path.abspath(sys.argv[1])))
player.set_state(gst.STATE_PLAYING)

bus = player.get_bus()
bus.add_signal_watch()
bus.enable_sync_message_emission()
bus.connect('sync-message::element', on_sync_message, window_id)

window.mainloop()

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume 
currentVolumeDb = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(currentVolumeDb + 10.1, None)
# NOTE: -6.0 dB = half volume !