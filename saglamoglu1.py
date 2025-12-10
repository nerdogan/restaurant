# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("user-data-dir=saglam")

import time
import requests
import pymongo
import datetime
import atexit
import subprocess
import nenraconfig

import MySQLdb as mdb

token=nenraconfig._GetOption2('token')

myclient = pymongo.MongoClient("mongodb://192.168.2.251/bishop")
mydb = myclient["bishop"]
mycol = mydb["saglamoglu"]
siparis=dict()

r2=[]



gecmissip="/html/body/div/div/div/main/div[2]/div[4]/div[2]/div/div/table/tbody/tr"
aktifsip="/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[6]/td[2]"
sipsayfa="/html/body/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td"
ustbilgi1="/html/body/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div"
ustbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div"
urunbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/table/tbody/tr/td"


altbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/div[3]/p"
galtbilgi="/html/body/div[3]/div/div[1]/div/div/div[2]/div[3]/div/div/p"

sipkapat="/html/body/div[3]/div/div[1]/div/div/div[1]/button"


def login(driver):
    toplamsip = 0
    # Load page]
    driver.get("https://www.saglamoglualtin.com/")
    time.sleep(6)
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
            siparis["altın"]="ALTIN"
            siparis["tarih"]=datetime.date.today().isoformat()
            siparis["saat"]=datetime.datetime.now().strftime("%H:%M:%S")
            siparis["USD_KG"]=siparis.get("USD_KG", []) + [sip]
            print(sip)


#            print((listToString(elma)))
        time.sleep(1)
        print ("mongo kaydı")
        print(siparis)
        try:
            if len(siparis)>0:
                mycol.update_one({'altın':'ALTIN'},{ '$set': siparis})
          #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),                              data={'chat_id': 839088426, 'text': str(siparis)}).json()

        except pymongo.errors.DuplicateKeyError:
            print("kaydedilmiş")
            pass



        time.sleep(40)
        driver.refresh()
        time.sleep(10)

@atexit.register
def cikis():
    print("sağlamoğlu çıkıyor")
    myclient.close()
   # subprocess.Popen('python3 deneme.py', shell=True)

  #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),  data={'chat_id': 839088426, 'text': "getiryemek kapandı"}).json()
    # celal 972595010

    pass


if __name__ == "__main__":

    driver = webdriver.Chrome("/home/nerdogan/PycharmProjects/restaurant/chromedriver",chrome_options=chrome_options)
    try:
        login(driver)
        time.sleep(1)
    finally:
        driver.quit()