from urllib.request import urlopen
import json

s_date = "2020-01-01"
e_date = "2020-12-29"

url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/"\
      + s_date +"/edate/" + e_date

text = urlopen(url)
json_objs = json.load(text)

for item in json_objs:
    print(item['date']+ "@" + item["settlement"])