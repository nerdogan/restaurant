import fdb
import MySQLdb as mdb
from datetime import datetime, timedelta
import time as ttim
from socket import *
import subprocess
import nenraconfig

server=nenraconfig._GetOption1('server')
user=nenraconfig._GetOption1('user')
password=nenraconfig._GetOption1('password')

dt = datetime.now() - timedelta(hours=24)
t = dt.timetuple()
tt1 = str(t[2]) + "." + str(t[1]) + "." + str(t[0])
tt2 = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2])
print (tt1)
con = fdb.connect(
    dsn=server,user=user, password=password,
    charset='UTF8'  # specify a character set for the connection #
)
cur = con.cursor()

selectt = "SELECT plu_no,urun_adi,miktar_turu,kdv,F,grup3  FROM urunler  where  (plu_no>0 and plu_no<1000 ) and urun_turu>0 and urun_turu<50"

selectt1 = "SELECT plu_no,urun_adi,adet,tutar,masa_no,tah_kod,kisi_sayisi,saat,departman FROM YEDEK_RAPOR WHERE TARIH='" + tt1 + "' and plu_no<1000 and urun_turu > 0 "
print(selectt)
ab = 0
aa = cur.execute(selectt)

for row in aa:
    print(row)

con.close()