import pymysql

# DB 설정
conn = pymysql.connect(host = 'ip', user = 'root', password = '1111', db = '', charset = 'utf8mb4', use_unicode=True)

# URL 설정
URL_BASE = "http://youth2030.co.kr/user/board/mn010203.do"