from flask import Flask, render_template, request, redirect
from webDriver import main
from config import *
import webbrowser

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("home.html")

# 최근 공고 조회 및 전송
@app.route("/crawl")
def scrape():
    main()
    return render_template("end.html")

# 슬랙 초대링크로 이동
# * 개선 필요사항 : 불필요한 랜더링으로 버튼 클릭시 바로 link로 이동하도록 수정 필요
@app.route("/invitation")
def inviation():
    webbrowser.open(SLACK_LINK)
    return render_template("home.html")

# DB 공고 업데이트
@app.route("/admin/db")
def updateDB():
    # Update문 작성 필요
    
    return render_template("home.html")

app.run(host="localhost")
