import twain
from PIL import Image

index = 11;

def next(ss):
    try:
        print ss.GetImageInfo()
        return True
    except:
        return False

def capture(ss):
    global index
    rv = ss.XferImageNatively()
    fileName = str(index) + '_image.bmp';
    index+=1;
    print rv;
    if rv:
        (handle, count) = rv
        twain.DIBToBMFile(handle, fileName)
    img=Image.open(fileName)
    dosya=fileName+".pdf"
    img.save(dosya)

sm = twain.SourceManager(0)

ss = sm.OpenSource('WIA-Brother MFC-1910W series [38b 1.0(32-32)')

try:
    print "elma"
    print ss.SetCapability(twain.CAP_FEEDERENABLED,twain.TWTY_BOOL,True)



except:
    print "Could not set duplex to True"

print "acquire image"
ss.RequestAcquire(0,0)


print ss.GetImageLayout()

while next(ss):
    capture(ss)

print('Done')