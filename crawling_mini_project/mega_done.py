# MEGABOX TOP5
import time
from selenium import webdriver
from bs4 import BeautifulSoup


def movie_list():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://megabox.co.kr/movie');
    time.sleep(0.01)
    movbutton = driver.find_element_by_css_selector(".movie-list-util .onair-condition .btn-onair")
    movbutton.click()
    time.sleep(0.01)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    ol = soup.find('ol', {'class': 'list'})
    lis = ol.findAll('li')
    link = ["", "", "", "", ""]
    name = ["", "", "", "", ""]

    cnt = 0

    for li in lis:

        # 영화 이름
        div = li.find('div', {'class': 'movie-list-info'})
        img = div.find('img')['alt']

        # 상세 링크
        div1 = li.find('div', {'class': 'movie-score'})
        a_tag = div1.find('a')['data-no']
        url = "https://megabox.co.kr/movie-detail?rpstMovieNo=" + str(a_tag)
        link[cnt] = url
        name[cnt] = img

        cnt = cnt + 1
        if cnt > 4:
            break
    driver.close()
    return link, name
