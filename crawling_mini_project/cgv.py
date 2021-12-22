from bs4 import BeautifulSoup
import urllib.request

def movie_list():
    html = urllib.request.urlopen('http://www.cgv.co.kr/movies/')
    soup = BeautifulSoup(html, 'html')
    titles = soup.find_all('div', 'box-contents')

    front_url = 'http://www.cgv.co.kr'

    cnt = 0
    link = ["", "", "", "", ""]
    name = ["", "", "", "", ""]

    for title in titles:

        mn = title.find('strong').text
        ml = front_url + title.find('a')['href']

        link[cnt] = ml
        name[cnt] = mn

        cnt = cnt + 1
        if cnt > 4:
            break

    return link, name


