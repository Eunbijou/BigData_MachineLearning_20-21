# 1~5위 영화 이름
import urllib.request
import bs4
def movie_list():
    url = "https://www.cinecube.co.kr/movie/list.jsp?flag=1"
    html = urllib.request.urlopen(url)

    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    list2 = bs_obj.find("ul", {"class": "movie_list"})

    movie = list2.findAll("span")

    movie_name = [movie[6].text, movie[12].text, movie[18].text, movie[24].text, movie[30].text]

    # 1~5 까지 링크 출력
    href = ["", "", "", "", "", ""]
    i = 0
    for link in list2.findAll('a', {"class": "btn_mdetail"}):
        href[i] = link['href']
        i = i + 1

    movie_link = ['https://www.cinecube.co.kr/movie/'+href[1], 'https://www.cinecube.co.kr/movie/'+href[2], 'https://www.cinecube.co.kr/movie/'+href[3], 'https://www.cinecube.co.kr/movie/'+href[4], 'https://www.cinecube.co.kr/movie/'+href[5]]

    return movie_link, movie_name
