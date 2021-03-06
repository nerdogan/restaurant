# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver):
    username = "erdogannamik@gmail.com"  # <username here>
    password = "qazxcV12"  # <password here>

    # Load page
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Login
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button").click()

    # Wait for the login page to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "See All")))


def scrape_followers(driver, account):
    # Load account page
    driver.get("https://www.instagram.com/{0}/".format(account))

    # Click the 'Follower(s)' link
    driver.find_element_by_partial_link_text("follower").click()

    # Wait for the followers modal to load
    xpath = "//div[@style='position: relative; z-index: 1;']/div/div[2]/div/div[1]"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))

    # You'll need to figure out some scrolling magic here. Something that can
    # scroll to the bottom of the followers modal, and know when its reached
    # the bottom. This is pretty impractical for people with a lot of followers

    # Finally, scrape the followers
    xpath = "//div[@style='position: relative; z-index: 1;']//ul/li/div/div/div/div/a"
    followers_elems = driver.find_elements_by_xpath(xpath)

    return [e.text for e in followers_elems]


if __name__ == "__main__":
    driver = webdriver.Firefox()
    try:
        login(driver)
        followers = scrape_followers(driver, "instagram")
        print(followers)
    finally:
        driver.quit()