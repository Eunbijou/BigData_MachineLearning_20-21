# 노원구 약국
from urllib.parse import quote
import requests
import bs4

url = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
servicekey = "gOOVNDaeFPsjOdskvgIGOynsY0fTyr0HJ7HGPSo7BzqVvAl9DSYmq%2FfnDnDykiwDZmY2hs9Hp9Y65fCjL7KZaw%3D%3D&"

Q0 = quote("서울특별시")
Q1 = quote("노원구")
QT = "1"
ORD = "Name"
pageNo = "1"
numOfRows = "10"

paramset = "serviceKey=" + servicekey +"&Q0=" +Q0 + "&Q1=" + Q1 + \
            "&QT=" + QT +"&ORD=" + ORD + "&pageNo=" + pageNo + \
            "&numOfRows=" + numOfRows 

url = url + paramset
print(url)

result = requests.get(url)
bs_obj = result.json()
# bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
# print(bs_obj)
print(bs_obj['item'])
# for item in json_obj['items']:
#     tagged_item = item["dutyName"]
#     print(tagged_item)
