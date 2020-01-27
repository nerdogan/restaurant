
rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the build folder
rd /S /Q build

rem ***** create the exe
pyinstaller  -F masa.spec --distpath="C:\Users\NAMIK\OneDrive\Desktop\masa"

rem **** pause so we can see the exit codes
rem pause "done...hit a key to exit"
