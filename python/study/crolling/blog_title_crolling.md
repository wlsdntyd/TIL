```python
from urllib.parse import quote_plus
import urllib.request
from bs4 import BeautifulSoup

baseurl = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
plusurl = input("검색어를 입력하세요 : ")
url = baseurl + quote_plus(plusurl)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

data = soup.find_all(class_ = 'sh_blog_title')
for i in data:
    print(i['href'])
    print(i['title'])
    print()
print("출력이 끝났습니다.")
```

> 네이버 검색을 통해 블로그 제목과 url 뽑아오는 웹 크롤링. 손에 어느정도 감이 생겼다.