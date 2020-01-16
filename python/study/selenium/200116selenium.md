```python
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = wd.Chrome('chromedriver.exe')
driver.implicitly_wait(30)
driver.get('http://tour.interpark.com/')
search = driver.find_element_by_xpath('//*[@id="SearchGNBText"]')
search.send_keys('달랏')
time.sleep(2)
enter = driver.find_element_by_xpath('//*[@id="dHead"]/div[2]/div[1]/form/fieldset/button[1]')
enter.click()
time.sleep(2)
body = driver.find_element_by_css_selector('body')
for _ in range(2):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
more = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[5]/div[4]/ul/li[6]/button')
more.click()
time.sleep(1)
for _ in range(4):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
btns = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[5]/div[4]/ul/li[*]')
i = 1
for btn in btns:
    if int(btn.text) == i:
        btns[i + 1].click()
        i += 1
        time.sleep(3)
        for _ in range(3):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
lists = driver.find_elements_by_css_selector('ul.boxList > li')
for i in lists:
    src = i.find_element_by_css_selector('a > img')
    img_source = src.get_attribute('src')
    title = i.find_element_by_css_selector('h5.proTit')
    url = title.get_attribute('onclick')
    passage = i.find_element_by_css_selector('p.proSub')
    price = i.find_element_by_css_selector('strong.proPrice')
    many = i.find_element_by_css_selector('div.info-row')
    print("이미지 : ", img_source, "\n링크 : ", url, "\n상품명 : ", title.text, "\n추가설명 : ", passage.text, "\n가격 : ", price.text, many.text)
    print("=====================================================================================")
```

> 집가서해야지