# -*- coding: cp1254 -*-
from escpos import *
p = printer.Network("192.168.2.223")

p.image('./images/bishop.png')

p.text("Big line\n")
p.text(chr(27))
p.text(chr(45))
p.text(chr(50))
p.text(u'on bahce\n')
p.text(chr(27))
p.text(chr(33))
p.text(chr(17))
p.text('BIG TEXT\n')
pbarcode("bishop", "CODE39",80,3,"BELOW", "A")
p.cut()