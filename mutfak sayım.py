import fdb
import MySQLdb as mdb
import pymssql
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

class Mmdb():
    def __init__(self):


        # connect to the database
        self.conn = pymssql.connect("WINSERVER","sa","QaZ147WsX","MYSYS_2015")
        # create a cursor
        self.cur = self.conn.cursor()
    def cek(self,tablename):
        # extract all the data
        sql = "select Stok_Kodu , Adi_1,Ozel_Kodu3 from %s where Ozel_Kodu1='HAMMADDE' AND Ozel_Kodu2='MUTFAK' AND Ozel_Kodu15!='PASIF' order by Adi_1 " % tablename
        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()
        return self.result

Mmdb1=Mmdb()
sonuc= Mmdb1.cek("STOK_Karti")
print sonuc[0][0], sonuc[0][1]
def createBarCodes():
    """
    Create barcode examples and embed in a PDF
    """
    c = canvas.Canvas("STOKMUTFAK.pdf", pagesize=A4)
    c.setFont("Helvetica", 12)





    # code93 also has an Extended and MultiWidth version






    x = 1 * mm
    y = 270* mm
    x1 = 6.4 * mm

    c.drawImage("./images/bishop.png",x+5,y-15)

    b=sonuc[0][2]
    c.setFont("Helvetica", 30)
    c.drawString(x+90,y-15,str(b))
    c.setFont("Helvetica", 21)
    c.drawString(x+190,y+35,"SAYIM MUTFAK 29/02/2016")
    c.setFont("Helvetica", 12)
    y = y - 20 * mm

    for code in sonuc:
        b=code[2]
        print code[0],code[1]
        barcode93 = code93.Standard93(code[0])
        barcode93.drawOn(c, x, y+10)
        c.drawString(x+90,y+15,str(code[0]+" "+ code[1]))
        c.rect(x,y+3,200*mm,10*mm, fill=0)
        y = y - 10 * mm
        if y<20 :
            c.showPage()
            y = 280* mm



    # draw a QR code
    qr_code = qr.QrCodeWidget('http://78.188.173.248/masa.php')
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
    d.add(qr_code)
    renderPDF.draw(d, c, 15, 50)

    c.save()
createBarCodes()

