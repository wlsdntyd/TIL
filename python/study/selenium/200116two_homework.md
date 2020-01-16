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
time.sleep(1)
enter = driver.find_element_by_xpath('//*[@id="dHead"]/div[2]/div[1]/form/fieldset/button[1]')
enter.click()
time.sleep(1)
body = driver.find_element_by_css_selector('body')
for _ in range(2):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

more = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[5]/div[4]/ul/li[6]/button')
more.click()

time.sleep(2)
for _ in range(3):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
 
j = 2
for _ in range(4):
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
    btn = driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div[5]/div[4]/ul/li[{j}]')
    btn.click()
    j += 1
    time.sleep(3)
driver.close()
```

> 16일 첫 번째 문제 완성,,,,, 스스로 해낸게 대단하다.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://info.nec.go.kr/main/showDocument.xhtml?electionId=0000000000&topMenuId=VC&secondMenuId=VCCP09')
driver.find_element_by_css_selector('#electionType1').click()
time.sleep(1)
driver.find_element_by_css_selector('#electionName').click()
time.sleep(1)
driver.find_element_by_css_selector('#electionName > option:nth-of-type(2)').click()
time.sleep(1)
driver.find_element_by_css_selector('#electionCode').click()
time.sleep(1)
driver.find_element_by_css_selector('#electionCode > option:last-of-type').click()
time.sleep(1)
driver.find_element_by_css_selector('#cityCode').click()
time.sleep(1)
driver.find_element_by_css_selector('#cityCode > option:nth-of-type(2)').click()
time.sleep(1)   # 타임슬립 없으면 너무 빠르다.
driver.find_element_by_css_selector('#searchBtn').click()   
# 검색 화면 출력
i = [2,3,6,7,9,18]
for n in range(6):
    num = i[n]
    list1 = driver.find_element_by_css_selector(f'tbody > tr:nth-child({num}) > td:nth-of-type(1)')
    list4 = driver.find_element_by_css_selector(f'tbody > tr:nth-child({num}) > td:nth-of-type(4)')
    list5 = driver.find_element_by_css_selector(f'tbody > tr:nth-child({num}) > td:nth-of-type(5)')
    list6 = driver.find_element_by_css_selector(f'tbody > tr:nth-child({num}) > td:nth-of-type(6)')
    print(list1.text, list4.text, list5.text, list6.text, end=" ")
    print("")
```

> 16일 두 번째 문제. 잘 풀은 거 같은데 한 줄 출력이 안 된다.