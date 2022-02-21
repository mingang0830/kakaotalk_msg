import os
from bs4 import BeautifulSoup as bs
import requests

from common import parse
from kakao import new_token, send_me_via_kakaotalk

url = "https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=109"


def get_data():
    r = requests.get(url)
    html = r.text
    soup = bs(html, 'html.parser')
    summary_data = soup.select('div.cmp-view-content > p > span')
    return str(summary_data)



if __name__ == "__main__":
    data = parse(get_data())
    access_token = os.getenv("WEATHER_ACCESS_TOKEN")
    refresh_token = os.getenv("WEATHER_REFRESH_TOKEN")

    status_code = send_me_via_kakaotalk(data, access_token).status_code

    if status_code == 401:
        new_access_token = new_token(refresh_token, os.getenv("WEATHER_KEY"))
        os.environ["WEATHER_ACCESS_TOKEN"] = new_access_token         
        send_me_via_kakaotalk(data, new_access_token)


    