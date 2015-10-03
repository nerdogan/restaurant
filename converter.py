__author__ = 'NAMIK'
import PIL
from PIL import Image
import os
import sys
def readf():
    try:

        input_dir  = "C:\Users\NAMIK\Desktop\kressin"  #path to img source folder
        img_size1   = "722" #The image size (128, 256,etc)
        img_size2   = "480" #The image size (128, 256,etc)
        output_dir  = "C:\Users\NAMIK\Desktop\kressinn"
        print "starting...."
        print "Colecting data from %s " % input_dir
        tclass = [ d for d in os.listdir( input_dir ) ]
        counter = 0
        strdc = ''
        hasil = []
        for x in tclass:
            print x
            list_dir =  os.path.join(input_dir, x )
            list_tuj = os.path.join(output_dir+'/', x+'/')
            if not os.path.exists(list_tuj):
                os.makedirs(list_tuj)
            if os.path.exists(list_tuj):
                for d in os.listdir(input_dir):
                    try:
                        print d
                        img = Image.open(input_dir+'/'+d)
                        img = img.resize((int(img_size1),int(img_size2)),Image.ANTIALIAS)
                        fname,extension = os.path.splitext(d)
                        newfile = fname+extension
                        if extension != ".jpg" :
                            newfile = fname + ".jpg"
                        img.save(os.path.join(output_dir+'/'+x,newfile),"JPEG",quality=90)
                        print "Resizing file : %s - %s " % (x,d)
                    except Exception,e:
                        print "Error resize file : %s - %s " % (x,d)
                        sys.exit(1)
            counter +=1
    except Exception,e:

        print "Error, check Input directory etc : ", e
        sys.exit(1)
readf()