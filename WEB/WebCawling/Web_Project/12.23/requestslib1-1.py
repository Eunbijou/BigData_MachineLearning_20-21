import requests
import bs4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=092&aid=0002208870"

result = requests.get(url, headers = headers).text

bs_obj = bs4.BeautifulSoup(result, "html.parser")

ba = bs_obj.find('div', {'class' : 'press_logo'})
bb = ba.find('img')['title']
print(bb)

bc = bs_obj.find('div', {'class' : 'article_info'})
bd = bc.find('h3')
print(bd.text)

be = bs_obj.find('span', {'class':'t11'})
print(be.text)

