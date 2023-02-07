from flask import Flask, render_template, request, redirect
from svc.main import startScan, stopScan
from svc.common.database import healthCheck
from svc.common.config import *
from svc.message import sendNotice
from svc.common.oauth import ADMIN_PW

app = Flask(__name__)

global state
state = "stop"

@app.route("/")
def home():
    return render_template("home.html", slack_link = SLACK_LINK, youth_url = URL_BASE)

# 관리자 페이지
@app.route("/admin")
def goAdmin():
    pw = request.args.get('pw', default = '', type = str)
    if(pw == ADMIN_PW):
        return render_template("admin.html")
    else:
        return render_template("home.html", slack_link = SLACK_LINK, youth_url = URL_BASE)

# 공지사항 알림
@app.route('/admin/notice', methods=['GET','POST'])
def requestNotice():
    if request.method == 'POST':
        message = request.form['notice_content']
        message = str(message)
        print(message)
        sendNotice(message)
    return render_template("complete.html", text = SEND_TEXT)

# DB 상태 확인
@app.route("/admin/healthCheck")
def checkState():
    db_state = healthCheck()

    if db_state == "complete":
        return render_template("home.html", slack_link = SLACK_LINK, youth_url = URL_BASE)
    elif db_state == "error":
        return render_template("complete.html", text = DB_ERROR_TEXT)
    else:
        return render_template("complete.html", text = ERROR_TEXT)
        
# 알림 시작
@app.route("/admin/start")
def start():
    global state
    if state == "stop":
        state = "start"
        startScan()
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
