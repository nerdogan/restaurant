__author__ = 'NAMIK'
from ctypes import *
# give location of dll
mydll = cdll.LoadLibrary("zkemsdk.dll")
ip = "192.168.2.224"

port = 4370

print mydll.Z_Connect_NET(c_char_p(ip),c_int(port))