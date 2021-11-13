
@echo off
move Download_update.bat ..\
move helper.py ..\
timeout 1
python create_desktop_shortcut.py %*
exit