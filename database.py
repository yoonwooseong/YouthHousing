from pdb import post_mortem
from config import *
from pymongo import MongoClient
from pymongo.cursor import CursorType

global db

def connectDataBase():
    global db
    mongoClient = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    db = mongoClient['youth_housing']

def updateNoticeSlim(count, date):
    global db
    db.notice_slim.update_one({"_id":1}, {"$set":{"count":count, "date":date}})

def getSavedNotice(isSimple):
    global db
    if isSimple:
        result = db.notice_slim.find_one({"_id":1})
        return int(result['count']), result['date']
    else:
        return

def updateNotice():
    # 공고 전체 내용 저장
    return

def healthCheck():
    try:
        connectDataBase()
        getSavedNotice(True)
        db_state = "complete"

    except:
        db_state = "error"

    print("DB State : " + db_state)
    return db_state