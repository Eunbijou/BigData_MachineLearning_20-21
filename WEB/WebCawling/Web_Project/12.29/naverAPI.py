import os
import sys
import urllib.request

client_id = "AId0UtJd5vw1x9i_GznA"
client_secret = "c5hDA1MfEE"

encText = urllib.parse.quote("광운대")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-ID", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200) :
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code : " + rescode)