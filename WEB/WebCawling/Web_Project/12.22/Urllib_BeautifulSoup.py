import urllib.request
import bs4

url = "https://news.naver.com"
html = urlopen.requests.get(url).text

bs_obj = bs4.BeautifulSoup(html, "html.parser")
print(bs_obj)

top_right = bs_obj.find("div", {"class":"logo_area"})
first_a = top_right.find("a")
print(first_a.text)

top_right = bs_obj.find("div", {"class":"service_area"})
first_a = top_right.find("a")
print(first_a.text)

top_right = bs_obj.find("div", {"class":"search_area"})
first_a = top_right.find("a")
print(first_a.text)

ul = bs_obj.find("div", {"class":"group_nav"})
lis = ul.findAll('li')
print(lis)

for li in lis:
    a_tag = li.find("a")
    print(a_tag.text)


