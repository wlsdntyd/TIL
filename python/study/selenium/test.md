```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://www.naver.com'
driver.implicitly_wait(5)
driver.get(url)

driver.find_element_by_css_selector('input#query').send_keys('인공지능')
driver.find_element_by_css_selector('input#query').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_css_selector('div.news.section._prs_nws_all > div.section_more > a.go_more').click()
time.sleep(1)

titles = driver.find_elements_by_css_selector('a._sp_each_title')
titles = [title.text for title in titles]
image_sources = driver.find_elements_by_css_selector('a.sp_thmb.thmb80 > img')
print(len(image_sources))
img_src = []
for image_source in image_sources:
    image_source = image_source.get_attribute('src')
    if 'http' in image_source:
        img_src.append(image_source)

titimg = list(zip(titles, img_src))
col = ["title", "src"]
data_frame = pd.DataFrame(titimg, columns=col)
data_frame.to_excel('titimg.xlsx', "new", startrow=0, header=True)
```

> 강의 시간에 구현해봄