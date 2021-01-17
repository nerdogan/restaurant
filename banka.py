import sys
import pandas as pd
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)
fname = QtGui.QFileDialog.getOpenFileName()
print(fname)



pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#xls=pd.ExcelFile("C:\\Users\\NAMIK\\DownLoads\\denizbank 202008.xls")
xls=pd.ExcelFile(fname)

ana= xls.parse( skiprows=7, index_col=None, na_values=['NA'])
ana['Tarih']=pd.to_datetime(ana['Tarih'],dayfirst=True)


# Verilen tarih aralığındaki kart komisyonlarını günlük ve toplamının bulunması excel dosyası olarak kaydeder
har=ana[ana['Açıklama'].str.contains('243000', regex=False)==True]
filt=har[har.columns[2]]<0
filt1=har['Tarih'].dt.date >= pd.to_datetime("2020-12-01")
filt2=har['Tarih'].dt.date <= pd.to_datetime("2020-12-31")
df=(har[filt&filt1&filt2])
df=df.groupby(df.Tarih.dt.date)[df.columns[2]].sum()
print (df)
print (df.sum())
export_excel = df.to_excel (r'C:\Users\namik\OneDrive\Desktop\gunlukkomisyon.xlsx', index =True, header=True)

# Verilen tarih aralığındaki kart komisyonlarını günlük ve toplamının bulunması excel dosyası olarak kaydeder
har=ana[ana['Açıklama'].str.contains('243000|Aktarım|Artırım', regex=True)==False]
filt=har[har.columns[2]]<0
filt1=har['Tarih'].dt.date >= pd.to_datetime("2020-12-01")
filt2=har['Tarih'].dt.date <= pd.to_datetime("2020-12-31")
df=(har[filt&filt1&filt2])
print (df)
print (df.sum())
export_excel = df.to_excel (r'C:\Users\namik\OneDrive\Desktop\bankaçıkış.xlsx', index =None, header=True)