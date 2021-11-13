@Echo OFF
timeout 2

Echo =======================================================
Echo       Developed by - Prashant Kumar and Team Members
Echo =======================================================

@echo off

Echo New directories creation in process...

cd C:\
mkdir Games

Echo Moving to new location...

cd C:\Games

Echo Starting clone do not close this window.

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

timeout 2

start startGame.bat
exit