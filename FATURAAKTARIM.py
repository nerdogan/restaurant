# -*- coding: cp1254 -*-
__author__ = 'NAMIK'
import pymssql
class Mmdb():
    def __init__(self):


        # connect to the database
        self.conn = pymssql.connect("WINSERVER","sa","QaZ147WsX","MYSYS_2015")
        # create a cursor
        self.cur = self.conn.cursor()
    def cek(self,sql):
        # extract all the data
        self.cur.execute(sql)
        # show the result
        self.result = self.cur.fetchall()
        return self.result

Mmdb1=Mmdb()
sql = """SELECT TOP 1000
[Kdv_Orani],
sum([GTutari] ),
     sum([KdvTutari])

  FROM [MYSYS_2015].[dbo].[STOK_Fis_Kalem] WHERE Fis_No=45 AND Fis_Tipi=50 GROUP BY [Kdv_Orani] """

sonuc= Mmdb1.cek(sql)
print sonuc[0][0], sonuc[0][1]


"""
SELECT TOP 1000

[Kdv_Orani],
sum([GTutari] ),
     sum([KdvTutari])

  FROM [MYSYS_2015].[dbo].[STOK_Fis_Kalem] WHERE Fis_No=45 AND Fis_Tipi=50 GROUP BY [Kdv_Orani]

"""
dosya=open(r"C:\Users\NAMIK\Google Drive\bishop\deneme1.csv","w")
dosya.writelines("EvrakTarihi;EvrakNo;Açıklama;GenelToplam;Matrah;KDV\n")
dosya.write("elma")
dosya.writelines("21.09.2015;7777;PROFESYONEL GIDA;883,17;817,75;65,42")
