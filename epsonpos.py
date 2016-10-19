# -*- coding: cp1254 -*-
from escpos.printer import Network
p = Network("192.168.2.223")

p.image('./images/bishop.png')

p.text("MUTFAK\n")
p.text(chr(27))
p.text(chr(45))
p.text(chr(50))
p.text(u'DONDURUCU\n')
p.text(chr(27))
p.text(chr(33))
p.text(chr(17))
p.text('NEN 2016 \n')
p.barcode("3057", "CODE39",80,3,"BELOW", "A")
p.text('\n')
p.barcode("3058", "CODE39",80,3)
p.cut()