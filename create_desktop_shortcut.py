import os, winshell
from win32com.client import Dispatch

desktop = winshell.desktop()
path = os.path.join(desktop, "Pairs Game.lnk")
target = r"C:\Games\Pairs-Game-Python\StartGame.bat"
wDir = r"C:\Games\Pairs-Game-Python"
icon = r"C:\Games\Pairs-Game-Python\assets\images\enally.ico"

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()