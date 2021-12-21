import requests
from urllib.parse import urlparse

keyword = "광운대"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(),
    headers = {"X-Naver-Client-ID" : "AId0UtJd5vw1x9i_GznA",
               "X-Naver-Client-Secret" : "c5hDA1MfEE"})

json_obj = result.json()
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['display'])

# for item in json_obj['items']:
#     print(item)