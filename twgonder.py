# -*- coding: utf-8 -*-
'''Post a message to twitter'''


import ConfigParser
import time as ttim
import getopt
import os
import sys
import twitter
import json
import panda as pd
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
import MySQLdb as mdb
from socket import *
reload(sys)
sys.setdefaultencoding('utf8')
tgtIP = gethostbyname('nen.duckdns.org')
print tgtIP

conmy = mdb.connect(tgtIP, "nen","654152", "bishop",charset='utf8' , port=30000)
curmy = conmy.cursor()



USAGE = '''Usage: tweet [options] message

  This script posts a message to Twitter.

  Options:
'''


def PrintUsageAndExit():
    print USAGE
    sys.exit(2)


def GetConsumerKeyEnv():
    return os.environ.get("TWEETUSERNAME", None)


def GetConsumerSecretEnv():
    return os.environ.get("TWEETPASSWORD", None)


def GetAccessKeyEnv():
    return os.environ.get("TWEETACCESSKEY", None)


def GetAccessSecretEnv():
    return os.environ.get("TWEETACCESSSECRET", None)


class TweetRc(object):
    def __init__(self):
        self._config = None

    def GetConsumerKey(self):
        return self._GetOption('consumer_key')

    def GetConsumerSecret(self):
        return self._GetOption('consumer_secret')

    def GetAccessKey(self):
        return self._GetOption('access_key')

    def GetAccessSecret(self):
        return self._GetOption('access_secret')

    def _GetOption(self, option):
        try:
            return self._GetConfig().get('Tweet', option)
        except:
            return None

    def _GetConfig(self):
        if not self._config:
            self._config = ConfigParser.ConfigParser()
            self._config.read(os.path.expanduser('.tweetrc'))
        return self._config


def main():
    try:
        shortflags = 'h'
        longflags = ['help', 'consumer-key=', 'consumer-secret=',
                     'access-key=', 'access-secret=', 'encoding=']
        opts, args = getopt.gnu_getopt(sys.argv[1:], shortflags, longflags)
    except getopt.GetoptError:
        PrintUsageAndExit()
    consumer_keyflag = None
    consumer_secretflag = None
    access_keyflag = None
    access_secretflag = None
    encoding = None
    for o, a in opts:
        if o in ("-h", "--help"):
            PrintUsageAndExit()
        if o in ("--consumer-key"):
            consumer_keyflag = a
        if o in ("--consumer-secret"):
            consumer_secretflag = a
        if o in ("--access-key"):
            access_keyflag = a
        if o in ("--access-secret"):
            access_secretflag = a
        if o in ("--encoding"):
            encoding = a
    message = ' '.join(args)
    if not message:
        message=" "
    rc = TweetRc()
    consumer_key = consumer_keyflag or GetConsumerKeyEnv() or rc.GetConsumerKey()
    consumer_secret = consumer_secretflag or GetConsumerSecretEnv() or rc.GetConsumerSecret()
    access_key = access_keyflag or GetAccessKeyEnv() or rc.GetAccessKey()
    access_secret = access_secretflag or GetAccessSecretEnv() or rc.GetAccessSecret()
    if not consumer_key or not consumer_secret or not access_key or not access_secret:
        PrintUsageAndExit()
    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_key, access_token_secret=access_secret,
                      input_encoding=encoding)
    try:
        results = api.GetSearch(term='''"I'm at Bishop in"''',count=100)
        print len(results)
        print "-------------------------------------------------------------------"
        for i in results:
            print i.text.encode('utf-8')
            print  i.user.screen_name
            print i.user.name
            tar=(i.created_at).split(' ',5)
            tarr=tar[0]+' '+tar[1]+' '+tar[2]+' '+tar[3]+' '+tar[5]
            date_object = datetime.strptime(tarr, '%a %b %d  %H:%M:%S  %Y')+timedelta(hours=3)
            tarih=date_object.strftime("%Y-%m-%d %H:%M:%S")

            print tarih
            select='INSERT INTO twittergc(enrolgc,stringgc,tarih,saat,screen_name) VALUES('+str(i.user.followers_count)+',"'+tarih+'","' + str(date_object.date())+ '","' + str(date_object.time())+ '","' +i.user.screen_name+'") ON DUPLICATE KEY UPDATE saat="'+ str(date_object.time())+'"'

            curmy.execute(select)
            conmy.commit()


    except UnicodeDecodeError:
        print "Your message could not be encoded.  Perhaps it contains non-ASCII characters? "
        print "Try explicitly specifying the encoding with the --encoding flag"
        sys.exit(2)
    selectt="SELECT screen_name,saat,tarih FROM twittergc where mail='0' "
    curmy.execute(selectt)
    aa=curmy.fetchall()
    if len(aa)==0:
        print   "Yeni tweet hareketi yok"


    for row in aa:
        a1='@'+row[0]+' Bizi tercih ettiğiniz için teşekkürler! Bishop Restaurant  '+str(row[1])
        print a1
        status = api.PostUpdate(a1)
        print "%s şimdi gönderildi: %s" % (status.user.name, status.text)
    curmy.execute("update twittergc SET mail='1' " )
    conmy.commit()


print "_______________________________________________________________"
main()
