from selenium import webdriver
import os

from kakao import send_me_via_kakaotalk, new_token

url = "https://music.bugs.co.kr/chart"
driver_path = "/home/mingyeong/chromedriver"
driver = webdriver.Chrome(driver_path)

def get_top(how_many):  # parameter 를 사용하여 좀더 유연하게
    tops = []
    driver.get(url)
    top_100 = driver.find_elements_by_css_selector("#CHARTrealtime table tbody p.title")
    for rank in range(how_many):
        tops.append(f'{rank+1}위 - {top_100[rank].text}')
    driver.close()
    return str(tops)

if __name__ == "__main__":
    data = get_top(how_many=5)
    access_token = os.getenv("BUGS_ACCESS_TOKEN")
    refresh_token = os.getenv("BUGS_REFRESH_TOKEN")

    status_code = send_me_via_kakaotalk(data, access_token).status_code

    if status_code == 401:
        new_access_token = new_token(refresh_token, os.getenv("BUGS_KEY"))
        os.environ["BUGS_ACCESS_TOKEN"] = new_access_token         
        send_me_via_kakaotalk(data, new_access_token)