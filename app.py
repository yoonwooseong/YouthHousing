from flask import Flask, render_template, request, redirect
from crawl import crawling
from webDriver import saveData

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/crawl") # 크롤링 후 데이터 입력 (하기 전에 이전 DB의 마지막 값 불러와서 변경 감지)
def scrape():
    param = {}
    crawlData = crawling(1, param)
    print(crawlData)
    # saveData(crawlData)
    return render_template("end.html")

# @app.route("/apply") # 버튼 클릭 시 -> 카카오 로그인 -> redirect로 complete 페이지에서 code 가져오고 DB에 새롭게 데이터가 추가되면 알림 전송
# def scrape():
#     return render_template("complete.html")


app.run(host="localhost")