@Echo OFF
Echo =============================================
Echo           Searching for Updates 
Echo =============================================

Echo Reading Software requirements...

timeout 2

Echo Moving Directory Success

cd ..\

python Helper.py %*

timeout 1

Echo ===========================================================
Echo       Developed by - Prashant Kumar & other team member
Echo ===========================================================

@echo off

Echo New Directory Created

cd C:\Games\

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
Echo           Launching The Game... 
Echo =============================================

timeout 2

start startGame.bat
exit