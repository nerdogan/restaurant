# -*- coding:utf8 -*-
import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
from socket import *
import sys
reload(sys)
import atexit
import subprocess
from modulemdb import Myddb


sys.setdefaultencoding('utf8')

appnot="masa1 kapandı"

interval_num=0
myddb=Myddb()

con = fdb.connect(
    dsn='nen.duckdns.org/30500:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',

    charset='UTF8'
     )
cur=con.cursor()

@atexit.register
def cikis():
    pass
#    p.pushMessage(CHANNEL_NAME, appnot,expire="2017-04-19")


def yenile():


    print " "

    selectt1="SELECT plu_no,urun_adi,adet,tutar,masa_no,tah_kod,kisi_sayisi,departman, islem_kod,saat,grup3 FROM YEDEK_RAPOR WHERE TARIH='"+tt1+"' and plu_no<1000 and urun_turu > 0 "
    #print selectt1
    ab=0
    aa=cur.execute(selectt1 )
    for row in aa:
        if row[2]<0:
            continue

        myddb.cur.execute("insert into bishop.ciro  (pluno,urun,adet,tutar,masano,tahkod,acik,tarih,kisi,departman,islem,saat,kategori) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],"0",tt2,row[6],row[7],row[8],row[9],row[10]))


        ab=ab+row[3]

    print "toplam       :",tt1,ab
    myddb.conn.commit()



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



    strt="delete from bishop.ciro where tarih='"+tt2+"' "
    tt3=tt2
    myddb.cur.execute(strt)
    son=myddb.cur.execute("select max(id) from bishop.ciro")
    son1="ALTER TABLE bishop.ciro AUTO_INCREMENT ="+str(son)
    yenile()



    myddb.conn.commit()
myddb.conn.close()
subprocess.Popen("C:\\xampp\\mysql\\bin\\mysqldump.exe -h 192.168.2.251 -u nen --password=654152  bishop > C:\\Users\\NAMIK\\PycharmProjects\\restaurant\\belge\\bishop"+tt1+".sql ",shell=True)
subprocess.Popen("C:\\xampp\\mysql\\bin\\mysqldump.exe -h 192.168.2.251 -u nen --password=654152  test > C:\\Users\\NAMIK\\PycharmProjects\\restaurant\\belge\\test"+tt1+".sql ",shell=True)
subprocess.Popen("C:\\xampp\\mysql\\bin\\mysqldump.exe -h 192.168.2.251 -u nen --password=654152  bishop | C:\wamp\\bin\\mysql\\mysql5.7.14\\bin\\mysql -u root  -h localhost bishop ",shell=True)
subprocess.Popen("C:\\xampp\\mysql\\bin\\mysqldump.exe -h 192.168.2.251 -u nen --password=654152  test | C:\wamp\\bin\\mysql\\mysql5.7.14\\bin\\mysql -u root   -h localhost test ",shell=True)
