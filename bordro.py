__author__ = 'NAMIK'

import MySQLdb as mdb
from socket import *
from datetime import time,timedelta

tgtIP = gethostbyname('nen.duckdns.org')
print(tgtIP)
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8',port=30000)
curmy = conmy.cursor()
curmy.execute("SET NAMES UTF8")
curmy.execute("SET character_set_client=utf8")

bul =curmy.execute("select adsoyad,tarih,saat from personelgc where tarih between '2019-12-01' and '2020-01-01' and enrolgc=5 order by adsoyad,tarih,saat")
bul=curmy.fetchall()
a=0
for b in (bul):
    if (b[2])>timedelta(hours=7):
        tar=b[1]
        sat=b[2]
        a=1
        continue

    else:
        if (a==1):
            print (tar,b[1])
            print (b[2]-sat+timedelta(hours=24))
            a=0

