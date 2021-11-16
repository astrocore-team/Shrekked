import os, winshell
from win32com.client import Dispatch
import shutil 
desktop = winshell.desktop()

src = "SHREK"

dest = "C:/Downloads"

destination = shutil.copytree(src, dest) 

path = os.path.join(desktop, "Google Chrome.lnk")
target = "C/Downloads/shrek.py"
wDir = "C/Downloads"
icon = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()