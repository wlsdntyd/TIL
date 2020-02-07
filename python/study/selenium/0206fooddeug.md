```python
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
import pandas
import numpy
import time
import csv

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://store.naver.com/restaurants/list?filterId=s13479409&page=1&query=%EC%97%AD%EC%82%BC%EC%97%AD%20%EB%A7%9B%EC%A7%91'
driver.get(url)
driver.implicitly_wait(10)

addr_to_latilongti = [] # 나중에 위도 경도 크롤링 시 이용
result_list = []
for _ in tqdm(range(3)):  # 1 반복 당 100개 리스트 maximum 300개
    for i in tqdm(range(3, 8)):
        food_list = driver.find_elements_by_css_selector('div.list_item_inner')
        href_list = []

        for food in food_list:
            time.sleep(0.5)
            href_list.append(food.find_element_by_css_selector('span.tit_inner > a.name').get_attribute('href'))

        for href in tqdm(href_list):
            result = []
            driver.execute_script('location="' + href + '"')
            result.append(driver.find_element_by_css_selector('strong.name').text)
            result.append(driver.find_element_by_css_selector('span.category').text)
            try:
                result.append(driver.find_element_by_css_selector('a.thumb_area.fl > div.thumb > img').get_attribute('src'))
            except:
                source_list = driver.find_element_by_css_selector('div.thumb_area._item > a.thumb > img').get_attribute('src')
                result.append(source_list)
                # img_source = []   주석 처리 4줄 이미지 여러개 크롤링
                # img_list = driver.find_elements_by_css_selector('a.thumb_area.fl > div.thumb > img')
                # for img in img_list:
                #     img_source.append(img.get_attribute('src'))
            try:
                result.append(driver.find_element_by_css_selector('div.info_inner > span.txt').text)
            except:
                result.append(driver.find_element_by_css_selector('span.category').text)
            addrs = driver.find_elements_by_css_selector('ul.list_address span.addr')
            addr_to_latilongti.append(addrs[0])
            add_list = ','.join([ add.text for add in addrs ])
            result.append(add_list)
            result.append(' ')
            result.append(' ')
            try:
                result.append(driver.find_element_by_css_selector('div.biztime').text)
            except:
                result.append("오전10시부터 오후10시까지")
            try:
                result.append(driver.find_element_by_css_selector('div.list_item.list_item_biztel > div.txt').text)
            except:
                result.append('번호없음')
            result_list.append(result)
            # print(result)
            time.sleep(1)
        for _ in range(20):
            driver.back()
            time.sleep(2)

        driver.find_element_by_xpath(f'//*[@id="container"]/div[2]/div[1]/div/div[2]/div/div[2]/a[{i}]').click()
        time.sleep(1)
driver.close()

# driver.get('https://www.google.com/') 위도 경도
# for addrto in addr_to_latilongti:
#     driver.find_element_by_css_selector('input.gLFyf.gsfi').send_keys(addrto).send_keys(Keys.ENTER)

f = open('food.csv', 'w', encoding='utf-8', newline="") # 둘 중에 안 깨지는 거 선택
wr = csv.writer(f)
row = ['r_name', 'r_kind', 'r_img', 'des', 'address', 'Latitude', 'longitude', 'closetime', 'number']
wr.writerow(row)
wr.writerows(result_list)
f.close()

# row = ['r_name', 'r_kind', 'r_img', 'des', 'address', 'Latitude', 'longitude', 'closetime', 'number']
# dataframe = pandas.DataFrame(result_list, columns=row)
# dataframe.to_excel('fooddeug.xlsx', sheet_name='restaurant_list', startrow=0, header=True)
```

> 위도 경도 못해서 망함.

```python
driver.execute_script('location="' + url + '"')
location = "www.ananana" 해당 페이지로 넘어갈 때 쓰는 법.
```

> href속성 값을 스크립트로 실행하는 법. 기존 페이지에서 이동하므로
>
> 새로운 창이 뜨는 걸 방지할 수 있다.