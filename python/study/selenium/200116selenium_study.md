```python
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
# driver = wd.Chrome(executable_path='chromedriver.exe')
driver = wd.PhantomJS(executable_path='phantomjs.exe')
driver.implicitly_wait(30)
driver.get('https://finance.naver.com/')
search = driver.find_element_by_xpath('//*[@id="stock_items"]')
# search1 = driver.find_element_by
search.send_keys('멀티캠퍼스')
search.send_keys(Keys.ENTER)

lists = driver.find_element_by_css_selector('#tab_con1 > div.first > table > tbody')
print(lists.text)
driver.close()
```

> phantormjs를 이용한 네이버 증권 창에서 멀티캠퍼스 검색 후 정보가져오기.