__author__ = 'NAMIK'

import MySQLdb as mdb
from socket import *
from datetime import timedelta,datetime
import time
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *

tgtIP = gethostbyname('nen.duckdns.org')
print(tgtIP)
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8',port=30000)
curmy = conmy.cursor()
curmy.execute("SET NAMES UTF8")
curmy.execute("SET character_set_client=utf8")
gunliste=[]

ayliste=[]

tarihh="2021-01-21"
interval_num=0
dt= datetime.strptime(tarihh, '%Y-%m-%d').date()


def cevirgunsaat(time):

    day = time // (9 * 60)
    time = time % (9 * 60)
    hour = time // 60
    time %= 60
    minutes = time
    return (" %d gün %d saat %d dk" % (day, hour, minutes))

def last_day_of_month( any_day):
    any_day = datetime.strptime(any_day, '%Y-%m-%d').date()
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return (next_month - timedelta(days=next_month.day)).day


bul =curmy.execute("select adsoyad,tarih,saat,enrolgc from personelgc where tarih between '2021-01-21' and '2021-02-21'  order by enrolgc,tarih,saat")
bul=curmy.fetchall()
print (bul)
#for day in range(1,last_day_of_month(tarihh)+1):
for day in range(1, 32):
    interval_type = 'days'
    one_day = timedelta(**{interval_type: interval_num})
    dt1=dt+one_day
    t=dt1.timetuple()
    tt1=str(t[0])+"-"+str(t[1])+"-"+str(t[2])

    tt1= datetime.strptime(tt1, '%Y-%m-%d').date()
    gunliste.append(tt1)
    gunliste.append(0)
    gunliste.append(0)
    gunliste.append("GELMEDİ")
    gunliste.append(bul[0][0])
    gunliste.append(bul[0][3])
    ayliste.append(gunliste)
    gunliste = []

    interval_num = interval_num + 1

a=0
c=bul[0][3]
cliste=[]
for b in (bul):

    if c==b[3]:
        pass
    else:
        cliste.append(ayliste)
        ayliste=[]
        gunliste=[]
        a=0
        tar=0
        sat=0
        c=b[3]


        tarihh = "2021-01-21"
        interval_num = 0
        dt = datetime.strptime(tarihh, '%Y-%m-%d').date()

        for day in range(1, 32):
            interval_type = 'days'
            one_day = timedelta(**{interval_type: interval_num})
            dt1 = dt + one_day
            t = dt1.timetuple()
            tt1 = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2])

            tt1 = datetime.strptime(tt1, '%Y-%m-%d').date()
            gunliste.append(tt1)
            gunliste.append(0)
            gunliste.append(0)
            gunliste.append("GELMEDİ")
            gunliste.append(b[0])
            gunliste.append(b[3])
            ayliste.append(gunliste)
            gunliste = []

            interval_num = interval_num + 1

    if (a==1) and (tar!=b[1]) and (b[2])>timedelta(hours=7) :
        a=0

    if(a==1):
        print (tar,sat,b[1],b[2])
        if tar==b[1]:
            d1 = '2020-01-01 ' + str(b[2] - sat)
        else:
            d1 = '2020-01-01 ' + str(b[2] - sat+timedelta(hours=24))

        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = datetime.strptime(d1, fmt)
        d2 = '2020-01-01 9:00:00'
        d2 = datetime.strptime(d2, fmt)

        # Convert to Unix timestamp

        d1_ts = time.mktime(d1.timetuple())
        d2_ts = time.mktime(d2.timetuple())

        # They are now in seconds, subtract and then divide by 60 to get minutes.

        print(tar,sat,b[2], int((d2_ts - d1_ts) / 60))
        for gunliste in ayliste:
            if tar in gunliste:
                gunliste[1]=sat
                gunliste[2]=b[2]
                gunliste[3]=int((d1_ts - d2_ts) / 60)
                break
        a=0
        continue


    if (b[2])>timedelta(hours=7) and (b[2])<timedelta(hours=21)  :
        tar=b[1]
        sat=b[2]
        a=1
        for gunliste in ayliste:
            if tar in gunliste:
                gunliste[1]=sat
                gunliste[3] = "EKSİK"
                break
        continue


    if (b[2])<timedelta(hours=7)   :

        for gunliste in ayliste:
            if (b[1]-timedelta(hours=24)) in gunliste:

                gunliste[2]=b[2]
                gunliste[3]="EKSİK"
                break
        a=0
    if (b[2]) > timedelta(hours=21):

        for gunliste in ayliste:
            if b[1] in gunliste:
                gunliste[2]=b[2]
                gunliste[3]="EKSİK"
                break
        a=0
