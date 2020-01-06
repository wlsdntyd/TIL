```python
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.youtube.com/")

time.sleep(3)	# 3초 후 실행

search = driver.find_element('//*[@id="search"]') # 유튜브 검색창 객체 불러온 코드

search.send_keys('코딩 공부') # 검색창 안에 입력
time.sleep(1)

search.send_keys(Keys.ENTER) # search객체 enter키 입력 
```

> 셀레니움의 아주 기본적인 동작. 할게 많다.

```python
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

num = 1
def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')   # bs4의 findAll과 같은 리스트 형식 반환

    for btn in btns:
        if btn.text == str(num):    # 비교하기 위해 num을 문자열로 변환시켜줌
            btn.click()
            num += 1
            return
while num <= 50:
    clickBtn()
```

> 1에서 50까지 숫자 찾아서 클릭하는 함수.