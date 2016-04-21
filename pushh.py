# -*- coding:utf8 -*-
import sys
reload(sys)
from instapush import Instapush,App
app=App(appid='5716c8375659e3a956080a46',secret='ae9a83ef6a5ffbc976309d9cc3f911f6')
#app.notify('Gec',{'isim':'Namık ERDOĞAN','tarih':'2016-04-20','gir':'giriş','saat':'9:51'})
a1="Namık ERDOĞAN"
a2="22:12:00"
a3="2014/04/20"

appnot={'plu':a1}




app.notify(event_name='sat',trackers=appnot)