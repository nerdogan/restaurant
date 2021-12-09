import sys
import pandas as pd
from PyQt5 import QtGui, QtCore,QtWidgets

app = QtWidgets.QApplication(sys.argv)
fname = QtWidgets.QFileDialog.getOpenFileName()
print(fname)
tarih1="2021-10-01"
tarih2="2021-10-31"


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#xls=pd.ExcelFile("C:\\Users\\NAMIK\\DownLoads\\denizbank pos202007.xls")
xls=pd.ExcelFile(fname[0])

ana= xls.parse( skiprows=7, index_col=None, na_values=['NA'])
ana['Tarih']=pd.to_datetime(ana['Tarih'],dayfirst=True)


# Verilen tarih aralığındaki kart komisyonlarını günlük ve toplamının bulunması excel dosyası olarak kaydeder
har=ana[ana['Açıklama'].str.contains('11781999-651', regex=False)==True]
filt=har[har.columns[2]]<0
filt1=har['Tarih'].dt.date >= pd.to_datetime(tarih1)
filt2=har['Tarih'].dt.date <= pd.to_datetime(tarih2)
df=(har[filt&filt1&filt2])
df=df.groupby(df.Tarih.dt.date)[df.columns[2]].sum()
print (df)
print (df.sum())
export_excel = df.to_excel (r'C:\Users\bisho\OneDrive\Desktop\gunlukkomisyon'+tarih2+'.xlsx', index =True, header=True)

# Verilen tarih aralığındaki kart komisyonlarını günlük ve toplamının bulunması excel dosyası olarak kaydeder
har=ana[ana['Açıklama'].str.contains('243000|Aktarım|Artırım', regex=True)==False]
filt=har[har.columns[2]]<0
filt1=har['Tarih'].dt.date >= pd.to_datetime(tarih1)
filt2=har['Tarih'].dt.date <= pd.to_datetime(tarih2)
df=(har[filt&filt1&filt2])
print (df)
print (df.sum())
export_excel = df.to_excel (r'C:\Users\bisho\OneDrive\Desktop\bankaçıkış.xlsx', index =None, header=True)