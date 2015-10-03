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
        sql = "select Stok_Kodu , Adi_1,Ozel_Kodu3 from %s where Ozel_Kodu1='HAMMADDE' AND Ozel_Kodu2='BAR' AND Ozel_Kodu15!='PASIF' order by Ozel_Kodu3 " % tablename
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
    c = canvas.Canvas("STOK.pdf", pagesize=A4)
    c.setFont("Helvetica", 12)




    # code93 also has an Extended and MultiWidth version






    x = 1 * mm
    y = 270* mm
    x1 = 6.4 * mm
    b=sonuc[0][2]
    c.setFont("Helvetica", 30)
    c.drawString(x+90,y+35,str(b))
    c.setFont("Helvetica", 14)
    c.drawString(x+390,y+35,"SAYIM BAR 30/09/2015")
    c.setFont("Helvetica", 12)

    for code in sonuc:
        if b!=code[2]:
            y = y - 20 * mm
            c.setFont("Helvetica", 30)
            c.drawString(x+90,y+35,str(code[2]))
            c.setFont("Helvetica", 12)

        b=code[2]
        barcode93 = code93.Standard93(code[0])
        barcode93.drawOn(c, x, y+10)
        c.drawString(x+90,y+15,str(code[0]+" "+ code[1]))
        c.rect(x,y+3,200*mm,10*mm, fill=0)
        y = y - 10 * mm
        if y<20 :
            c.showPage()
            y = 280* mm



    # draw a QR code
    qr_code = qr.QrCodeWidget('http://192.168.2.55/masa.php')
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
    d.add(qr_code)
    renderPDF.draw(d, c, 15, 50)

    c.save()
createBarCodes()

conmy = mdb.connect("127.0.0.1", "root","", "bishop",charset='utf8')
curmy = conmy.cursor()
curmy.execute("DROP TABLE IF EXISTS `ciro`")
strt="CREATE TABLE `ciro` (`id` int(11) unsigned NOT NULL AUTO_INCREMENT,  `masano` varchar(50) COLLATE utf8_turkish_ci DEFAULT NULL,  `pluno` int(10) unsigned NOT NULL,  `urun` varchar(50) COLLATE utf8_turkish_ci DEFAULT NULL,  `adet` int(10)  NOT NULL,  `tutar` float DEFAULT NULL,  `tarih` date ,  `acik` tinyint(3) unsigned DEFAULT NULL,  `tahkod`  varchar(50) COLLATE utf8_turkish_ci DEFAULT NULL,  UNIQUE KEY `id` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci AUTO_INCREMENT=1"

curmy.execute(strt)

con = fdb.connect(
    dsn='192.168.2.251:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',
   
    charset='UTF8' # specify a character set for the connection
  )
cur=con.cursor()
selectt="SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05 FROM DATA WHERE  plu_no<1000"

selectt1="SELECT plu_no,urun_adi,adet,tutar,masa_no,tah_kod FROM YEDEK_RAPOR WHERE TARIH='01.10.2015' and plu_no<1000  "

slectaylik="""select
  c.d_adi,
  sum(a.adet) as Adet,
  Sum(a.tutar) as Tutar
from YEDEK_RAPOR a, urunler b , departman c
where (a.URUN_TURU between 0 and 2)
      and (a.tarih between '01.08.2015' and '31.08.2015')
      and a.PLU_NO=b.PLU_NO and b.fire=c.D_KODU
group by c.d_adi
order by c.d_adi

"""





ab=0
aa=cur.execute(selectt)
print "ACIK MASALAR"
print " "
for row in aa:
    if row[2]<0:
        continue
    print '%s masasinda %s TL  %s urun ' % (row[4], row[1],row[2])
    curmy.execute("insert into ciro  (pluno,urun,adet,tutar,masano,tahkod,acik) values (%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],"1"))

    ab=ab+row[3]

print "toplam       :",ab
print " "
print " "
ab=0
aa=cur.execute(selectt1 )

print "KAPALI MASALAR"
print " "
for row in aa:
    if row[2]<0:
        continue
    print '%s masasinda %s TL  %s urun ' % (row[4], row[1],row[2])
    curmy.execute("insert into ciro  (pluno,urun,adet,tutar,masano,tahkod,acik) values (%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],"0"))

    ab=ab+row[3]

print "toplam       :",ab
conmy.commit()




print " "
ab=0
aa=cur.execute(slectaylik )
print "AYLIK DAGILIM "
print " "
for row in aa:
    print '%s -- %s  TL --  %s ADET ' % (row[0], row[2],row[1])
    ab=ab+row[2]

print "toplam       :",ab
