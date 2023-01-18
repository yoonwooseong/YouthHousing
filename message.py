import requests
from oauth import BUOT
from config import *

def sendNotice(message):
    token = BUOT
    channel = "#공지사항"
    text = message

    #Post 메소드로 전송, headers에 Bearer 인증 방법 사용
    requests.post("http://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer "+token}, data={"channel":channel, "text":text})

def sendAlarm(message):
    token = BUOT
    channel = "#공고-알림"
    text = message

    #Post 메소드로 전송, headers에 Bearer 인증 방법 사용
    requests.post("http://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer "+token}, data={"channel":channel, "text":text})

def writeMessage(info, numOfUpdates):
    message = (
        "["+info['type']+"] " + info['title'] + "\n"
        " - 청약신청일 : " + info['registerDate'] + "\n"
        " - 공고게시일 : " + info['noticeDate'] + "\n"
        " - 사업자 : " + info['department'] + "\n"
        " - 공고 보러가기 : " + info['link']
    )

    if numOfUpdates > 1:    # 공고 갯수 추가
        message = changeMoreMsg(message, numOfUpdates)
    elif numOfUpdates == 0: # 공고 갯수 동일, 공고 날짜가 다른 경우
        message = changeCustomMsg(message)

    return message

def changeMoreMsg(message, numOfUpdates): 
    frontMsgFormat = str(numOfUpdates)+"개의 공고가 추가되었습니다!" + "\n\n"
    backMsgFormat = "\n\n" + " * 그 밖의 공고 보러가기 : " + URL_BASE
    message = frontMsgFormat + message + backMsgFormat

    return message

def changeCustomMsg(message): 
    frontMsgFormat = "변경된 공고가 있습니다." + "\n\n"
    backMsgFormat = "\n\n" + " * 변경된 공고 확인하러 가기 : " + URL_BASE
    message = frontMsgFormat + message + backMsgFormat

    return message