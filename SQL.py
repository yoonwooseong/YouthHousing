import os
from config import conn, URL_BASE

#####한글깨짐 방지######
os.environ["NLS_LANG"] = ".AL32UTF8"

db = conn.cursor()

def sample(param):
    sql = 'insert into table (idx, type, postDate, winnerDate, entrepreneur) VALUES (0, %s, %s, %s, %s)'
    val = (param)
    db.execute(sql, val)
    conn.commit()

def selectAllNotice(param):
    sql = 'select * from notice'
    db.execute(sql)
    notice = db.fetchall()
    return notice

def selectNotice(param):
    sql = 'select * from notice LIMIT 1'
    db.execute(sql)
    notice = db.fetchall()
    return notice

def insertNotice(param):
    sql = 'insert into notice (idx, index, type, title, postDate, applyDate, entrepreneur) VALUES (0, %s, %s, %s, %s, %s, %s)'
    val = (param)
    db.execute(sql, val)
    conn.commit()

