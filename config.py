import pymysql

# URL 설정
URL_BASE = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008"

# webdriver 경로
WEB_DRIVER_PATH = "C:/SIDE/chromeDirver/"

# DB 설정
# conn = pymysql.connect(host='ip', user='root', password='1111', db='', charset='utf8mb4', use_unicode=True)

# 가장 최근 공고 css-select path
NUM_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(1)'
TYPE_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(2)'
TITLE_CSS_PATH = '#boardList > tr:nth-child(1) > td.align_left > a'
NOTICE_DATE_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(4)'
REGISTER_DATE_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(5)'
DEPARTMENT_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(6)'
