```python
from selenium import webdriver as wd
driver = wd.Chrome(executable_path='chromedriver.exe')
from selenium.webdriver.common.by import By	# time처럼 명시적 대기를 이용할 때
from selenium.webdriver.support.ui import WebDriverWait	# by,webdriverwait,ec 같이
from selenium.webdriver.support import expected_conditions as EC
import time
driver.get('http://tour.interpark.com')
driver.implicitly_wait(10)
driver.find_element_by_id('SearchGNBText').send_keys('달랏')
driver.find_element_by_css_selector('button.search-btn').click()
WebDriverWait(driver, 10).until( # 명시적 대기 class를 찾을 때까지 10초가 지나도 기다림
 EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
)
driver.find_element_by_css_selector('.oTravelBox .moreBtn').click()

data = []
for page in range(1, 2):
    driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
    time.sleep(2)
    boxItems = driver.find_elements_by_css_selector('.panelZone > .oTravelBox > .boxList > li')
    for li in boxItems:
        dat = dict()
        dat['img'] = li.find_element_by_css_selector('img.img').get_attribute('src')
        dat['link'] = li.find_element_by_css_selector('a').get_attribute('onclick')
        dat['title'] = li.find_element_by_css_selector('h5.proTit').text
        dat['desc'] = li.find_element_by_css_selector('.proSub').text
        dat['price'] = li.find_element_by_css_selector('strong.proPrice').text
        # db.tour.insert_one(dat) 이것도 가능
        data.append(dat)
driver.close()

from pymongo import MongoClient
client = MongoClient(host='localhost', port=27017)
db = client['tour']
db.tour.insert_many(data)
cursor = db.tour.find()
#cursor.rewind() 커서 되감기, 다시 출력 가능.
for data in list(cursor):
    print(data)
```

