import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
from socket import *




def yenile():
    selectt = "SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05,kasa,ISLEM_KOD  FROM YEDEK_RAPOR  where  (plu_no>899 and plu_no<909 or plu_no=2000) and tarih='" + tt1 + "' and urun_turu>0 and urun_turu<50"

    selectt1="SELECT plu_no,urun_adi,adet,tutar,masa_no,tah_kod,kisi_sayisi,saat,departman FROM YEDEK_RAPOR WHERE TARIH='"+tt1+"' and plu_no<1000 and urun_turu > 0 "
    print selectt
    ab=0
    aa=cur.execute(selectt )


    print "KAPALI MASALAR"
    print " "
    for row in aa:
        tut = row[3]
        kno = 100

        if row[3] < 0:
            kno = 111

        if row[0] != 2000:
            kno = 101

        if (row[1] == "* Trst") or (row[1] == "* Tip"):
            kno = 102
        if row[6] == "DENIZ BANK":
            kno = 105
        elif row[6] == "YAPI KREDI":
            kno = 106

        print '%s masasinda %s TL  %s urun ' % (row[4], row[1],row[2])
        curmy.execute(
            "insert ignore into kasa  (posid,aciklama,tutar,belgeno,muhkod,tarih,kasano,islemid) values (%s,%s,%s,%s,%s,%s,%s,%s)",
            (row[0], row[1], tut, row[4], row[5], tt2, kno, row[7]))

        ab=ab+tut

    print "toplam       :",ab
    conmy.commit()




    print "--------------------------------------------------------------------------------- "
    """   ab=0
    aa=cur.execute(slectaylik )
    print "AYLIK DAGILIM "
    print " "
    for row in aa:
        print '%s -- %s  TL --  %s ADET ' % (row[0], row[2],row[1])
        ab=ab+row[2]

    print "toplam       :",ab """


while True:
    try:
        dt=datetime.now()-timedelta(hours=5)
        t=dt.timetuple()
        tt1=str(t[2])+"."+str(t[1])+"."+str(t[0])
        tt2=str(t[0])+"-"+str(t[1])+"-"+str(t[2])
        tgtIP = gethostbyname('nen.duckdns.org')
        print tgtIP
        conmy = mdb.connect(tgtIP, 'nen','654152', 'test',charset='utf8',port=30000)
        curmy = conmy.cursor()
        con = fdb.connect(
            dsn='192.168.2.251:D:\RESTO_2015\DATA\DATABASE.GDB',
            user='sysdba', password='masterkey',
            charset='UTF8' # specify a character set for the connection #
        )
        cur=con.cursor()
        yenile()
        ttim.sleep(60)
        conmy.commit()
        strt="delete from kasa where tarih='"+tt2+"' "
        tt3=tt2
        curmy.execute(strt)
        son=curmy.execute("select max(kasaid) from kasa")
        son1="ALTER TABLE kasa AUTO_INCREMENT ="+str(son)
        curmy.execute(son1)
        conmy.commit()
        conmy.close()
    except:
        ttim.sleep(60)
        pass

