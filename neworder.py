import pprint

import fdb
#from escpos.printer import Network, Dummy
import time

import sys
from PyQt5 import  QtCore, QtWidgets,QtGui
from PyQt5.QtCore import *


class Login(QtWidgets.QDialog):
    acac1 = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle(u"NENRA 2022  Sipariş Bilgisi ")
        self.labelname = QtWidgets.QLabel(self)
        self.labelpass = QtWidgets.QLabel(self)

        self.labelname.setFont(QtGui.QFont("Arial",24))
        self.labelpass.setFont(QtGui.QFont("Arial",18))

        self.labelname.setText(u"")
        self.labelpass.setText(u"")

        self.resize(500,500)


        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.labelname)
        layout.addWidget(self.labelpass)

app = QtWidgets.QApplication(sys.argv)

sql1 = "SELECT first 10 plu_no,urun_adi,adet,tutar,masa_no,islem_kod,kisi_sayisi,tarih,departman,grup3,birim_fiyati,satis_kod,yazici_grubu FROM DATA WHERE yazici_grubu=2100  and plu_no<1000 and urun_turu > 0  order by satis_kod desc "
kontrol=1

while True:
    time.sleep(10)

    con = fdb.connect(
        dsn='nen.duckdns.org/30500:D:\RESTOPOS\DATA\DATABASE.GDB',
        user='sysdba', password='masterkey',
        charset='UTF8'  # specify a character set for the connection #
    )
    cur = con.cursor()

    cur.execute(sql1)
    bb = cur.fetchall()
    print(bb[0][11])
    kontrol1=int(bb[0][11])
    not1 = Login()

    masano=1369
    urun=""
    if kontrol1>kontrol:
        for bb1 in bb:
            if masano!=bb1[4]:
                masano=bb1[4]
                print(" ")
                print(masano)
            print(bb1[1],bb1[2],bb1[5])
            not1.labelname.setText(masano)
            urun=urun+(str(int(bb1[2]))+" ad "+str(bb1[1])+"  "+str(bb1[5])+"\n" )
        not1.labelpass.setText(urun)
        not1.show()
        time.sleep(5)
        not1.hide()


    kontrol=kontrol1
    cur.close()
    con.close()
    not1.close()
