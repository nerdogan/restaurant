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
server1=nenraconfig._GetOption3('server')
user1=nenraconfig._GetOption3('user')
password1=nenraconfig._GetOption3('password')
port1=nenraconfig._GetOption3('port')

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

conn = mdb.connect(server1, user1, password1, 'test', charset='utf8',port=int(port1))
curr = conn.cursor()


selectt = "SELECT plu_no,urun_adi,miktar_turu,kdv,F,grup3  FROM urunler  where  (plu_no>0 and plu_no<1000 ) and urun_turu>0 and urun_turu<50"

selectt1 = "INSERT INTO `hammadde` (`hamkod`, `hamad`, `birim`, `kdv`, `kategori`, `fiyat1`, `departman`, `bolum`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
print(selectt)
ab = 0
aa = cur.execute(selectt)

for row in aa:
    print(row)
    try:
        curr.execute(selectt1,(row[0],row[1],row[2],row[3],3,row[4],1,row[5]))
        conn.commit()
    except (mdb.Error, mdb.Warning) as e:
        print(e)
        print ("girilemedi")
        pass
con.close()
conn.close()