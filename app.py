from flask import Flask, render_template, request, redirect
from main import main, stopScan
from config import *
import webbrowser

app = Flask(__name__)

global state
state = "stop"

@app.route("/")
def home():
    return render_template("home.html")

# 슬랙 초대링크로 이동
# * 개선 필요사항 : 불필요한 랜더링으로 버튼 클릭시 바로 link로 이동하도록 수정 필요
@app.route("/invitation")
def inviation():
    webbrowser.open(SLACK_LINK)
    return render_template("home.html")

# 알림 시작
@app.route("/admin/start")
def start():
    global state
    if state == "stop":
        state = "start"
        main()
    return render_template("home.html")

# 알림 중지
@app.route("/admin/stop")
def stop():
    global state
    
    state = "stop"
    stopScan()
    return render_template("home.html")

if __name__ == '__main__':
    app.run()
