```python
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import pandas as pd

# options = Options()
# options.add_argument('--start-fullscreen')  # 전체화면 띄우기
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com/maps/')
driver.implicitly_wait(10)

f = pd.read_csv('food.csv')
# while True:   해당 위치 좌표 찾기
#     print(pyautogui.position())
pointer = (1164,569)
Latitude = []
longitude = []
for i in range(300):
    driver.find_element_by_css_selector('div.gstl_50.sbib_a > div.sbib_b > div#gs_lc50 > input#searchboxinput').clear()
    time.sleep(1)
    driver.find_element_by_css_selector('div.gstl_50.sbib_a > div.sbib_b > div#gs_lc50 > input#searchboxinput').send_keys(f.iloc[i,4].split(',')[0])
    time.sleep(1)
    driver.find_element_by_css_selector('div.gstl_50.sbib_a > div.sbib_b > div#gs_lc50 > input#searchboxinput').send_keys(Keys.ENTER)
    time.sleep(5)
    pyautogui.click(pointer,button='right')
    time.sleep(1)
    driver.find_element_by_css_selector('div.action-menu-entry:nth-of-type(3)').click()
    time.sleep(2)
    Latitude.append(driver.find_element_by_css_selector('div.widget-reveal-card-container > button.link-like').text.split(", ")[0])
    longitude.append(driver.find_element_by_css_selector('div.widget-reveal-card-container > button.link-like').text.split(", ")[1])
    time.sleep(2)
driver.close()

for i in range(300):
    f.iloc[i,0] = f.iloc[i,0] + '+' + str(i+1)  # 이름 바꾸기
    urlretrieve(f.iloc[i,2], f'./imgs/{i+1}.png')   # 이미지 다운
    f.iloc[i,2] = f"./imgs/{i+1}.png"   # r_img에 경로 저장

f['id'] = [ i for i in range(1,301) ]
f['Latitude'] = Latitude
f['longitude'] = longitude
f = f[['id','r_name','r_kind','r_img','des','address','Latitude','longitude','closetime','number']]
f.to_csv('./food_oneimg.csv', header=True, index=False)
```

> 힘들게 구현한 구글 지도에서 위도, 경도 따오기. + 이미지 다운 및 열 값 변경