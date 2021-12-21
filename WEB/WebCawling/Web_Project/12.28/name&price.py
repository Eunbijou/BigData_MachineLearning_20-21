import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "http://jolse.com/category/toners-mists/1019/"

result = requests.get(url, headers = headers)
bs_obj = BeautifulSoup(result.text)

ul = bs_obj.find('ul',{'class' : 'prdList grid4'})
div = ul.findAll('div',{'class' : 'box'})

for box in div:
    tag = box.find('p',{'class' : 'name'})
    span = tag.find('span')
    print(span.text)

    atag = box.findAll('li',{'class' : 'xans-record-'})
    pans = atag[1].findAll("span")
    print(pans[1].text)





