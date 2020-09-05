# -*- coding:utf8 -*-
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
import smtplib
from socket import *
import subprocess
import requests
import sys
import nenraconfig

token=nenraconfig._GetOption2('token')


url1 = 'https://pushmeapi.jagcesar.se'

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
        print('successfully sent the mail')
    except:
        print("failed to send mail")


tgtIP = gethostbyname('nen.duckdns.org')
print(tgtIP)
conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8',port=30000)
curmy = conmy.cursor()
curmy.execute("SET NAMES UTF8")
curmy.execute("SET character_set_client=utf8")


selectt="SELECT adsoyad,saat,tarih,id FROM personelgc where mail='0' "


def yenile():


    curmy.execute(selectt)
    aa=curmy.fetchall()
    if len(aa)==0:
        print("Yeni hareket yok !!")

    for row in aa:
        a1=row[0]
        a2=str(row[1])
        a3=str(row[2])
        a4=(row[3])

        bodyy="\n\n"+a3+" tarihinde saat "+a2+" personelimiz "+a1+" giriş-çıkış yapmıştır. \n\nBilgilerinize\n NAMIK ERDOĞAN"
      # send_email('erdogannamik@gmail.com','qazxcv654152','orhangunendii@gmail.com','personel giriş çıkış bilgilendirme',bodyy)
        appnot=a3+u" "+a2+u"  "+a1


        r=requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),
                      data={'chat_id': -362841907, 'text': appnot}).json()
        print (r)

        print(row[0], row[1], row[2])
        curmy.execute("update personelgc SET mail='1' where id=%s ",(a4,))
        conmy.commit()
        ttim.sleep(1)







while True:
    ab += 1

    subprocess.Popen("/home/nerdogan/PycharmProjects/restaurant/venv/bin/python persatt.py",shell=True)

#    subprocess.Popen("python3 getiryemek.py",shell=True)

    ttim.sleep(10)
    yenile()
    conmy.commit()
    a,b = divmod(ab,50)

    if b==0:
        pass
        #subprocess.Popen('python twgonder.py')
    print("_______________________________________________________________", ab)
    ttim.sleep(60)



