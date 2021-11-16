from win32com.client import Dispatch
desktop = winshell.desktop()
import os

path = os.path.join(desktop, "Media Player Classic.lnk")
target = r"P:\Media\Media Player Classic\mplayerc.exe"
wDir = r"P:\Media\Media Player Classic"
icon = r"P:\Media\Media Player Classic\mplayerc.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
