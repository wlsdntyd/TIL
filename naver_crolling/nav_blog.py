import requests
from selenium import webdriver

search = input("검색어를 입력하세요 : ")
baseurl = f"https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={search}&sm=tab_pge&srchby=all&st=sim&where=post&start=1"
url = baseurl + search
html = requests.get(url).text
data = BeautifulSoup(html, 'html.parser')
setdata = data.find_all(class_ = "sh_blog_title")

n = 1

for i in setdata:

    print(i['title'])

    print(i['href'])

    print("%d번째 자료 출력" % n)

    n += 1