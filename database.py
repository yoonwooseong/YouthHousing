from pdb import post_mortem
from config import *
from pymongo import MongoClient
from pymongo.cursor import CursorType

global db

def connectDataBase():
    global db
    mongoClient = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    db = mongoClient['youth_housing']

def updateNoticeSlim(count):
    global db
    db.notice_slim.update_one({"_id":1}, {"$set":{"count":count}})

def getNumberOfSavedNotice(isSimple):
    global db
    if isSimple:
        result = db.notice_slim.find_one({"_id":1})

        # 만약 없다면 신규로 재생성 로직 추가
        
        return int(result['count']) 
    else:
        return

def updateNotice():
    # 공고 전체 내용 저장
    return