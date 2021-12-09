# -*- coding: utf-8 -*-
import pymongo
import datetime
from socket import *
from escpos.printer import Network,Dummy
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class escpostan():
    def __init__(self):
        self.kontrol = 0
        self.myclient = pymongo.MongoClient("mongodb://192.168.2.251/bishop")
        self.mydb = self.myclient["bishop"]
        self.mycol = self.mydb["bishoppaket2021"]
        self.mycol.update_many({"isPrinted": {"$exists": False}}, {"$set": {"isPrinted": 0}})

    def artir(self):
        self.kontrol=self.kontrol+1


    def parcala(self,a):

        for parca in range(0,len(a),40):
            kelime=a[parca:parca+40]
            img = Image.new("RGB", (550, 34), (255, 255, 255))
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("./images/NotoSans-Regular.ttf", 28)
            print(draw.textsize((kelime), font=font))

            self.artir()
            draw.text((0, -3), (kelime), (0, 0, 0), font=font)
            img.save(str(self.kontrol)+'.png')
            d.image(str(self.kontrol)+'.png')

    def satirparcala(self,a):
        img = Image.new("RGB", (550, 34), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./images/NotoSans-Regular.ttf", 28)
        print(draw.textsize((a), font=font))
        self.artir()
        draw.text((0, -3), (a), (0, 0, 0), font=font)
        img.save(str(self.kontrol)+'.png')
        d.image(str(self.kontrol)+'.png')


    def cumleparcala(self,elma):
        elma=elma.split("\n")
        for a in elma:
            if len(a)>40:
                self.parcala(a)
            else:
                self.satirparcala(a)

elma=escpostan()

for x in elma.mycol.find({"$and":[{"isPrinted":0},{"kaynak":"yemeksepeti"}]}):

    d = Dummy()
    d.text(chr(27))
    d.text(chr(116))
    d.text(chr(61))
    d.codepage = 'CP857'
    d.image("bishopap.png")
    d.text("\n")
    d.set(font='a', align='center', height=1, width=1)
    elma.cumleparcala(x["Teslim tarihi"])
    d.text("\n")
    d.text("-------------------------------------------")
    d.text("\n")

    d.set(font='a', align='left', height=2, width=1)
    elma.cumleparcala(x["Müşteri"])
    elma.cumleparcala(x["Adres"])
    d.text("\n")
    elma.cumleparcala("Telefon : "+x["Telefon 1"])
    d.text("\n")
    d.text("-------------------------------------------")
    d.text("\n")
    print((len(x["urun"])))
    for aa in range(0, len(x["urun"]), 5):
        try:
            d.text(x["urun"][aa].ljust(3) + x["urun"][aa + 1].ljust(27, "_") + x["urun"][aa + 4].rjust(10))
            d.set(font='a', align='center', height=2, width=1)
            d.text("\n"+x["urun"][aa+2]+"\n")

        except:
            d.text(x["urun"][aa].rjust(40, "_"))
    d.text("\n")
    d.text("-------------------------------------------")
    d.text("\n")
    try:
      elma.cumleparcala("Müşteri Notu :"+x["Müşteri Notu"])
    except:
      pass
    d.text("\n")
    elma.cumleparcala(x["Ödeme şekli"])
    d.text(x["kaynak"])
    d.set(font='a', align='center', height=1, width=1)
    d.text("\n")
    if x["Ödeme şekli"]==" Online Kredi/Banka Kartı - Sipariş tutarı internet üzerinden ÖDENMİŞTİR. - Lütfen fiş getiriniz.":
        d.image("online.png")
    elif x["Ödeme şekli"]==" Kredi Kartı (Sipariş tesliminde kredi kartı / banka kartı ile ödeme) - Lütfen fiş getiriniz.":
        d.image("kk.png")
    elif x["Ödeme şekli"] == " Nakit (Nakit ödeme) - Lütfen fiş getiriniz.":
        d.image("tl.png")

    d.cut()

    p = Network("192.168.2.39")
    p._raw(d.output)
    elma.mycol.update_one({'_id': x['_id']}, {"$set": {"isPrinted":1}})


print("sipariş yazma çıkıyor")
elma.myclient.close()


