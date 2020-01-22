```python
import urllib.request
from selenium import webdriver 
from bs4 import BeautifulSoup as bs
import csv

url = 'https://www.melon.com/chart/index.htm'
# driver = webdriver.Chrome('.\chromedriver.exe') # 동적 페이지 일 때 해결 방법 1
# driver.implicitly_wait(5)
# driver.get(url)
# html = driver.page_source
# print(html)

hdr = { 'User-Agent' : 'Mozilla/5.0' }   # 동적 페이지 일 때 해결 방법2(header값이 이것만 있진 않다.)
req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = bs(html, 'html.parser')
lst50_100 = soup.select('.lst50, .lst100')  # 두 가지 이상 가지고 오고 싶을 때 해결법.

# for i in lst50_100: # 출력
#     print(i.select_one('.wrap.t_center').text, end=" ")
#     print(i.select_one('.ellipsis.rank01 > span > a').text, end=" ")
#     print(i.select_one('.ellipsis.rank03 > a').text, end=" ")
#     print(i.select_one('.ellipsis.rank02 > a').text)

melonlist = []
for i in lst50_100: # csv파일을 만들기 위해 데이터 저장.
    mlist = []
    mlist.append(i.select_one('.wrap.t_center').text)
    mlist.append(i.select_one('.ellipsis.rank01 > span > a').text)
    # mlist.append(i.select_one('.ellipsis.rank01').a.text) 위와 같다.
    mlist.append(i.select_one('.ellipsis.rank02 > a').text)
    mlist.append(i.select_one('.ellipsis.rank03 > a').text)
    melonlist.append(mlist)

with open('melon100.csv', 'w', encoding='utf-8', newline="") as f:  # csv파일 생성, 인코딩, 새 줄에 출력
    writer = csv.writer(f)
    writer.writerow(['순위', '곡명', '아티스트', '앨범'])   # 첫 번째 열 이름 지정.
    writer.writerows(melonlist)                           # 순서에 맞게 값 저장.
```

> 멜론 1~100위 곡명, 가수, 앨범 크롤링해서 csv파일화 하는 코드. 이젠 좀 쉽다.
>
> selenium은 직접 페이지에 접속하기 때문에 page_source를 따오면 동적 웹이더라도 잘 해결된다.
>
> 두 번째 방식은 헤더값을 줘서 해결하는 건데 원리는 모르겠다.