cliste.append(ayliste)


# listeleme ve pdf oluşturma

c = canvas.Canvas("...TAM" + str(tarihh) + str(tar)+".pdf")

pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
print(c.getAvailableFonts())
c.setFont("Verdana", 12)

item = u"BISHOP PERSONEL DEVAM LİSTESİ     "
c.drawString(55, 815, item)
c.setFont("Verdana", 8)

item = " AD SOYAD                   TARİH            GİRİŞ          ÇIKIŞ           FARK            "
c.drawString(10, 800, item)
aa = 0
bb = 0
toplam = 0
toplam1 = 0.0
toplam2 = 0.0000

for ayliste in cliste:
    for gunliste in ayliste:

        print (gunliste[5],gunliste[4],gunliste[0],gunliste[1],gunliste[2],gunliste[3])
        c.drawString(10, 800 - (15 * (bb + 1)), str(str(gunliste[5])+" "+gunliste[4]))
        c.drawString(110, 800 - (15 * (bb + 1)), str(gunliste[0]))
        c.drawString(165, 800 - (15 * (bb + 1)), str(gunliste[1]))
        c.drawString(220, 800 - (15 * (bb + 1)), str(gunliste[2]))
        c.drawString(275, 800 - (15 * (bb + 1)), str(gunliste[3]))
        bb = bb + 1

        if (str(gunliste[3])).isalpha():
            pass
        else:
            toplam=toplam+int(gunliste[3])

        if (15 * (bb + 1)) >= 760:
            c.setFont("Verdana", 11)
            c.drawString(210, 800 - (15 * (bb + 1)), ".")
            c.drawString(320, 800 - (15 * (bb + 1)), ".")
            c.drawString(550, 800 - (15 * (bb + 1)), ".")

            c.setFont("Courier", 60)
            # This next setting with make the text of our
            # watermark gray, nice touch for a watermark.
            c.setFillGray(0.3, 0.3)
            # Set up our watermark document. Our watermark
            # will be rotated 45 degrees from the direction
            # of our underlying document.
            c.saveState()
            c.translate(500, 100)
            c.rotate(45)
            c.drawCentredString(0, 0, "BISHOP NEN ©")
            c.drawCentredString(0, 300, "BISHOP NEN ©")
            c.drawCentredString(0, 600, "BISHOP NEN ©")
            c.restoreState()
            c.setFillGray(1,1)
            c.showPage()
            c.setFont("Verdana", 8)
            bb = 0


    c.setFont("Verdana", 11)
    c.drawString(160, 800 - (15 * (bb + 1)), "Toplam ")
    c.drawString(275, 800 - (15 * (bb + 1)), str(toplam)+" dk")
    c.drawString(370, 800 - (15 * (bb + 1)), cevirgunsaat(toplam))
    curmy.execute('select maas from personel where kod='+str(gunliste[5])+' ')
    mas =curmy.fetchone()
    print(int(mas[0]/(30*9*60)*toplam))
    c.drawString(520, 800 - (15 * (bb + 1)), str(int(mas[0]/(30*9*60)*toplam))+" TL")

    c.setFont("Courier", 60)
    # This next setting with make the text of our
    # watermark gray, nice touch for a watermark.
    c.setFillGray(0.3, 0.3)
    # Set up our watermark document. Our watermark
    # will be rotated 45 degrees from the direction
    # of our underlying document.
    c.saveState()
    c.translate(500, 100)
    c.rotate(45)
    c.drawCentredString(0, 0, "BISHOP NEN ©")
    c.drawCentredString(0, 300, "BISHOP NEN ©")
    c.drawCentredString(0, 600, "BISHOP NEN ©")
    c.restoreState()
    c.setFillGray(1, 1)
    c.showPage()
    c.setFont("Verdana", 8)
    bb = 0
    toplam=0

c.save()









