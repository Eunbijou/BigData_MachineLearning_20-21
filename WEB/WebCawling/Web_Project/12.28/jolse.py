import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "http://jolse.com"

result = requests.get(url, headers = headers)
bs_obj = BeautifulSoup(result.text)
print(bs_obj)