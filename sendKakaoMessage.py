import requests
import json

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

# 6시간 만료시간 -> 리프레시 토큰으로 갱신

data={
    "template_object": json.dumps({
    	"object_type": "text",
        "text": "[역세권 청년주택]\n\n새로운 공고가 등록되었습니다.\n홈페이지를 확인해주세요.",
        "link": {
            "web_url" : "http://youth2030.co.kr/user/board/mn010203.do",
            "mobile_web_url" : "http://youth2030.co.kr/user/board/mn010203.do"
        },
        "buttons": [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "http://youth2030.co.kr/user/board/mn010203.do",
                    "mobile_web_url": "http://youth2030.co.kr/user/board/mn010203.do"
                }
            }
        ]
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code
print(response.status_code)
