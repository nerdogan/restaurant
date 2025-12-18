# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("user-data-dir=saglam")
chrome_options.add_argument("--headless=new")
#chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--window-size=1920,1080")
import time
import re
import datetime
import atexit
import subprocess
import requests
import nenraconfig
from modulemdb import Myddb as mdb

myddb=mdb()
curmy = myddb.cur
curmy.execute("SET NAMES UTF8")
curmy.execute("SET character_set_client=utf8")
token=nenraconfig._GetOption2('token')

siparis=dict()

r2=[]

gecmissip="/html/body/div/div/div/main/div[2]/div[4]/div[2]/div/div/table/tbody/tr"
aktifsip="/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]"
sipsayfa="/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]"
ustbilgi1="/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]"
ustbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div"
urunbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/table/tbody/tr/td"


altbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/div[3]/p"
galtbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/div[3]/div/div/p"

sipkapat="/html/body/div[3]/div/div[1]/div/div/div[1]/button"


def kontrol( girdi):
    girdi = str(girdi)
    ara = re.search(",", girdi)
    if ara:
        derle = re.compile(",")
        cikti = derle.sub("", girdi)
        return cikti
    return girdi


def login(driver):
    toplamsip = 0
    # Load page]
    driver.get("https://www.saglamoglualtin.com/")
    time.sleep(26)
#    driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/form/div[3]/div/button").click()
    #
    # Wait for the login page to
#    driver.find_element_by_xpath("/ html / body / div / div / div / main / div[2] / div[2] / div[1] / div[1] / div / a[2]").click()
#    driver.get("https://restoran.getiryemek.com/r/6059fa557c32c54e27b97fc0/dashboard")

 #   time.sleep(15)
  #  driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a").click()

   # time.sleep(3)

    def listToString(s):

        # initialize an empty string
        str1 = ""
        a=0
        # traverse in the string
        for ele in s:
            str1 += (ele+"  ")

            # return string
        return str1
    while True:
        time.sleep(3)
        siparis.clear()
        xpath = aktifsip
        try:
            followers_elems = driver.find_elements(By.XPATH,xpath)
        except:
            print("hgjhghj")
            continue
        elma = [e.text for e in followers_elems]
        #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),data={'chat_id': 839088426, 'text': listToString(elma)}).json()

        for sip in elma:
            #a=(str(sip).split(":",1))
            siparis["altın"]="USD"
            siparis["tarih"]=datetime.date.today().isoformat()
            siparis["saat"]=datetime.datetime.now().strftime("%H:%M:%S")
            siparis["USD_KG"]=sip
            print(sip)


#            print((listToString(elma)))
        time.sleep(1)
        print ("mongo kaydı")
        print(siparis)
        if len(siparis)>0:
            print(siparis["altın"],siparis["USD_KG"])
            sql1 = "insert into kur (parite,fiyat) values (%s,%s)"
            curmy.execute(sql1, (siparis["altın"],kontrol(siparis["USD_KG"])))
            myddb.conn.commit()
          #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),                              data={'chat_id': 839088426, 'text': str(siparis)}).json()

        time.sleep(3)
        siparis.clear()
        xpath = ustbilgi1
        try:
            followers_elems = driver.find_elements(By.XPATH, xpath)
        except:
            print("hgjhghj")
            continue
        elma = [e.text for e in followers_elems]
        #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),data={'chat_id': 839088426, 'text': listToString(elma)}).json()

        for sip in elma:
            # a=(str(sip).split(":",1))
            siparis["altın"] = "EUR"
            siparis["tarih"] = datetime.date.today().isoformat()
            siparis["saat"] = datetime.datetime.now().strftime("%H:%M:%S")
            siparis["USD_KG"] = sip
            print(sip)

        #            print((listToString(elma)))
        time.sleep(1)
        print("mongo kaydı")
        print(siparis)
        if len(siparis) > 0:
            print(siparis["altın"], siparis["USD_KG"])
            sql1 = "insert into kur (parite,fiyat) values (%s,%s)"
            curmy.execute(sql1, (siparis["altın"], kontrol(siparis["USD_KG"])))
            myddb.conn.commit()
        #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),                              data={'chat_id': 839088426, 'text': str(siparis)}).json()

        time.sleep(3)
        siparis.clear()
        xpath = sipsayfa
        try:
            followers_elems = driver.find_elements(By.XPATH, xpath)
        except:
            print("hgjhghj")
            continue
        elma = [e.text for e in followers_elems]
        #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),data={'chat_id': 839088426, 'text': listToString(elma)}).json()

        for sip in elma:
            # a=(str(sip).split(":",1))
            siparis["altın"] = "TL"
            siparis["tarih"] = datetime.date.today().isoformat()
            siparis["saat"] = datetime.datetime.now().strftime("%H:%M:%S")
            siparis["USD_KG"] = sip
            print(sip)

        #            print((listToString(elma)))
        time.sleep(1)
        print("mongo kaydı")
        print(siparis)
        if len(siparis) > 0:
            print(siparis["altın"], siparis["USD_KG"])
            sql1 = "insert into kur (parite,fiyat) values (%s,%s)"
            curmy.execute(sql1, (siparis["altın"], kontrol(siparis["USD_KG"])))
            myddb.conn.commit()
        #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),                              data={'chat_id': 839088426, 'text': str(siparis)}).json()

        time.sleep(10)
        #driver.execute_script("window.location.reload(true);")
        driver.refresh()
        time.sleep(60)

@atexit.register
def cikis():
    print("sağlamoğlu çıkıyor")
    curmy.close()
   # subprocess.Popen('python3 deneme.py', shell=True)
    requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),  data={'chat_id': 839088426, 'text': "saglamoglu kapandı"}).json()
    # celal 972595010

    pass


if __name__ == "__main__":

    driver = webdriver.Chrome(options=chrome_options)
    try:
        login(driver)
        time.sleep(1)
    finally:
        driver.quit()