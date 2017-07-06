# -*- coding:utf8 -*-

import fdb
import MySQLdb
import pymssql
from socket import *
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('tahoma', 'tahoma.ttf'))


class Mmdb():
    def __init__(self):
        tgtIP = gethostbyname('nen.duckdns.org')
        self.conn = MySQLdb.connect(tgtIP, 'nen', '654152', 'test', charset='utf8', port=30000);

        # create a cursor
        self.cur = self.conn.cursor()
        self.cur.execute("SET NAMES UTF8")
        self.cur.execute("SET character_set_client=utf8")


    def cek(self,tablename):
        # extract all the data
       # sql = "select Stok_Kodu , Adi_1,Ozel_Kodu3 from %s where Ozel_Kodu1='HAMMADDE' AND Ozel_Kodu2='BAR' AND Ozel_Kodu15!='PASIF' order by Ozel_Kodu3 " % tablename
        sql="select hamkod , hamad , bolum from %s where departman='BAR' AND HAMKOD<9000 order by bolum " % tablename
        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()
        return self.result

Mmdb1=Mmdb()
sonuc= Mmdb1.cek("hammadde")
print sonuc[0][0], sonuc[0][1]
def createBarCodes():
    """
    Create barcode examples and embed in a PDF
    """
    c = canvas.Canvas("STOKBARHAZIRAN2017.pdf", pagesize=A4)
    c.setFont("tahoma", 12)





    # code93 also has an Extended and MultiWidth version






    x = 1 * mm
    y = 270* mm
    x1 = 6.4 * mm

    c.drawImage("./images/bishop.png",x+5,y-15)

    b=sonuc[0][2]
    c.setFont("tahoma", 30)
    c.drawString(x+90,y-15,str(b))
    c.setFont("tahoma", 21)
    c.drawString(x + 190, y + 35, "SAYIM BAR 30/06/2017")
    c.setFont("tahoma", 12)
    y = y - 20 * mm
    orhan=0
    sayfa=1

    for code in sonuc:
        if b!=code[2]:
            if orhan!=0:
                c.drawString(x + 190, 20 , "SAYIM BAR 30/06/2017     SAYFA  "+str(sayfa))
                sayfa=sayfa+1
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

                c.showPage()
                y = 280* mm
            y = y - 20 * mm
            c.setFont("tahoma", 30)
            c.drawString(x+90,y+35,str(code[2]))
            c.setFont("tahoma", 12)

        b=code[2]
        orhan=orhan+1
        print code[0],code[1],orhan
        barcode93 = code93.Standard93(code[0])
        barcode93.drawOn(c, x, y+10)
        c.drawString(x+90,y+15,str(code[0])+" "+ code[1])
        c.rect(x,y+3,200*mm,10*mm, fill=0)
        y = y - 10 * mm
        if y<20 :
            c.drawString(x + 190, 20, "SAYIM BAR 30/06/2017     SAYFA  " + str(sayfa))
            sayfa = sayfa + 1

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

            c.showPage()
            y = 280* mm



    # draw a QR code
    qr_code = qr.QrCodeWidget('http://nen.duckdns.org/siparis/www')
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
    d.add(qr_code)
    renderPDF.draw(d, c, 15, 50)

    c.drawString(x + 190, 20, "SAYIM BAR 30/06/2017     SAYFA  " + str(sayfa))

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

    c.save()
createBarCodes()

