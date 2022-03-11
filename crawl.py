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
        results = soup.find_all("tr", {"class": "basicList"})

        for result in results:
            mobHide = result.find_all("td", {"class": "mobHide"})
            title = result.find("td", {"class": "subject"}).find(
                "a").get_text()    # 공고문 제목
            # 민간 or 공공
            type = mobHide[0].get_text()
            # 공고 게시일
            postDate = mobHide[1].get_text()
            # 당첨자 발표일
            winnerDate = mobHide[2].get_text()
            # 당첨자 발표일
            entrepreneur = mobHide[3].get_text()
            crawlData = {"mobHide": mobHide, "title": title, "type": type,
                         "postDate": postDate, "winnerDate": winnerDate, "entrepreneur": entrepreneur}
            if crawlData not in crawl_data:
                crawl_data.append(crawlData)

        data['param'] = param
        data['crawl_data'] = crawl_data
    return data


def crawling(param):
    data = goUrl(param)
    return data
