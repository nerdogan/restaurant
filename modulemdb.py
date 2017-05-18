# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     23.01.2014
# Copyright:   (c) NAMIK ERDOĞAN 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import MySQLdb
import os
from socket import *
import nenraconfig




tgtIP = gethostbyname(nenraconfig._GetOption('server'))

print(tgtIP)
class Myddb():
    def __init__(self):
        # connect to the database
        self.conn = MySQLdb.connect(tgtIP, nenraconfig._GetOption('user'), nenraconfig._GetOption('password'), 'test', charset='utf8',port=int(nenraconfig._GetOption('port')));


        # create a cursor
        self.cur = self.conn.cursor()
        self.cur.execute("SET NAMES UTF8")
        self.cur.execute("SET character_set_client=utf8")







    def cek( self , sql):

        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()

        return self.result

    def cek1( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        sql=" '%"+ sql +"%'"
        print sql
        sql1="select * from "+tablenam+ " where "+colname+" like "+sql
        if colname=="hamad":
            sql1=sql1+"and kategori<>3 or hamkod like "+sql +" or barkod1 like "+sql
        print sql1
        self.cur.execute(sql1)
        # show the result
        self.result = self.cur.fetchall()
        return self.result
    def cek2( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"
        print sql
        sql1="select * from "+tablenam+ " where "+colname+" = %s "

        self.cur.execute(sql1,[sql])
        # show the result
        self.result = self.cur.fetchall()
        return self.result

    def sil( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"
        print sql
        sql1="delete from "+tablenam+ " where "+colname+" = %s "
        print sql1
        self.cur.execute(sql1,[sql])
        # show the result
        self.result =  self.cur.lastrowid
        return self.result



    def kaydet( self,deger0,deger1,deger2):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"

        sql1="insert into recete (menukod,hamkod,miktar) values (%s,%s,%s)"
        print sql1
        print self.cur.execute(sql1,(deger0,deger1,deger2))

        # show the result
        print "Auto Increment ID: %s" % self.cur.lastrowid
        self.result = self.cur.lastrowid

        return self.result

    def kapat(self):
        self.cur.close()
        self.conn.close()

class Myddb1():
    def __init__(self):
        # connect to the database
        self.conn = MySQLdb.connect(tgtIP, nenraconfig._GetOption('user'), nenraconfig._GetOption('password'), 'test', charset='utf8',port=int(nenraconfig._GetOption('port')));


        # create a cursor
        self.cur = self.conn.cursor()
        self.cur.execute("SET NAMES UTF8")
        self.cur.execute("SET character_set_client=utf8")







    def cek( self , sql):

        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()

        return self.result

    def cek1( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        sql=" '%"+ sql +"%'"
        print sql
        sql1="select * from "+tablenam+ " where "+colname+" like "+sql
        if colname=="hamad":
            sql1=sql1+"and kategori<>3 or hamkod like "+sql +" or barkod1 like "+sql
        print sql1
        self.cur.execute(sql1)
        # show the result
        self.result = self.cur.fetchall()
        return self.result
    def cek2( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"
        print sql
        sql1="select * from "+tablenam+ " where "+colname+" = %s "

        self.cur.execute(sql1,[sql])
        # show the result
        self.result = self.cur.fetchall()
        return self.result

    def sil( self,sql,tablenam,colname):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"
        print sql
        sql1="delete from "+tablenam+ " where "+colname+" = %s "
        print sql1
        self.cur.execute(sql1,[sql])
        # show the result
        self.result =  self.cur.lastrowid
        return self.result



    def kaydet( self,deger0,deger1,deger2):
        # extract all the data
        #sql = "select * from %s" % self.tablename
        #sql="'"+ sql +"'"

        sql1="insert into recete (menukod,hamkod,miktar) values (%s,%s,%s)"
        print sql1
        print self.cur.execute(sql1,(deger0,deger1,deger2))

        # show the result
        print "Auto Increment ID: %s" % self.cur.lastrowid
        self.result = self.cur.lastrowid

        return self.result

    def kapat(self):
        self.cur.close()
        self.conn.close()
