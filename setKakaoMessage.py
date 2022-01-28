import requests

# https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '' # api key
redirect_uri = 'http://youth2030.co.kr/user/board/mn010203.do'
authorize_code = '' # token key

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)