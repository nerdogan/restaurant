# -*- coding: utf8 -*-
__author__ = 'NAMIK'
import sys
reload(sys)
sys.path.append("C:\Python27\Lib\site-packages\zklib")

import zklib1
import time
import zkconst
import MySQLdb as mdb
from socket import *

tgtIP = gethostbyname('nen.duckdns.org')
print tgtIP
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8',port=30000)
curmy = conmy.cursor()
curmy.execute("SET NAMES UTF8")
curmy.execute("SET character_set_client=utf8")

zk = zklib1.ZKLib("192.168.2.224", 4370)

ret = zk.connect()
print "Bağlantı:", ret

if ret == True:
    print "Cihaz Devredışı", zk.disableDevice()




    attendance = zk.getAttendance()
    print len(attendance)

    print "Giriş çıkış listesi:"

    if ( attendance ):
        for lattendance in attendance:
            if lattendance[1] == 15:
                state = 'Check In'
            elif lattendance[1] == 0:
                state = 'Check Out'
            else:
                state = 'Undefined'

            print " %s, %s , %s,   %s" % ( lattendance[2].date(), lattendance[2].time(), lattendance[0], state )
            saatt =str(lattendance[2].time())
            tarihh= str(lattendance[2].date())
            select='INSERT INTO personelgc(enrolgc,stringgc,tarih,saat) VALUES('+lattendance[0]+',"'+tarihh+saatt+'","' + tarihh+ '","' + saatt+'") ON DUPLICATE KEY UPDATE saat="'+ saatt+'"'

            curmy.execute(select)
            conmy.commit()

        #print "Clear Attendance:", zk.clearAttendance()

    print "Cihaz saati:", zk.getTime()

    print "Cihaz Devrede", zk.enableDevice()

    print "Bağlantı kesildi.", zk.disconnect()