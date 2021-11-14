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

# Module Details

#Shutil - module
#Shutil module in Python provides many functions of high-level operations on files and collections of files. 
# It comes under Python's standard utility modules. 
# This module helps in automating process of copying and removal of files and directories.

#os - module
#The OS module in Python provides functions for interacting with the operating system. 
# OS comes under Python's standard utility modules. 
# This module provides a portable way of using operating system-dependent functionality. ... path* 
# modules include many functions to interact with the file system.