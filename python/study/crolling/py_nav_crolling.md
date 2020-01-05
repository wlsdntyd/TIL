```python
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen

baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusurl = input('다운로드할 사진을 입력하세요 : ')
url = baseurl + urllib.parse.quote_plus(plusurl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgurl = i['data-source']
    with urlopen(imgurl) as f:
        with open('./down/' + plusurl + str(n) + '.jpg', 'wb') as h:
            imgsource = f.read()	# imgurl을 열어서 내용을 변수에 담는 과정.
            h.write(imgsource)		# 내용이 담긴 변수를 새로 만든 파일에 내용을 적는 과정.
    n += 1		# 파일 이름을 안 겹치게 하기 위해.
print("다운로드 완료")
```

> 심심해서 해본 네이버 이미지 검색 목록 이미지 다운하는 크롤링.