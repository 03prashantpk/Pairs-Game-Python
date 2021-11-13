import os 
import time

# adding 2second delay to shutdown all game file before updating
time.sleep(2)

# Folder Name to be deleted
directory = "Pairs-Game-Python"

# Location of the folder to be deleted
parent = "C:\Games"
    
#Full path to be deleted Path 
path = os.path.join(parent, directory) 
    
# Remove the Directory to download new updates
os.rmdir(path)

