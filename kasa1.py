# -*- coding:utf8 -*-
import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
from socket import *
import sys
reload(sys)
import atexit


sys.setdefaultencoding('utf8')

appnot="kasa1 kapandı"

interval_num=0
tgtIP = gethostbyname('nen.duckdns.org')
print tgtIP
conmy = mdb.connect(tgtIP, 'nen','654152', 'test',charset='utf8',port=30000)
curmy = conmy.cursor()
con = fdb.connect(
    dsn='nen.duckdns.org/30500:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',

    charset='UTF8' # specify a character set for the connection #
     )
cur=con.cursor()

@atexit.register
def cikis():
    pass


def yenile():


    print " "

    selectt1="SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05,kasa,ISLEM_KOD  FROM YEDEK_RAPOR  where  (plu_no>899 and plu_no<909 or plu_no=2000) and tarih='" + tt1 + "' and urun_turu>0 and urun_turu<50"
 #print selectt1
    ab=0
    aa=cur.execute(selectt1 )
    for row in aa:
        tut=row[3]
        kno=100

        if row[3] < 0:
            kno = 111


        if row[0] != 2000:
            kno = 101

        if (row[1]=="* Trst") or (row[1]=="* Tip"):
            kno=102
        if row[6]=="DENIZ BANK":
            kno=105
        elif row[6]=="YAPI KREDI":
            kno=106


        curmy.execute("insert ignore into kasa  (posid,aciklama,tutar,belgeno,muhkod,tarih,kasano,islemid) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                      (row[0], row[1], tut, row[4], row[5], tt2,kno,row[7]))

        ab=ab+tut

    print "toplam       :",tt1,ab
    conmy.commit()



while True:
    dt=datetime.now()-timedelta(hours=5)
    interval_type = 'days'

    if interval_num==1:
        break
    one_day = timedelta(**{interval_type: interval_num})
    dt2=dt-one_day
    t=dt2.timetuple()
    tt1=str(t[2])+"."+str(t[1])+"."+str(t[0])
    tt2=str(t[0])+"-"+str(t[1])+"-"+str(t[2])



    tt3=tt2

    yenile()
    interval_num = interval_num + 1




conmy.close()
