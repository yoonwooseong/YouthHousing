import requests
from oauth import BUOT
from config import *

def changeMsgFormat(info, numOfUpdates):
    message = (
        "["+info['type']+"] " + info['title'] + "\n"
        " - 청약신청일 : " + info['registerDate'] + "\n"
        " - 공고게시일 : " + info['noticeDate'] + "\n"
        " - 사업자 : " + info['department'] + "\n"
        " - 공고 보러가기 : " + info['link']
    )

    if numOfUpdates > 1:
        message = changeManyMsgFormat(message, numOfUpdates)

    return message

def changeManyMsgFormat(message, numOfUpdates): 
    frontMsgFormat = str(numOfUpdates)+"개의 공고가 추가되었습니다!" + "\n\n"
    backMsgFormat = "\n\n" + " * 그 밖의 공고 보러가기 : " + URL_BASE
    message = frontMsgFormat + message + backMsgFormat

    return message

def sendAlarm(message):
    token = BUOT
    channel = "#공고-알림"
    text = message

    #Post 메소드로 전송, headers에 Bearer 인증 방법 사용
    requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer "+token}, data={"channel":channel, "text":text})
    