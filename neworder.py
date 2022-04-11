import pprint

import fdb
from escpos.printer import Network, Dummy
import time

sql1 = "SELECT first 10 plu_no,urun_adi,adet,tutar,masa_no,n_05,kisi_sayisi,tarih,departman,grup3,birim_fiyati,satis_kod,yazici_grubu FROM DATA WHERE yazici_grubu=2100  and plu_no<1000 and urun_turu > 0  order by satis_kod desc "
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
    if kontrol1>kontrol:
        pprint.pprint(bb)

    kontrol=kontrol1
    cur.close()
    con.close()
