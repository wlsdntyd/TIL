```python
from selenium import webdriver
from urllib.request import urlretrieve
import time
import os

keyword = "방탄소년단"
print("접속중")
driver = webdriver.Chrome('./chromedriver.exe')	# './' 요건 현재 위치
driver.implicitly_wait(30)

url = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}'
driver.get(url)

imgs = driver.find_elements_by_css_selector('img._img')	# img태그의 _img가 클래스 이름
result = []
for img in imgs:
    if 'http' in img.get_attribute('src'):	# get_attribute로 속성 '값' 가져옴
        result.append(img.get_attribute('src'))

driver.close()
print("수집완료")

if not os.path.isdir(f'./{keyword}'): #해당 폴더가 없다면 False 반환 고로 True가 된다.
    os.mkdir(f'./{keyword}')	# 폴더 생성.

for index, link in enumerate(result):	# 사진 다운할 때 이름을 다르게 하기 위해 인덱스까지.
    start = link.rfind('.') # 오른쪽에서 부터 해당 문자를 찾아 인덱스 번호 반환
    end = link.rfind('&')
    filetype = link[start:end]  # '.jpg', '.png' 확장자가 다른 경우를 대비해 적음
    
    urlretrieve(link, f'./{keyword}/{keyword}{index}{filetype}')
print("다운로드 완료")
```

> 방탄소년단 사진 다운 크롤링. 재밌다.