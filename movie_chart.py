from bs4 import BeautifulSoup as bs
import os
import requests

from common import parse
from kakao import send_me_via_kakaotalk, new_token

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

def get_titles():
    r = requests.get(url)
    html = r.text
    soup = bs(html, "html.parser")
    titles = soup.select("div.box-contents > a > strong.title")
    return str(titles)

def rank(movie_list):
    movie_list = movie_list.split(", ")
    result = []
    for ranking in range(len(movie_list)):
        result.append(f'{ranking+1}위 - {movie_list[ranking]}')
    return str(result)[1:-1]

if __name__ == "__main__":
    titles = parse(get_titles())
    data = rank(titles)

    access_token = os.getenv("MOVIE_ACCESS_TOKEN")
    refresh_token = os.getenv("MOVIE_REFRESH_TOKEN")

    status_code = send_me_via_kakaotalk(data, access_token).status_code

    if status_code == 401:
        new_access_token = new_token(refresh_token, os.getenv("WEATHER_KEY"))
        os.environ["MOVIE_ACCESS_TOKEN"] = new_access_token         
        send_me_via_kakaotalk(data, new_access_token)

