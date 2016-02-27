import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim


conmy = mdb.connect("192.168.2.211", "nen","654152", "bishop",charset='utf8')
curmy = conmy.cursor()



con = fdb.connect(
    dsn='192.168.2.211:C:\DigiAccess\DigiAccess300\Data\DATABASE.GDB',
    user='sysdba', password='masterkey',
charset='WIN1254'
  )
cur=con.cursor()
selectt="SELECT PS,AD,SOYAD FROM KIMLIK "


def yenile():

    ab="0"
    aa=cur.execute(selectt)

    print "ACIK MASALAR"
    print " "
    for row in aa:

        curmy.execute("insert into personel (kod,ad,soyad,adsoyad) values (%s,%s,%s,%s)",(row[0],row[1],row[2],(row[1]+" "+row[2])))
        print row[0],row[1],row[2]

    print " "
    conmy.commit()


    print " "
    """   ab=0
    aa=cur.execute(slectaylik )
    print "AYLIK DAGILIM "
    print " "
    for row in aa:
        print '%s -- %s  TL --  %s ADET ' % (row[0], row[2],row[1])
        ab=ab+row[2]

    print "toplam       :",ab """


yenile()
conmy.commit()
