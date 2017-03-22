# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Replace below path with the absolute path
# to chromedriver in your computer


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\NAMIK\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\") #Path to your chrome profile
driver = webdriver.Chrome( chrome_options=options)


# driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Aşkım"'

# Replace the below string with your own message
string = "Message sent using Python!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))

input_box.send_keys(string + Keys.ENTER)
time.sleep(10)