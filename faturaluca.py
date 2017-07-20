# -*- coding: cp1254 -*-
__author__ = 'NAMIK'
import pymssql
import sys
from PyQt4 import QtCore, QtGui
from mainwindow import MainWindow

app = QtGui.QApplication(sys.argv)
app.processEvents()
class Mmdb():
    def __init__(self):


        # connect to the database
        self.conn = pymssql.connect("SERVERPC","sa","QaZ123WsX","RESTO_2016")
        # create a cursor
        self.cur = self.conn.cursor()
    def cek(self,sql):
        # extract all the data
        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()
        return self.result

Mmdb1=Mmdb()

mainWindow = MainWindow()

mainWindow.show()
dosya=open(r"C:\Users\NAMIK\Google Drive\bishop\faturaluca.csv","w")
dosya.writelines("EvrakTarihi;EvrakNo;Açıklama;GenelToplam;Matrah;KDV\n")


def kontrol(girdi):
    return str(girdi).replace("." , ",")


def OK(self):
    print 'OK pressed.'
    belgeno=str(mainWindow.lineEdit.text())
    sql="    select a.Fis_No,a.Fis_Tarihi,b.Unvani from STOK_Fis_Baslik  a   inner join CARI_Karti b on a.Cari_No=b.Cari_No and Belge_No='"+belgeno+"'"
    sonuc= Mmdb1.cek(sql)
    sql1 ="SELECT sum([GTutari] ), sum([KdvTutari])  FROM [RESTO_2016].[dbo].[STOK_Fis_Kalem] WHERE Fis_No="+str(sonuc[0][0])+" AND Fis_Tipi=50 GROUP BY [Kdv_Orani]"
    sonuc1= Mmdb1.cek(sql1)

    aa=(sonuc[0][2]).encode('utf-16')[2:]
    xc=-1
    bb=""
    while True:
        xc=xc+1

        if xc%2==0:
            bb=bb+aa[xc]

        if xc==len(aa)-2:
            break
    cc=(sonuc[0][1]).strftime("%d.%m.%Y")

    print sonuc[0][0], cc,bb

    for row in sonuc1:

        dosya.write(cc)
        dosya.write(";")
        dosya.write(belgeno)
        dosya.write(";")
        dosya.write(bb)
        dosya.write(";")
        dosya.write(kontrol('{:0.2f}'.format(row[0]+row[1])))
        dosya.write(";")
        dosya.write(kontrol('{:0.2f}'.format(row[0])))


        dosya.write(";")
        dosya.writelines(kontrol('{:0.2f}'.format(row[1])))

        dosya.write("\n")


    print mainWindow.lineEdit.text()
    mainWindow.lineEdit_2.setText(str(sonuc[0][0])+"   "+cc+"   "+bb)
    mainWindow.lineEdit.selectAll()





mainWindow.pushButton.clicked.connect(OK)
sys.exit(app.exec_())
