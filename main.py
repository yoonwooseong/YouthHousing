from ast import While
import os
import schedule
import time
from config import *
from selenium import webdriver
from message import changeMsgFormat, sendAlarm
from database import connectDataBase, updateNoticeSlim, getNumberOfSavedNotice

##### 한글깨짐 방지 소스 ######
os.environ["NLS_LANG"] = ".AL32UTF8"

global curNoticeNum
global chromeDriver
global scanSchedule

def main():
    global curNoticeNum
    global chromeDriver
    global scanSchedule

    connectDataBase()
    #connectDriverByUrl(URL_BASE) # scan으로 이동

    scanSchedule = schedule.every(10).days.do(scan)
    while True:
        schedule.run_pending()
        time.sleep(1)
    

def connectDriverByUrl(url):
    global chromeDriver

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chromeDriver = webdriver.Chrome(WEB_DRIVER_PATH +'chromedriver.exe')
    chromeDriver.set_window_size(1920, 1280) # 반응형 방지
    chromeDriver.implicitly_wait(3)
    chromeDriver.get(url)
    chromeDriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return chromeDriver

def scan():
    print("scanning ...")
    global chromeDriver

    connectDriverByUrl(URL_BASE)
    #chromeDriver.refresh()
    
    isUpdated, numOfUpdates = checkUpdatedList(chromeDriver)

    if isUpdated:
        info = readPage(chromeDriver)
        message = changeMsgFormat(info, numOfUpdates)
        sendAlarm(message)
        updateNoticeSlim(curNoticeNum)

    else:
        print("최근 공고가 없습니다.")
        chromeDriver.quit()

# 조건 : 공고문이 삭제되지 않는다는 것을 가정
def checkUpdatedList(driver):
    global curNoticeNum

    currentTotalNumStr = driver.find_element_by_css_selector(TOTAL_NOTICE_NUMBER_CSS_PATH).get_attribute('innerHTML')
    currentTotalNum = int(currentTotalNumStr)
    curNoticeNum = currentTotalNum                      # DB에 저장할 갯수
    prevDBNum = getNumberOfSavedNotice(True)                  # DB에 저장되어있는 갯수


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

def stopScan():
    global scanSchedule

    schedule.cancel_job(scanSchedule)
    print("stop scan")
