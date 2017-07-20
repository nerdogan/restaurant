# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     22.06.2016
# Copyright:   (c) NAMIK ERDOĞAN  2016
# Licence:     
# "C:\Program Files (x86)\gs\gs9.10\bin\gswin32.exe"  -sDEVICE=png16m -dTextAlphaBits=4 -r300 -o a%03d.png EKSTRE0101201719072017.pdf
#-------------------------------------------------------------------------------

import PIL.Image as Image
import PIL.ImageFilter as ImageFilter

size=550,778
img=Image.open("a005.png")


im=img
barcode_value="elma"
dosya="./images/"+barcode_value+".png"
im.thumbnail(size, Image.ANTIALIAS)
im.save(dosya, 'png')
