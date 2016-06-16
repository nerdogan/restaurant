# -*- coding:utf8 -*-
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
import smtplib
from socket import *
import subprocess
import sys
reload(sys)
from pushetta import Pushetta

API_KEY = "58fee02c2e20ed7511b179af994fc34850f84656"
CHANNEL_NAME = "attendance"
p = Pushetta(API_KEY)




def send_email(user, pwd, recipient, subject, body):


    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

tgtIP = gethostbyname('bishop')
print tgtIP
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8')
curmy = conmy.cursor()


sys.setdefaultencoding('utf8')

selectt="SELECT adsoyad,saat,tarih FROM personelgc where mail='0' "


def yenile():

    ab="0"
    curmy.execute(selectt)
    aa=curmy.fetchall()
    if len(aa)==0:
        print   "Yeni hareket yok"


    for row in aa:
        a1=row[0]
        a2=str(row[1])
        a3=str(row[2])

        bodyy="\n\n"+a3+" tarihinde saat "+a2+" personelimiz "+a1+" giriş-çıkış yapmıştır. \n\nBilgilerinize\n NAMIK ERDOĞAN"
        send_email('erdogannamik@gmail.com','qazxcv654152','orhangunendii@gmail.com','personel giriş çıkış bilgilendirme',bodyy)
        appnot=a3+" tarihinde saat "+a2+" personelimiz "+a1+" giriş yapmıştır"

        #app.notify(event_name='Gec',trackers=appnot)
        p.pushMessage(CHANNEL_NAME, appnot)
        print row[0],row[1],row[2]


    curmy.execute("update personelgc SET mail='1' " )




    """   ab=0
    aa=cur.execute(slectaylik )
    print "AYLIK DAGILIM "
    print " "
    for row in aa:
        print '%s -- %s  TL --  %s ADET ' % (row[0], row[2],row[1])
        ab=ab+row[2]

    print "toplam       :",ab """

while True:

    subprocess.Popen('python persatt.py')
    ttim.sleep(10)
    yenile()
    conmy.commit()
    print "_______________________________________________________________"
    ttim.sleep(300)



