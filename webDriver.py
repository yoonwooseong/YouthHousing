import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from config import conn
from SQL import sample

#####한글깨짐 방지###### 
os.environ["NLS_LANG"] = ".AL32UTF8"

URL_BASE = "http://youth2030.co.kr/user/board/mn010203.do"
URL_PARAM = ""

db = conn.cursor()

def scrape(URL):
    while True:
        driver = webdriver.Chrome('C:/Wooseong/web scraper/chromedriver') # webdriver 경로
        driver.set_window_size(1920,1280)                                 # 반응형 방지
        driver.implicitly_wait(3)
        driver.get(URL)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        
        results = soup.select_one('')
        item = results.select_one('')

        # 크롤링 작업 공간
        
        # 결과 parsing
        data = {}

        driver.quit()
        return data

def saveData(crawlData):
    param = crawlData['param']
    data = crawlData['crawl_data']
    sample(data)

    db.close()
    conn.close()