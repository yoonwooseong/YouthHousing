from flask import Flask, render_template, request, redirect
from crawl import crawling
from webDriver import saveData

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/crawl")
def scrape():
    param = {}
    
    crawlData = crawling(param)
    saveData(crawlData)
    return render_template("scrapepage.html")

app.run(host="localhost")