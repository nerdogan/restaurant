__author__ = 'NAMIK'
import subprocess
import twain
from PIL import Image

sm = twain.SourceManager(0)
ss = sm.OpenSource()
ss.RequestAcquire(0,0)

rv = ss.XferImageNatively()
if rv:
    (handle, count) = rv
    twain.DIBToBMFile(handle, 'image.bmp')

img=Image.open("image.bmp")
left = 0
top = 0
width = 580
height = 780
box = (left, top, left+width, top+height)
area = img.crop(box)

half = 0.5
im = area.resize( [int(half * s) for s in area.size] )

res=subprocess.Popen(['zenity','--entry','--text','Personel ismi Giriniz'], stdout=subprocess.PIPE)
usertext=str(res.communicate()[0][:-1])
barcode_value=usertext[0:-1]
dosya=barcode_value+".png"
im.save(dosya, 'png')
img.save(barcode_value+".pdf", 'pdf')
img.close()