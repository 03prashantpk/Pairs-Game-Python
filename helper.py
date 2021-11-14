import os 
import time
import shutil

time.sleep(2)

# Folder Name to be deleted
directory = "Pairs-Game-Python"

# Location of the folder to be deleted
parent = "C:\Games"

shutil.rmtree("C:\Games\Pairs-Game-Python", ignore_errors=True)

time.sleep(1)