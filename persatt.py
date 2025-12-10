# -*- coding:utf8 -*-
from zk import ZK, const
from datetime import datetime
import MySQLdb as mdb
from socket import *
print("----------")
#tgtIP = gethostbyname('nen.duckdns.org')
tgtIP="192.168.2.251"
print(tgtIP)
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8',port=3306)
curmy = conmy.cursor()
curmy.execute("SET NAMES UTF8")
curmy.execute("SET character_set_client=utf8")

zk = ZK('192.168.2.224', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
conn = zk.connect()
# disable device, this method ensures no activity on the device while the process is run
conn.disable_device()
# another commands will be here!
i = 0
attendance = conn.get_attendance()
print(len(attendance))
print("Giriş çıkış listesi:")

if ( attendance ):
    for lattendance in attendance:

        print(" %s, %s , %s" % (lattendance.timestamp.date(), lattendance.timestamp.time(), lattendance.user_id))
        saatt =str(lattendance.timestamp.time())
        tarihh= str(lattendance.timestamp.date())
        select = 'INSERT INTO personelgc(enrolgc,stringgc,tarih,saat) VALUES(' + lattendance.user_id + ',"' + tarihh + saatt + '","' + tarihh + '","' + saatt + '") ON DUPLICATE key UPDATE saat="' + saatt + '"'

        curmy.execute(select)
        conmy.commit()

    #print("Clear Attendance:", conn.clear_attendance())
#newtime = datetime.today()
#conn.set_time(newtime)
print("Cihaz saati:", conn.get_time())

print("Cihaz Devrede", conn.enable_device())

print("Bağlantı kesildi.", conn.disconnect())
print(len(attendance))

#subprocess.Popen('python opencvvv1.py')
