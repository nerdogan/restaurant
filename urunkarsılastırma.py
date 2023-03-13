# -*- coding:utf8 -*-
import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
from socket import *
import sys
import atexit


interval_num=1
tgtIP = gethostbyname('nen.duckdns.org')
print (tgtIP)
conmy = mdb.connect(tgtIP, 'nen','654152', 'test',charset='utf8',port=30000)
curmy = conmy.cursor()
con = fdb.connect(
    dsn='nen.duckdns.org/30500:D:\RESTOPOS\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',

    charset='UTF8' # specify a character set for the connection #
     )
cur=con.cursor()

@atexit.register
def cikis():
    pass


def yenile():


    print (" ")

    selectt1="SELECT plu_no,urun_adi,kdv,fire,f,grup3  FROM urunler  where  plu_no='" + str(interval_num) + "' "
 #print selectt1
    ab=0
    aa=cur.execute(selectt1 )
    if not son:
        ab=1
        print("elma")
    for row in aa:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

        cevap = "e"
            #input("Değiştirilsin mi ?")
        if cevap == "e":
            print("")
            sonuc=curmy.execute("""update hammadde set hamad=%s,kdv=%s, departman=%s,fiyat1=%s,bolum=%s where hamkod=%s """,
                          (str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), (row[0])))

            if ab==1:
                sonuc = curmy.execute(
                    """insert into hammadde (hamkod,hamad,kdv, departman,fiyat1,bolum) values(%s,%s,%s,%s,%s,%s) """,
                    (str(row[0]),str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))

            print(sonuc)
            print("değişti")
        else:
            print("devammm")

    conmy.commit()



while True:

    if interval_num==947:
        break

    son = curmy.execute("select * from hammadde where hamkod='"+str(interval_num)+"' ")
    son=curmy.fetchall()
    for row in son:
        print (row[1],row[2],row[4],row[7],row[6],row[8])


    yenile()

    conmy.commit()

    interval_num = interval_num + 1
    print (" ")




conmy.close()
