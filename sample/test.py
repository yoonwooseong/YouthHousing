from operator import truediv
from pickle import FALSE
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import URL_BASE


def readHtml(totalPage, param):
    print("여기")
    totalNotice = {}
    oneNotice = []
    for page in range(totalPage):
        URL = URL_BASE
        print(URL)
        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")

        mainMenuList = soup.find("div", "topWrap").find_all("ul","depth2")[1]
        subMenuList = mainMenuList.find_all("li")
        recruitmentNotice = subMenuList[1].find("a")
        recruitmentNoticeTitle = recruitmentNotice['title']
        print(recruitmentNotice)
        print(recruitmentNoticeTitle)
        if recruitmentNoticeTitle == "모집공고 페이지이동":
            #엔터키 동작
            driver.find_element_by_link_text('Send InMail').click()
            recruitmentNotice.click()
            return





        noticeTable = soup.find("div", {"class": "tableWrap"})
        noticeTbody = noticeTable.find("tbody")
        noticeList = noticeTbody.find_all("tr")

        # 공고번호, 민간 or 공공, 공고명, 공고일, 신청일, 사업자명
        for notice in noticeList:
            infoList = notice.find_all("td")

            index = infoList[0].get_text()
            type = infoList[1].get_text()
            title = infoList[2].get_text()
            postDate = infoList[3].get_text()
            applyDate = infoList[4].get_text()
            entrepreneur = infoList[5].get_text()

            # 한 공고 정보
            resultData = {"index": index, "type": type, "title": title,
                          "postDate": postDate, "applyDate": applyDate, "entrepreneur": entrepreneur}
            print(resultData)
            # 같은 공고 저장 방지
            if resultData not in oneNotice:
                oneNotice.append(resultData)

        totalNotice['param'] = param
        totalNotice['notice'] = oneNotice

    return totalNotice


def crawling(totalPage, param):
    result = readHtml(totalPage, param)
    print(result)
    return result


def isSameNotice(notice, prevNotice):
    if notice['title'] == prevNotice['title'] and notice['type'] == prevNotice['type'] and notice['type'] == prevNotice['type']:
        return True
    else:
        return False


# 가장 최근 공고 비교 후 다르면 같을때까지 비교
# 다른 공고들 메일에 추가
def checkUpdateNotice(readNotice):
    newNotice = []
    prevNotice = ['']  # load DB
    noticeList = readNotice['notice']

    for notice in noticeList:
        if isSameNotice(notice, prevNotice[0]):
            return newNotice
        else:
            newNotice.append(notice)

    return newNotice
