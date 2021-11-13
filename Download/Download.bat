@Echo OFF
timeout 5

Echo =======================================================
Echo       Developed by - Prashant Kumar and Team Members
Echo =======================================================

@echo off

cd C:\
mkdir Games

cd C:\Games

rm -rf Pairs-Game-Python
git clone https://github.com/03prashantpk/Pairs-Game-Python.git

Echo =============================================
Echo              Download Success!
Echo     Location C:\Games\Pairs-Game-Python 
Echo =============================================

@echo off
cd Pairs-Game-Python/
start success.bat

Echo =============================================
Echo   Launching The Game... 
Echo ============================================

timeout 5

start startGame.bat
exit