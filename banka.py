import pandas as pd
import ctypes
from ctypes import wintypes


user32 = ctypes.windll.user32

h_wnd = user32.GetForegroundWindow()
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
print(pid.value)

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

xls=pd.ExcelFile("C:\\Users\\NAMIK\\DownLoads\\denizbank aralık.xls")
ana= xls.parse( skiprows=7, index_col=None, na_values=['NA'])
ana['Tarih']=pd.to_datetime(ana['Tarih'],dayfirst=True)


# Verilen tarih aralığındaki kart komisyonlarını günlük ve toplamının bulunması excel dosyası olarak kaydeder
har=ana[ana['Açıklama'].str.contains('243000', regex=False)==True]
filt=har['Tutar(TL)']<0
filt1=har['Tarih'].dt.date >= pd.to_datetime("2019-12-01")
filt2=har['Tarih'].dt.date <= pd.to_datetime("2019-12-31")
df=(har[filt&filt1&filt2])
df=df.groupby(df.Tarih.dt.date)['Tutar(TL)'].sum()
print (df)
print (df.sum())
export_excel = df.to_excel (r'C:\Users\namik\OneDrive\Desktop\gunlukkomisyon.xlsx', index =True, header=True)

# Verilen tarih aralığındaki kart komisyonlarını günlük ve toplamının bulunması excel dosyası olarak kaydeder
har=ana[ana['Açıklama'].str.contains('243000|Aktarım|Artırım', regex=True)==False]
filt=har['Tutar(TL)']<0
filt1=har['Tarih'].dt.date >= pd.to_datetime("2019-12-01")
filt2=har['Tarih'].dt.date <= pd.to_datetime("2019-12-31")
df=(har[filt&filt1&filt2])
print (df)
print (df.sum())
export_excel = df.to_excel (r'C:\Users\namik\OneDrive\Desktop\bankaçıkış.xlsx', index =None, header=True)