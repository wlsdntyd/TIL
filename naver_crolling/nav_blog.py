import requests
from bs4 import BeautifulSoup

search = input("검색어를 입력하세요 : ")
baseurl = f"https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={search}&sm=tab_pge&srchby=all&st=sim&where=post&start=1"
url = baseurl + search
html = requests.get(url).text
data = BeautifulSoup(html, 'html.parser')
li = data.select('ul.type01 > li')

for i in li:
    img = i.select_one('img')
    src = img['src']
    title_href = i.select_one('li > dl > dt > a')
    title = title_href['title']
    href = title_href['href']
    passage = i.select_one('dd.sh_blog_passage')
    print(title)
    print(passage.text)
    print(href)
    print(src)
    print("")