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
sys.setdefaultencoding('utf8')
API_KEY = "58fee02c2e20ed7511b179af994fc34850f84656"
CHANNEL_NAME = "attendance1"
p = Pushetta(API_KEY)
ab=0



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

tgtIP = gethostbyname('nen.duckdns.org')
print tgtIP
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8',port=30000)
curmy = conmy.cursor()
curmy.execute("SET NAMES UTF8")
curmy.execute("SET character_set_client=utf8")

sys.setdefaultencoding('utf8')

selectt="SELECT adsoyad,saat,tarih,id FROM personelgc where mail='0' "


def yenile():


    curmy.execute(selectt)
    aa=curmy.fetchall()
    if len(aa)==0:
        print   "Yeni hareket yok"


    for row in aa:
        a1=row[0]
        a2=str(row[1])
        a3=str(row[2])
        a4=(row[3])

        bodyy="\n\n"+a3+" tarihinde saat "+a2+" personelimiz "+a1+" giriş-çıkış yapmıştır. \n\nBilgilerinize\n NAMIK ERDOĞAN"
        send_email('erdogannamik@gmail.com','qazxcv654152','orhangunendii@gmail.com','personel giriş çıkış bilgilendirme',bodyy)
        appnot=a3+u" tarihinde saat "+a2+u" personelimiz "+a1+u" giriş yapmıştır"

        #app.notify(event_name='Gec',trackers=appnot)
        p.pushMessage(CHANNEL_NAME, appnot,expire="2017-01-30")
        print row[0],row[1],row[2]
        curmy.execute("update personelgc SET mail='1' where id=%s ",(a4,))
        conmy.commit()
        ttim.sleep(10)







while True:
    ab += 1

    subprocess.Popen('python persatt.py')
    ttim.sleep(10)
    yenile()
    conmy.commit()
    a,b = divmod(ab,50)

    if b==0:
        subprocess.Popen('python twgonder.py')
        subprocess.Popen('python masa1.py')
        p.pushMessage("admin-nen", ab,expire="2017-01-30")
    print "_______________________________________________________________" , ab
    ttim.sleep(300)



