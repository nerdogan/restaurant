import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
from socket import *

interval_num=0
tgtIP = gethostbyname('bishop')
print tgtIP
conmy = mdb.connect(tgtIP, 'nen','654152', 'bishop',charset='utf8')
curmy = conmy.cursor()
con = fdb.connect(
    dsn='192.168.2.250:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',

    charset='UTF8' # specify a character set for the connection #
     )
cur=con.cursor()

def yenile():


    print " "

    selectt1="SELECT plu_no,urun_adi,adet,tutar,masa_no,tah_kod,kisi_sayisi FROM YEDEK_RAPOR WHERE TARIH='"+tt1+"' and plu_no<1000 and urun_turu > 0 "
    print selectt1
    ab=0
    aa=cur.execute(selectt1 )
    for row in aa:
        if row[2]<0:
            continue

        curmy.execute("insert into ciro  (pluno,urun,adet,tutar,masano,tahkod,acik,tarih,kisi) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],"0",tt2,row[6]))


        ab=ab+row[3]

    print "toplam       :",ab
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
