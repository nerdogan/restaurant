# -*- coding: utf-8 -*
import modulemdb
from escpos.printer import Network
p = Network("192.168.2.222")

p.image('./images/bishop.png')
p.set(font='a', align='center',height=1,width=1)

p.text("MUTFAK\n")
p.text(chr(27))
p.text(chr(116))
p.text(chr(61))
p.text(u'ulaşım  öçşiğü ÖÇŞİĞÜ\n')
p.text(chr(27))
p.text(chr(33))
p.text(chr(17))
p.text('NEN 2016 \n')
p.qr("http://nen.duckdns.org/kasa.php",size=int(6))
p.barcode("3058", "CODE39",80,3)
p.set(font='a', align='left',height=1,width=1)
a="01234567890123456789"
b=a.ljust(5)
p.text(b)
p.text("100,00 \n")
b=a.ljust(30)
p.text(b)
p.text("100,00 \n")
p.text("012345678901234567890012345678901234567890")

p.cut()