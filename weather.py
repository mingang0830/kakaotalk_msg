from bs4 import BeautifulSoup as bs
import re
import requests
import json


url = "https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=109"


def get_data():
    r = requests.get(url)
    html = r.text
    soup = bs(html, 'html.parser')
    summary_data = soup.select('div.cmp-view-content > p > span')
    return summary_data


def send_me_via_kakaotalk(data):
    template_object = {
        "object_type": 'text',
        "text": data,
        "link": {
            "web_url": url,
            "mobile_web_url": url,
        },
        "button_title": "기상청 홈페이지"
    }
    access_token = "o0sFFZ7dlOI5Jv-4wTPbDpghUGc8wWnE0SaZuwo9dNoAAAF_AO36lQ"
    response = requests.post("https://kapi.kakao.com/v2/api/talk/memo/default/send",
                             headers={"Authorization": f"Bearer {access_token}"},
                             data={"template_object": json.dumps(template_object)})
    
def parse(data):
  html_tag = re.compile('<.*?>')
  result = re.sub(html_tag, '', data)
  return result



if __name__ == "__main__":
    data = parse(str(get_data()))
    send_me_via_kakaotalk(data)
    print(data)
    