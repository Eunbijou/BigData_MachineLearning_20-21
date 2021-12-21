import requests
import bs4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://eosindex.io"

result = requests.get(url, headers = headers).text

bs_obj = bs4.BeautifulSoup(result, "html.parser")
print(bs_obj)