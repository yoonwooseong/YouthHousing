import os
from config import conn

#####한글깨짐 방지######
os.environ["NLS_LANG"] = ".AL32UTF8"

URL_BASE = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008#"
db = conn.cursor()


def sample(param):
    sql = 'insert into table (idx, type, postDate, winnerDate, entrepreneur) VALUES (0, %s, %s, %s, %s)'
    val = (param)
    db.execute(sql, val)
    conn.commit()
