import requests
import bs4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://news.naver.com"

result = requests.get(url, headers = headers).text

bs_obj = bs4.BeautifulSoup(result, "html.parser")
# print(bs_obj)58

bd = bs_obj.find('div', {'class' : 'mtype_list_wide'})
bf = bd.find('ul', {'class' : 'mlist2 no_bg'})
bg = bf.findAll('li')

hrefs = [div.find('a')['href']for div in bg]

print(hrefs)
print(hrefs[0:2])
print(len(hrefs[0:2]))
