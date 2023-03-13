import fdb
from escpos.printer import Network, Dummy
import time

sql1 = "SELECT first 1 plu_no,urun_adi,adet,tutar,masa_no,n_05,kisi_sayisi,tarih,departman,grup3,birim_fiyati,satis_kod,yazici_grubu FROM DATA WHERE yazici_grubu=2100  and yazici_grubu=1100  and plu_no<1000 and urun_turu > 0  order by satis_kod desc "
kontrol=1

while True:
    time.sleep(10)
    try:

        con = fdb.connect(
            dsn='192.168.2.251/3050:D:\RESTOPOS\DATA\DATABASE.GDB',
            user='sysdba', password='masterkey',
            charset='UTF8'  # specify a character set for the connection #
        )
        cur = con.cursor()

        cur.execute(sql1)
        bb = cur.fetchone()
        print(bb[11],bb)
        kontrol1=int(bb[11])
        if kontrol1>kontrol:
            d = Dummy()
            d.text(chr(27))
            d.text(chr(116))
            d.text(chr(61))

            d.set(font='a', align='left', height=1, width=1)
            d.text(chr(27))
            d.text("B")
            d.text(chr(4))
            d.text(chr(6))

            p = Network("192.168.2.221")
            p._raw(d.output)


            p = None
        kontrol=kontrol1
        cur.close()
        con.close()
    except:
        print("bağlanamadı")

