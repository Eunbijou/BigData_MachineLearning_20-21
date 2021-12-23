# 서울시 약국 오후 9시 이후까지 여는 곳
from urllib.parse import quote
import requests
import bs4

url = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
servicekey = "gOOVNDaeFPsjOdskvgIGOynsY0fTyr0HJ7HGPSo7BzqVvAl9DSYmq%2FfnDnDykiwDZmY2hs9Hp9Y65fCjL7KZaw%3D%3D&"

Q0 = quote("서울특별시")
QT = "1"
ORD = "Name"
pageNo = "1"
numOfRows = "10"

paramset = "serviceKey=" + servicekey +"&Q0=" +Q0 + \
            "&QT=" + QT +"&ORD=" + ORD + "&pageNo=" + pageNo + \
            "&numOfRows=" + numOfRows

url = url + paramset
print(url)

result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")
# print(bs_obj)

count = 0
for item in items:
    tagged_item = item.find("dutyTime1c")
    if(tagged_item != None):
        close_time = int(tagged_item.text)
        if(close_time > 2100):
            count += 1
            

print("서울특별시 내 9시 이후까지 하는 약국의 수 : " + str(count))
