# -*- coding:utf8 -*-
import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
from socket import *
import sys
reload(sys)
import atexit

from pushetta import Pushetta
sys.setdefaultencoding('utf8')
API_KEY = "58fee02c2e20ed7511b179af994fc34850f84656"
CHANNEL_NAME = "admin-nen"
p = Pushetta(API_KEY)
appnot="masa1 kapandı"

interval_num=0
tgtIP = gethostbyname('nen.duckdns.org')
print tgtIP
conmy = mdb.connect(tgtIP, 'nen','654152', 'bishop',charset='utf8',port=30000)
curmy = conmy.cursor()
con = fdb.connect(
    dsn='nen.duckdns.org/30500:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',

    charset='UTF8' # specify a character set for the connection #
     )
cur=con.cursor()

@atexit.register
def cikis():
    p.pushMessage(CHANNEL_NAME, appnot)


def yenile():


    print " "

    selectt1="SELECT plu_no,urun_adi,adet,tutar,masa_no,tah_kod,kisi_sayisi,departman, islem_kod FROM YEDEK_RAPOR WHERE TARIH='"+tt1+"' and plu_no<1000 and urun_turu > 0 "
    #print selectt1
    ab=0
    aa=cur.execute(selectt1 )
    for row in aa:
        if row[2]<0:
            continue

        curmy.execute("insert into ciro  (pluno,urun,adet,tutar,masano,tahkod,acik,tarih,kisi,departman,islem) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],"0",tt2,row[6],row[7],row[8]))


        ab=ab+row[3]

    print "toplam       :",tt1,ab
    conmy.commit()



while True:
    dt=datetime.now()-timedelta(hours=5)
    interval_type = 'days'
    interval_num = interval_num+1
    if interval_num==2:
        break
    one_day = timedelta(**{interval_type: interval_num})
    dt2=dt-one_day
    t=dt2.timetuple()
    tt1=str(t[2])+"."+str(t[1])+"."+str(t[0])
    tt2=str(t[0])+"-"+str(t[1])+"-"+str(t[2])



    strt="delete from ciro where tarih='"+tt2+"' "
    tt3=tt2
    curmy.execute(strt)
    son=curmy.execute("select max(id) from ciro")
    son1="ALTER TABLE ciro AUTO_INCREMENT ="+str(son)
    yenile()



    conmy.commit()
conmy.close()
