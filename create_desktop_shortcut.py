import os, winshell
from win32com.client import Dispatch

# Providing paths and other variables
desktop = winshell.desktop()
path = os.path.join(desktop, "Pairs Game.lnk")
target = r"C:\Games\Pairs-Game-Python\StartGame.bat"
wDir = r"C:\Games\Pairs-Game-Python"
icon = r"C:\Games\Pairs-Game-Python\assets\images\enally.ico"

# Runs WScript.Shell using on windows to execute commands
shell = Dispatch('WScript.Shell')

# Data to be added on shortcut file.
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()


# About Winshell
# The winshell module is a light wrapper around the Windows shell functionality.
# It includes convenience functions for accessing special folders, for using the shell’s file copy, rename & 
# delete functionality, and a certain amount of support for structured storage.

#About Dispatch
# Is event handlerfor Python (runtime)