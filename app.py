from flask import Flask, render_template, request, redirect
from webDriver import main
from config import URL_BASE
# from mail import *

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/crawl")  # 크롤링 후 데이터 입력 (하기 전에 이전 DB의 마지막 값 불러와서 변경 감지)
def scrape():
    main()
    return render_template("end.html")

app.run(host="localhost")
