import requests
import urllib.request
import bs4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
# http://useragentstring.com/ 참고
url = "https://news.naver.com"
html = requests.get(url, headers = headers).text

bs_obj = bs4.BeautifulSoup(html, "html.parser")
# print(bs_obj)

# top_right = bs_obj.find("div", {"class":"logo_area"})
# first_a = top_right.find("a")
# print(first_a.text)
#
# top_right = bs_obj.find("div", {"class":"service_area"})
# first_a = top_right.find("a")
# print(first_a.text)
#
# top_right = bs_obj.find("div", {"class":"search_area"})
# first_a = top_right.find("a")
# print(first_a.text)

# ul = bs_obj.find("div", {"class":"group_nav"})
# lis = ul.findAll('li')
# print(lis)
#
# for li in lis:
#     a_tag = li.find("a")
#     print(a_tag.text)


newsnow_txarea = bs_obj.findAll("ul", {"class" : "mlist2 no_bg"})
# print(newsnow_txarea)
lis = newsnow_txarea[1].findAll("li")

for li in lis:
    strong = li.find("strong")
    print(strong.text)
