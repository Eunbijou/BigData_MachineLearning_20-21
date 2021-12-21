import requests
import bs4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
# url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=092&aid=0002208870"
# url_1 = "https://news.naver.com"
url = "https://news.naver.com"

def get_news_info(url):

    result = requests.get(url, headers = headers).text
    bs_obj = bs4.BeautifulSoup(result, "html.parser")

    ba = bs_obj.find('div', {'class' : 'press_logo'})
    A1 = ba.find('img')['title']

    bc = bs_obj.find('div', {'class' : 'article_info'})
    bd = bc.find('h3')
    A2 = bd.text

    be = bs_obj.find('span', {'class':'t11'})
    A3 = be.text

    dictionary1 = {}
    dictionary1['news_name'] = A1
    dictionary1['news_title'] = A2
    dictionary1['news_time'] = A3

    return dictionary1

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://news.naver.com"

result = requests.get(url, headers = headers).text
bs_obj = bs4.BeautifulSoup(result, "html.parser")

bd = bs_obj.find('div', {'class' : 'mtype_list_wide'})
bf = bd.find('ul', {'class' : 'mlist2 no_bg'})
bg = bf.findAll('li')

hrefs = [div.find('a')['href']for div in bg]

for number in range(0,5):
    dic_result = get_news_info(hrefs[number])
    print(dic_result)
