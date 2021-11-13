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

# Path 
#path = os.path.join(parent, directory) 


    
# Remove the Directory to download new updates
#os.rmdir(path)