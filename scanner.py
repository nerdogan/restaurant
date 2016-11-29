# -*- coding:utf8 -*-
__author__ = 'NAMIK ERDOĞAN'
import subprocess
import twain
import PIL.Image as Image
import PIL.ImageFilter as ImageFilter
import sys
reload(sys)



sm = twain.SourceManager(0)
ss = sm.OpenSource()
ss.RequestAcquire(1,1)
if hasattr(ss, 'ModalLoop'):
    ss.ModalLoop()
rv = ss.XferImageNatively()
if rv:
    (handle, count) = rv
    print count
    twain.DIBToBMFile(handle, 'image.bmp')

img=Image.open("image.bmp")
img = img.filter(ImageFilter.SHARPEN)
"""
left = 0
top = 0
width = 2480
height = 3508
box = (left, top, left+width, top+height)
area = img.crop(box)

half = 0.23
im = area.resize( [int(half * s) for s in area.size] )
"""
im=img
res=subprocess.Popen(['zenity','--entry','--text','  isim Giriniz'], stdout=subprocess.PIPE)
usertext=str(res.communicate()[0][:-1])
barcode_value=usertext[0:-1]
dosya="./images/"+barcode_value+".png"

im.save(dosya, 'png')

dosya="./images/"+barcode_value+".pdf"
img.save(dosya)
