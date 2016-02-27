__author__ = 'NAMIK'
import subprocess
import twain
import PIL.Image as Image
import PIL.ImageFilter as ImageFilter
sm = twain.SourceManager(0)
ss = sm.OpenSource('WIA-Brother MFC-1910W series [38b 1.0(32-32)')
ss.RequestAcquire(1,1)
if hasattr(ss, 'ModalLoop'):
    ss.ModalLoop()
rv = ss.XferImageNatively()
if rv:
    (handle, count) = rv
    print count
    twain.DIBToBMFile(handle, 'image.bmp')

img=Image.open("image.bmp")
left = 0
top = 0
width = 900
height = 1200
box = (left, top, left+width, top+height)
area = img.crop(box)

half = 0.5
im = area.resize( [int(half * s) for s in area.size] )

res=subprocess.Popen(['zenity','--entry','--text','Personel ismi Giriniz'], stdout=subprocess.PIPE)
usertext=str(res.communicate()[0][:-1])
barcode_value=usertext[0:-1]
dosya=barcode_value+".png"
im.save(dosya, 'png')
img = img.filter(ImageFilter.SHARPEN)
dosya=barcode_value+".pdf"
img.save(dosya)
