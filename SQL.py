import os
from config import conn

#####한글깨짐 방지###### 
os.environ["NLS_LANG"] = ".AL32UTF8"

URL_BASE = "http://youth2030.co.kr/user/board/mn010203.do"
db = conn.cursor()

def sample(param):
    sql =  'insert into table (idx, type, postDate, winnerDate, entrepreneur) VALUES (0, %s, %s, %s, %s)'
    val = (param)
    db.execute(sql, val)
    conn.commit()