# -*- coding: cp1254 -*-
import pymssql
import sys
from PyQt4 import QtCore, QtGui
from mainwindow import MainWindow

app = QtGui.QApplication(sys.argv)
app.processEvents()

class Mmdb():
    def __init__(self):


        # connect to the database
        self.conn = pymssql.connect("WINSERVER","sa","QaZ147WsX","MYSYS_2015")
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


def OK(self):
    print 'OK pressed.'
    belgeno=str(mainWindow.lineEdit.text())
    sql="    select a.Fis_No,a.Fis_Tarihi,b.Unvani from STOK_Fis_Baslik  a   inner join CARI_Karti b on a.Cari_No=b.Cari_No and Belge_No='"+belgeno+"'"
    print sql

    sql1 = """SELECT TOP 1000
[Kdv_Orani],
sum([GTutari] ),
     sum([KdvTutari])

  FROM [MYSYS_2015].[dbo].[STOK_Fis_Kalem] WHERE Fis_No=45 AND Fis_Tipi=50 GROUP BY [Kdv_Orani] """
    sonuc= Mmdb1.cek(sql)
    aa=(sonuc[0][2]).encode('utf-16')[2:]
    print sonuc[0][0], sonuc[0][1],aa
    dosya=open(r"C:\Users\NAMIK\Google Drive\bishop\deneme1.csv","w")
    dosya.writelines("EvrakTarihi;EvrakNo;Açıklama;GenelToplam;Matrah;KDV\n")
    dosya.write((sonuc[0][2]).encode('utf16'))
    dosya.writelines("21.09.2015;7777;PROFESYONEL GIDA;883,17;817,75;65,42")
    mainWindow.lineEdit_2.setText(str(sonuc[0][0])+"   "+str(sonuc[0][1])+"   "+aa)




mainWindow.pushButton.clicked.connect(OK)
sys.exit(app.exec_())



