```python
from selenium import webdriver as wd
driver = wd.Chrome(executable_path='chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver.get('http://tour.interpark.com')
driver.implicitly_wait(10)
driver.find_element_by_id('SearchGNBText').send_keys('달랏')
driver.find_element_by_css_selector('button.search-btn').click()
WebDriverWait(driver, 10).until(
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
        data.append(dat)
        # db.tour.insert_one(dat) 이렇게 해도 된다.
driver.close()
```

```python
from pymongo import MongoClient
client = MongoClient(host='localhost', port=27017)
db = client['tour']
db.tour.insert_many(data)
cursor = db.tour.find()
for data in list(cursor):
    print(data)
```

> mongo는 cursor의 위치가 메모리에 저장되기에 한번 값을 출력하고 다시 실행하면 값이 안나온다.
>
> 그럴때엔 cursor.rewind() 를 사용하면 다시 출력된다.