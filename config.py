from oauth import DB_HOST

# URL 설정
URL_BASE = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008"

# webdriver 경로
WEB_DRIVER_PATH = "C:/SIDE/chromeDirver/"

# DB 설정
MONGODB_HOST = DB_HOST
MONGODB_PORT = 27017

# Slack 초대 링크
SLACK_LINK = "https://join.slack.com/t/youthhousinghq/shared_invite/zt-1fgpdx8q9-_VS~4yj1R~euf60hyP0Jxg"

# 전체 공고 갯수
TOTAL_NOTICE_NUMBER_CSS_PATH = "#schResult1 > strong"
# 가장 최근 공고 css-select path
NUM_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(1)'
TYPE_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(2)'
TITLE_CSS_PATH = '#boardList > tr:nth-child(1) > td.align_left > a'
NOTICE_DATE_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(4)'
REGISTER_DATE_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(5)'
DEPARTMENT_CSS_PATH = '#boardList > tr:nth-child(1) > td:nth-child(6)'

START_TEXT = "알람 설정이 완료되었습니다."
STOP_TEXT = "알람을 삭제하였습니다."
ERROR_TEXT = "설정을 실패하였습니다. 네트워크를 확인해 주세요."
