# -*- coding: cp1254 -*-
from escpos import *
p = printer.Network("192.168.2.223")

p.image('./images/bishop.png')

p.text("Big line\n")
p.text(u'on bahce\n')
p.text(chr(27))
p.text(chr(33))
p.text(chr(17))
p.text('BIG TEXT\n')
p.cut()