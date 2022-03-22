import requests
from bs4 import BeautifulSoup
from config import URL_BASE

def readHtml(totalPage, param):
    totalNotice = {}
    oneNotice = []
    for page in range(totalPage):
        URL = URL_BASE

        request = requests.get(URL)
        soup = BeautifulSoup(request.text, "html.parser")
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
            resultData = {"index": index, "type": type, "title": title, "postDate": postDate, "applyDate": applyDate, "entrepreneur": entrepreneur}
            
            # 같은 공고 저장 방지
            if resultData not in oneNotice:
                oneNotice.append(resultData)

        totalNotice['param'] = param
        totalNotice['notice'] = oneNotice

    return totalNotice

def crawling(totalPage, param):
    result = readHtml(totalPage, param)
    return result
