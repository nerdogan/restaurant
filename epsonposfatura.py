# -*- coding: cp1254 -*-
from escpos import printer
p = printer.Serial("COM1")

# p.image('./images/bishop.png')

p.text("\n\n\n                   30-09-2016 \n\nSET KURUMSAL HIZ. A.S\n")
p.text("Leylak Sk. Nursanlar is Merkezi \n")
p.text("K:8 D:27 SISLI IST \n\n")
p.text("V.D  : Bogazici Kur  7640179796\n\n")
p.text("--------------------------\n")
p.text("YEMEK            138,89\n")
p.text("          KDV %8  11,11\n")
p.text("--------------------------\n")
p.text("        TOPLAM : 150,00\n")
p.text("--------------------------\n\n")
p.text("Yuzelli TL")
p.text("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
p.text("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

p.text('NEN 2016\n')
p.text("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


