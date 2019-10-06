
from modulemdb import Myddb,fbdd

from datetime import datetime,timedelta

fireb=fbdd()
myddb=Myddb()

class masa():
    def __init__(self):
        dt2 = datetime.now() - timedelta(hours=5)
        t = dt2.timetuple()
        self.tt1 = str(t[2]) + "." + str(t[1]) + "." + str(t[0])
        self.tt2 = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2])

    def masagetir(self,masano):

        selectt="SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05,kisi_sayisi,departman,grup3,islem_kod,saat,tarih FROM DATA WHERE  plu_no<1000 and masa_no='"+masano+"'"
        # print selectt1
        ab = 0
        aa = fireb.cur.execute(selectt)
        for row in aa:
            print (row)
            if row[2] < 0:
                continue

            myddb.cur.execute(
                "insert into ciro  (pluno,urun,adet,tutar,masano,tahkod,acik,tarih,kisi,departman,kategori,islem,saat) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (row[0], row[1], row[2], row[3], row[4], row[5], "0", row[11], row[6], row[7], row[8], row[9],row[10]))

            ab = ab + row[3]

        print("toplam       :", self.tt1, ab)
        myddb.cur.execute("insert into test.kasa (posid,aciklama,tutar,belgeno,muhkod,tarih,kasano,islemid) values (%s,%s,%s,%s,%s,%s,%s,%s)",
            (2000,"Tahsilat", ab, row[4], row[5],row[11], 99,row[9]))
        myddb.conn.commit()
mas=masa()
mas.masagetir('KULE 1')
