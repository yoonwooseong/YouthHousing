import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from mailAccount import BUOT

from config import *
# from config import conn
# from SQL import sample

#####한글깨짐 방지######
os.environ["NLS_LANG"] = ".AL32UTF8"

URL_PARAM = ""

# db = conn.cursor()
def main():
    driver = setDriverByUrl(URL_BASE)
    readPage(driver)
    changeMsgFormat()
    sendAlarm()
    return

def setDriverByUrl(url):
    driver = webdriver.Chrome(WEB_DRIVER_PATH +'chromedriver.exe')
    driver.set_window_size(1920, 1280) # 반응형 방지
    driver.implicitly_wait(3)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return driver

def readPage(driver):
    recentlyNum = driver.find_element_by_css_selector(NUM_CSS_PATH)
    recentlyType = driver.find_element_by_css_selector(TYPE_CSS_PATH)
    recentlyTitle = driver.find_element_by_css_selector(TITLE_CSS_PATH)
    recentlyNoticeDate = driver.find_element_by_css_selector(NOTICE_DATE_CSS_PATH)
    recentlyRegisterDate = driver.find_element_by_css_selector(REGISTER_DATE_CSS_PATH)
    recentlyDepartment = driver.find_element_by_css_selector(DEPARTMENT_CSS_PATH)
    
    print(recentlyTitle.get_attribute('innerHTML'))
    driver.quit()

def changeMsgFormat():
    print()

def sendAlarm():
    token = BUOT
    channel = "#공고-알림"
    text = "test message"

    #Post 메소드로 전송, headers에 Bearer 인증 방법 사용
    requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer "+token}, data={"channel":channel, "text":text})
    