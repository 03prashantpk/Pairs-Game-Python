move Download_update.bat ..\
move helper.py ..\
timeout 5
python create_desktop_shortcut.py %*
exit