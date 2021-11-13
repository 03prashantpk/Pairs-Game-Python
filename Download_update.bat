@Echo OFF
Echo Reading Software requirements...
Echo Working on Directory Creation...
Echo Diretory Creation Succcess!

timeout 4

cd ..\

python Helper.py %*

timeout 2

Echo ===========================================================
Echo       Developed by - Prashant Kumar & other team member
Echo ===========================================================

@echo off

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
Echo   Launching The Game... 
Echo ============================================

timeout 5

start startGame.bat
exit