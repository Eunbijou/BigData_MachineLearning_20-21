import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")
lis = ul.findAll("li")
# print(ul)
# print(lis[2])

for i in range(0, 3, 1):
    print(lis[i].text)