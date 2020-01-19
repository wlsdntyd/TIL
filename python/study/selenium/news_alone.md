```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas

search = input("검색할 키워드를 입력하세요 : ")
driver = webdriver.Chrome('chromedriver.exe')
url = f'https://search.naver.com/search.naver?query={search}&where=news'
driver.implicitly_wait(5)
driver.get(url)

for _ in range(5):	# 페이지 넘기기
    try:
        driver.find_element_by_css_selector('a.next').click()
        time.sleep(1)
    except:
        break

titles = driver.find_elements_by_class_name('_sp_each_title')
titles = [title.text for title in titles]

passas = driver.find_elements_by_css_selector('a._sp_each_url')
passas = [passa.text for passa in passas]

news = driver.find_elements_by_css_selector('span._sp_each_source')
news = [new.text for new in news]

result = list(zip(titles, news, passas))

col = ('제목','계열','몰라')
dataframe = pandas.DataFrame(result, columns=col)
dataframe.to_excel('title&new.xlsx', sheet_name='제목과 계열', startrow=0, header=True)
```

> 혼자 구현해본 네이버 뉴스 크롤링&엑셀 형식으로 저장.