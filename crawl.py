import requests
from bs4 import BeautifulSoup

URL_BASE = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008#"

def goUrl(totalPage, param):
    data = {}
    crawl_data = []
    for page in range(totalPage):
        URL = URL_BASE  # + parameter ..

        result = requests.get(URL)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find("div", {"class": "tableWrap"})
        noticeArea = results.find("tbody")
        noticeList = noticeArea.find_all("tr")

        for notice in noticeList:
            infoList = notice.find_all("td")

            index = infoList[0].get_text()
            type = infoList[1].get_text()
            title = infoList[2].get_text()
            postDate = infoList[3].get_text()
            applyDate = infoList[4].get_text()
            entrepreneur = infoList[5].get_text()
            crawlData = {"index": index, "type": type, "title": title, 
                         "postDate": postDate, "applyDate": applyDate, "entrepreneur": entrepreneur}
            # 같은 공고문 저장 방지
            if crawlData not in crawl_data:
                crawl_data.append(crawlData)

        data['param'] = param
        data['crawl_data'] = crawl_data

    return data

def crawling(totalPage, param):
    data = goUrl(totalPage, param)
    return data
