# -*- coding:cp857 -*-
__author__ = 'NAMIK'
import sys
reload(sys)
sys.path.append("C:\Python27\Lib\site-packages\zklib")

import zklib1
import time
import zkconst
import MySQLdb as mdb
from socket import *

tgtIP = gethostbyname('bishop')
print tgtIP
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8')
curmy = conmy.cursor()

zk = zklib1.ZKLib("192.168.2.224", 4370)

ret = zk.connect()
print "Baßlantç:", ret

if ret == True:
    print "Cihaz Devredçüç", zk.disableDevice()




    attendance = zk.getAttendance()
    print "Giriü áçkçü listesi:"

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

    print "Baßlantç kesildi.", zk.disconnect()