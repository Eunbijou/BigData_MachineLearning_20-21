import requests
from urllib.parse import urlparse

keyword = "광운대"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100"
result = requests.get(urlparse(url).geturl(),
    headers = {"X-Naver-Client-ID" : "AId0UtJd5vw1x9i_GznA",
               "X-Naver-Client-Secret" : "c5hDA1MfEE"})

json_obj = result.json()
print("display " + str(json_obj['display']))
print("start " + str(json_obj['start']))
print("items " + str(json_obj['items']))