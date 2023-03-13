# -*- coding:utf8 -*-
from typing import List, Any

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import requests
import pymongo
import datetime
import atexit
import subprocess

import nenraconfig

token=nenraconfig._GetOption2('token')

myclient = pymongo.MongoClient("mongodb://192.168.2.251/bishop")
mydb = myclient["bishop"]
mycol = mydb["bishoppaket2021"]
siparis=dict()

r2=[]

guvercingiris="/html/body/div[2]/p[3]/a"
gecmissip="/html/body/div[3]/div/div/div[2]/div[6]/div[2]/table/tbody/tr"
aktifsip="/html/body/div[3]/div/div/div[2]/div[3]/div/div/table/tbody/tr"
sipsayfa="/html/body/div[1]/div/div/div[2]/ul/li[1]/a"
siparisno='/html/body/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/h1'

ustbilgi="/html/body/div[3]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr/td"
altbilgi="/html/body/div[3]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/table[1]/tbody/tr"
galtbilgi="/html/body/div[3]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/table[2]/tbody/tr"
sipkapat="/html/body/div[2]/div/div[1]/div/div/div[1]/button"

def login(driver):
    username = "bishopyesilkoy@gmail.com"  # <username here>
    password = "5533155794"  # <password here>
    toplamsip = 0
    # Load page]
    driver.get("https://siparistakip.yemeksepeti.com")
    time.sleep(3)

    # Login
    driver.find_element_by_name("userName").send_keys(username)
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/button").click()
    # Wait for the login page to
    time.sleep(30)

    def listToString(s):

        # initialize an empty string
        str1 = ""
        a=0
        # traverse in the string
        for ele in s:
            str1 += (ele+"\t ")


            # return string
        return str1
    while True:
        try:
            driver.find_element_by_xpath(sipsayfa).click()
        except:
            time.sleep(1)

        time.sleep(3)

        xpath =aktifsip
        try:
            followers_elems = driver.find_elements_by_xpath(xpath)
            elma = [e.text for e in followers_elems]

        except:
            continue
        for sip in elma:
            print (sip)
            if sip=="Sipariş bulunmamaktadır":
                r2.clear()
        sipadet=len(elma)

        print("sipariş sayısı_ "+str(sipadet))
        if toplamsip!=sipadet:
            toplamsip=sipadet
        for kacinci in range(sipadet+1):
            if sipadet==1:
                detay1 ='/html/body/div[3]/div/div/div[2]/div[3]/div/div/table/tbody/tr'
            else:
                detay1 = "/html/body/div[3]/div/div/div[2]/div[3]/div/div/table/tbody/tr[" + str(
                    kacinci + 1) + "]"

            print ("hangi sipariş")
            print(range(sipadet))

            try:
                driver.find_element_by_xpath(detay1).click()
                time.sleep(5)
            except:
                try:
                    driver.find_element_by_xpath(sipsayfa).click()
                except:
                    time.sleep(1)

                continue

            followers_elems = driver.find_elements_by_xpath(siparisno)
            elma=[e.text for e in followers_elems]
            print(listToString(elma))

            try:
                r1 = re.findall(r'\d+', (listToString(elma)))
                if len(r1)==0:
                    print ("None")
                    continue

                if r1[0] not in r2:
                    r2.append(r1[0])
                    siparis.clear()
                    siparis["sipno"]=(r1[0])
                    siparis["kaynak"]="yemeksepeti"
                else:
                    continue
                    print ("var zaten")
            except:
                pass


            followers_elems = driver.find_elements_by_xpath(altbilgi)
            elma=[e.text for e in followers_elems]
            for sip in elma:
                a=(str(sip).split(":",1))
#                print (a)
                siparis[a[0]]=a[1]

            time.sleep(1)
            followers_elems = driver.find_elements_by_xpath(galtbilgi)
            elma=[e.text for e in followers_elems]

            for sip in elma:
                a=(str(sip).split(":",1))
#                print (a)
                siparis[a[0]]=a[1]
#            print((elma))

            time.sleep(1)
            followers_elems = driver.find_elements_by_xpath(ustbilgi)
            elma=[e.text for e in followers_elems]
            print("ürünbilgi..............................................")

            for sip in elma:
                siparis["urun"]=siparis.get("urun", []) + [sip]
                print(sip)
            try:
                 driver.find_element_by_xpath(sipsayfa).click()
            except:
                print ("sipariş sayfasına geçilemedi")
                time.sleep(1)
            time.sleep(3)
            print ("mongo kaydı")
            print(siparis)
            try:
                mycol.insert(siparis)
  #              requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),                           data={'chat_id': 839088426, 'text': str(siparis)}).json()

            except pymongo.errors.DuplicateKeyError:
                print("kaydedilmiş")
                pass
        break
        time.sleep(40)
        driver.refresh()
        time.sleep(5)


@atexit.register
def cikis():
    print("yemek sepeti çıkıyor")
    myclient.close()
    subprocess.Popen('python3 siparisyazdir.py', shell=True)

  #  requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),    data={'chat_id': 839088426, 'text': "yemeksepeti kapandı"}).json()

    # celal 972595010


if __name__ == "__main__":

    driver = webdriver.Chrome("/home/nerdogan/PycharmProjects/restaurant/chromedriver")
    try:
        login(driver)
        time.sleep(1)
      #  followers = scrape_followers(driver, "instagram")
       # print(followers)
    finally:
        driver.quit()