@Echo OFF
Echo =======================================================
Echo       Developed by - Prashant Kumar
Echo =======================================================
Pause

@echo off

rm -rf Pairs-Game-Python
git clone https://github.com/03prashantpk/Pairs-Game-Python.git

Echo =============================================
Echo              Download Success!
Echo     Location C:\\Games\Pairs-Game-Python 
Echo =============================================


Echo =============================================
Echo   Press ENTER to Start the Game
Echo =============================================

pause

@echo off
cd Pairs-Game-Python/
start startGame.bat

start success.bat
exit