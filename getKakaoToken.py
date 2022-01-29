import requests

rest_api_key = ''
redirect_uri = 'http://youth2030.co.kr/user/board/mn010203.do'
url = 'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id='+rest_api_key+'&redirect_uri='+redirect_uri

response = requests.get(url)