from win32com.client import Dispatch
import os
import winshell
desktop = winshell.desktop()

path = os.path.join(desktop, "Google Chrome.lnk")
target = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
wDir = "C:\\Program Files\\Google\\Chrome\\Application"
icon = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
