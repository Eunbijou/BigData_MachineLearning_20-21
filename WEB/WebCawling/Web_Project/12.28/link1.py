import requests
from bs4 import BeautifulSoup

def get_page_products(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    # url = "http://jolse.com/category/toners-mists/1019/"

    result = requests.get(url, headers=headers)
    bs_obj = BeautifulSoup(result.text)

    ul = bs_obj.find('ul', {'class' : 'prdList grid4'})
    div = ul.findAll('div', {'class' : 'box'})
    product_info_list = [Toner_Search(box) for box in div]

    return product_info_list

def Toner_Search(box):
    tag = box.find('p', {'class' : 'name'})
    span = tag.find('span')
    name = span.text

    atag = box.findAll('li', {'class' : 'xans-record-'})
    pans = atag[1].findAll("span")
    price = pans[1].text

    a_tag = box.find('a')
    b_tag = a_tag['href']

    return {"name" : name, "price" : price, "link" : "http://jolse.com" + b_tag}

for num in range(1,6):
    try:
        url = "http://jolse.com/category/toners-mists/1019/?page=" + str(num)
        results = get_page_products(url)

        for result in results:
            print("name : " + (result['name']) + ", price : " + (result['price']))

        print("현재페이지 #" + str(num))
    except:
        print("오류발생")







