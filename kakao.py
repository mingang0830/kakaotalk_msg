import requests
import json

def new_token(refresh_token, client_id) -> str:
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "refresh_token", 
        "client_id": client_id,
        "refresh_token": refresh_token 
    }    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(url , headers=headers, data=data)
    new_token = response.json()

    return new_token["access_token"]


def send_me_via_kakaotalk(data, access_token):
    template_object = {
        "object_type": 'text',
        "text": data,
        "link": {
            "web_url": "",
            "mobile_web_url": "",
        },
        "button_title": "더보기"
    }
    response = requests.post("https://kapi.kakao.com/v2/api/talk/memo/default/send",
                             headers={"Authorization": f"Bearer {access_token}"},
                             data={"template_object": json.dumps(template_object)})
    return response


