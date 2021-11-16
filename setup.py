import os, winshell
from win32com.client import Dispatch
desktop = winshell.desktop()

path = os.path.join(desktop, "Google Chrome.lnk")
target = "C:\\Users\\Jake Gorham\\Documents\\GitHub\\Shrekked\\shrek.py"
wDir = "C:\\Users\\Jake Gorham\\Documents\\GitHub\\Shrekked"
icon = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()