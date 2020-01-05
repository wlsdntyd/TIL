```python
from urllib.parse import quote_plus
import urllib.request
from bs4 import BeautifulSoup

plusurl = quote_plus(input("검색어를 입력하세요 : "))
i = input("출력할 페이지를 입력하세요 : ")
lastpage = int(i) * 10 - 9
count = 1
pagenum = 1
while pagenum < lastpage + 1:
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusurl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pagenum}'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    data = soup.find_all(class_ = 'sh_blog_title')
    
    for j in data:
        print(j.attrs['href'])
        print(j.attrs['title'])
    print()
    print(f"{count}페이지 출력이 끝났습니다.\n")
    pagenum += 10
    count += 1

```

> 여러 페이지 크롤링하는 코드. 네이버 블로그 페이지 별 제목과 url을 따온 코드.
>
> 다음번엔 url라이브러리 말고 requests라이브러리로 한번 해보자.