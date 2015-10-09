
python C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py -x mainwindow.ui -o ui_mainwindow.py



rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the build folder
rd /S /Q build

rem ***** create the exe
python setup.py py2exe --includes sip
C:\Users\NAMIK\PycharmProjects\restaurant\dist\nenra.exe
rem **** pause so we can see the exit codes
rem pause "done...hit a key to exit"
