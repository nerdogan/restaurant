# -*- coding:utf8 -*-
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email(user, pwd, recipient, subject, body):


    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject



    # Prepare actual message
    fp = open(body, 'rb')
    pdf = fp.read()
    fp.close()
    pdfAttachment = MIMEApplication(pdf, _subtype="pdf")
    pdfAttachment.add_header('content-disposition', 'attachment', filename=('utf-8', '', 'maliyet.pdf'))
    text = MIMEMultipart('alternative')
    text.attach(MIMEText("Some plain text \n", "plain", _charset="utf-8"))
    text1 = MIMEMultipart('alternative')
    text1.attach(
        MIMEText("<html><head>Some HTML text</head><body><h1>Some HTML Text</h1> Another line of text</body></html>",
                 "html", _charset="utf-8"))
    message = MIMEMultipart('mixed')
    message.attach(text)
    message.attach(text1)
    message.attach(pdfAttachment)
    message['Subject'] = subject
    message['From'] = 'erdogannamik@gmail.com'
    message['To'] = 'namikerdogan@hotmail.com'
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message.as_string())
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

send_email('erdogannamik@gmail.com','qazxcv654152','namikerdogan@hotmail.com','personel giriş çıkış bilgilendirme','/Users/namikerdogan/nenra/maliyet.pdf')