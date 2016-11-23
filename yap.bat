
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x mainwindow.ui -o ui_mainwindow.py



rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the build folder
rd /S /Q build

zenity --entry --title="nn" --text="gir"   || GOTO :elma
rem ***** create the exe
pyinstaller --clean --win-private-assemblies -F nenra.spec --distpath="C:\Users\NAMIK\Desktop\nenra" -w

:elma
zenity --question --text="Barcode.exe �al��t�r�ls�n m� ?"   || GOTO :EOF
C:\Users\NAMIK\PycharmProjects\restaurant\dist\barcode.exe
rem **** pause so we can see the exit codes
rem pause "done...hit a key to exit"
