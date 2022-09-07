from flask import Flask, render_template, request, redirect
from main import main, stopScan
from config import *

app = Flask(__name__)

global state
state = "stop"

@app.route("/")
def home():
    return render_template("home.html", slack_link = SLACK_LINK)

# 알림 시작
@app.route("/admin/start")
def start():
    global state
    if state == "stop":
        state = "start"
        # Background schedule로 변경 예정
        main()
        return render_template("complete.html", text = START_TEXT)
    else:
        return render_template("complete.html", text = ERROR_TEXT)

# 알림 중지
@app.route("/admin/stop")
def stop():
    global state
    if state == "start":
        state = "stop"
        stopScan()
        return render_template("complete.html", text = STOP_TEXT)
    else:
        return render_template("complete.html", text = ERROR_TEXT)

if __name__ == '__main__':
    app.run()
