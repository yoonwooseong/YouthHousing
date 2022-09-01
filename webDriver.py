import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from oauth import BUOT

from config import *
# from config import conn
# from SQL import sample

##### 한글깨짐 방지 소스 ######
os.environ["NLS_LANG"] = ".AL32UTF8"

URL_PARAM = ""

# db = conn.cursor()
def main():
    driver = setDriverByUrl(URL_BASE)
    isUpdated, numOfUpdates = checkUpdatedList(driver)
    if isUpdated:
        info = readPage(driver)
        message = changeMsgFormat(info, numOfUpdates)
        sendAlarm(message)

    else:
        print("최근 공고가 없습니다.")
        driver.quit()


def setDriverByUrl(url):
    driver = webdriver.Chrome(WEB_DRIVER_PATH +'chromedriver.exe')
    driver.set_window_size(1920, 1280) # 반응형 방지
    driver.implicitly_wait(3)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return driver

# 판별 방식의 조건은 공고문이 삭제되지 않는다는 것을 가정
def checkUpdatedList(driver):
    currentTotalNumStr = driver.find_element_by_css_selector(TOTAL_NOTICE_NUMBER_CSS_PATH).get_attribute('innerHTML')
    currentTotalNum = int(currentTotalNumStr)
    prevDBNum = 37 # DB에 저장되어있는 갯수

    isUpdated = True if currentTotalNum > prevDBNum else False
    numOfUpdates = currentTotalNum - prevDBNum

    return isUpdated, numOfUpdates

def readPage(driver):
    recentlyNum = driver.find_element_by_css_selector(NUM_CSS_PATH)
    recentlyType = driver.find_element_by_css_selector(TYPE_CSS_PATH)
    recentlyTitle = driver.find_element_by_css_selector(TITLE_CSS_PATH)
    recentlyNoticeDate = driver.find_element_by_css_selector(NOTICE_DATE_CSS_PATH)
    recentlyRegisterDate = driver.find_element_by_css_selector(REGISTER_DATE_CSS_PATH)
    recentlyDepartment = driver.find_element_by_css_selector(DEPARTMENT_CSS_PATH)
    info = {
        'num' : recentlyNum.get_attribute('innerHTML'),
        'type' : recentlyType.get_attribute('innerHTML'),
        'title' : recentlyTitle.get_attribute('innerHTML'),
        'noticeDate' : recentlyNoticeDate.get_attribute('innerHTML'),
        'registerDate' : recentlyRegisterDate.get_attribute('innerHTML'),
        'department' : recentlyDepartment.get_attribute('innerHTML'),
        'link' : recentlyTitle.get_attribute('href')
    }

    driver.quit()
    return info

def changeMsgFormat(info, numOfUpdates):
    message = (
        "["+info['type']+"] " + info['title'] + "\n"
        " - 청약신청일 : " + info['registerDate'] + "\n"
        " - 공고게시일 : " + info['noticeDate'] + "\n"
        " - 사업자 : " + info['department'] + "\n"
        " - 공고 보러가기 : " + info['link']
    )

    if numOfUpdates > 1:
        message = changeManyMsgFormat(message, numOfUpdates)

    return message

def changeManyMsgFormat(message, numOfUpdates): 
    frontMsgFormat = str(numOfUpdates)+"개의 공고가 추가되었습니다!" + "\n\n"
    backMsgFormat = "\n\n" + " * 그 밖의 공고 보러가기 : " + URL_BASE
    message = frontMsgFormat + message + backMsgFormat

    return message

def sendAlarm(message):
    token = BUOT
    channel = "#공고-알림"
    text = message

    #Post 메소드로 전송, headers에 Bearer 인증 방법 사용
    requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer "+token}, data={"channel":channel, "text":text})
    