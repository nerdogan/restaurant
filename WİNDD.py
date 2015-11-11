__author__ = 'NAMIK'
import subprocess as SP
# call an OS subprocess $ zenity --entry --text "some text"
# (this will ask OS to open a window with the dialog)
res=SP.Popen(['zenity','--entry','--text',
'please write some text'], stdout=SP.PIPE)
# get the user input string back
usertext=str(res.communicate()[0][:-1])
# adjust user input string
text=usertext[0:-1]
print("I got this text from the user: %s"%text)