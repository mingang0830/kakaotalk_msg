from selenium import webdriver

from kakao import send_me_via_kakaotalk

# 순환참조 import 문제인 경우에만 embed import
# def foo():
#     from weather import send_me_via_kakaotalk
#     ...

access_token = "UmM1KhM3Ee-LOLn5q_sA70KoreUmKdaK2oD3fAopyNgAAAF_FvWBJA"

url = "https://music.bugs.co.kr/chart"
driver_path = "/home/mingyeong/chromedriver"
driver = webdriver.Chrome(driver_path)

def get_top5():
    top_5 = []
    driver.get(url)
    top_100 = driver.find_elements_by_css_selector("#CHARTrealtime table tbody p.title")
    for rank in range(5):
        top_5.append(f'{rank+1}위 - {top_100[rank].text}')
    driver.close()
    return top_5

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
    send_me_via_kakaotalk(data, access_token)
