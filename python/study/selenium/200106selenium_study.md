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
    global num	# while문 과 같이 쓰기 위해 global로 불러옴
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')   # bs4의 findAll과 같은 리스트 형식 반환

    for btn in btns:
        if btn.text == str(num):    # 비교하기 위해 num을 문자열로 변환시켜줌
            btn.click()
            num += 1	# 전역변수 num의 값이 바뀜.
            return
while num <= 50: # for문에 의해 숫자가 더해져 50번 반복.
    clickBtn()
```

> 1에서 50까지 숫자 찾아서 클릭하는 함수.

```python
a = 5
def sum():
    a = 10		# 수정: 함수 안의 변수는 전역변수와 별개. 전역변수를 불러온게 아님
    return a	# 함수 안에서만 a값이 10 밖으로 나오면 다시 5
print(sum())
def div():
    return a	# 전역 변수 불러온 것으로 5
print(div())
####################
10
5
```

```python
num = 1
def sum():
    global num		# global로 전역변수를 가져오면 값이 바뀜.
    while num < 10:
        num = num + 1
    return num		# 여기서 num값이 10으로 됨
print(sum())
def div():
    global num		# 값이 10인 num을 global로 불러옴
    while num < 20:
        num += 1
    return num		# 고로 반복문으로 전역변수 num값은 20이 됨
print(div())
#######################
10
20
```

> global로 전역변수 값을 바꿔놨으니 두 번째 함수에서 global로 접근을 안해도 num값은 10이 되어있음.