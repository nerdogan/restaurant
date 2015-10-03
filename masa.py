import fdb
import MySQLdb as mdb
import time


conmy = mdb.connect("127.0.0.1", "root","", "bishop",charset='utf8')
curmy = conmy.cursor()


con = fdb.connect(
    dsn='192.168.2.251:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',
   
    charset='UTF8' # specify a character set for the connection
  )
cur=con.cursor()
selectt="SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05 FROM DATA WHERE  plu_no<1000"

selectt1="SELECT plu_no,urun_adi,adet,tutar,masa_no,tah_kod FROM YEDEK_RAPOR WHERE TARIH='03.10.2015' and plu_no<1000  "

slectaylik="""select
  c.d_adi,
  sum(a.adet) as Adet,
  Sum(a.tutar) as Tutar
from YEDEK_RAPOR a, urunler b , departman c
where (a.URUN_TURU between 0 and 2)
      and (a.tarih between '01.09.2015' and '30.09.2015')
      and a.PLU_NO=b.PLU_NO and b.fire=c.D_KODU
group by c.d_adi
order by c.d_adi

"""

def yenile():
    curmy.execute("DROP TABLE IF EXISTS `ciro`")
    strt="CREATE TABLE `ciro` (`id` int(11) unsigned NOT NULL AUTO_INCREMENT,  `masano` varchar(50) COLLATE utf8_turkish_ci DEFAULT NULL,  `pluno` int(10) unsigned NOT NULL,  `urun` varchar(50) COLLATE utf8_turkish_ci DEFAULT NULL,  `adet` int(10)  NOT NULL,  `tutar` float DEFAULT NULL,  `tarih` date ,  `acik` tinyint(3) unsigned DEFAULT NULL,  `tahkod`  varchar(50) COLLATE utf8_turkish_ci DEFAULT NULL,  UNIQUE KEY `id` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci AUTO_INCREMENT=1"
    curmy.execute(strt)

    ab=0
    aa=cur.execute(selectt)
    print "ACIK MASALAR"
    print " "
    for row in aa:
        if row[2]<0:
            continue
        print '%s masasinda %s TL  %s urun ' % (row[4], row[1],row[2])
        curmy.execute("insert into ciro  (pluno,urun,adet,tutar,masano,tahkod,acik) values (%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],"1"))

        ab=ab+row[3]

    print "toplam       :",ab

    print " "
    print " "
    ab=0
    aa=cur.execute(selectt1 )

    print "KAPALI MASALAR"
    print " "
    for row in aa:
        if row[2]<0:
            continue
        print '%s masasinda %s TL  %s urun ' % (row[4], row[1],row[2])
        curmy.execute("insert into ciro  (pluno,urun,adet,tutar,masano,tahkod,acik) values (%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],"0"))

        ab=ab+row[3]

    print "toplam       :",ab
    conmy.commit()




    print " "
    ab=0
    aa=cur.execute(slectaylik )
    print "AYLIK DAGILIM "
    print " "
    for row in aa:
        print '%s -- %s  TL --  %s ADET ' % (row[0], row[2],row[1])
        ab=ab+row[2]

    print "toplam       :",ab


while True:
    yenile()
    time.sleep(5)
