```python
"""
1. 나라장터 쇼핑몰에 들어가서 "작업용의자"로 검색한다.
2. 조건은 등판과 좌판이 "메시" 또는 "망사"여야 하며, "가죽"이 들어있지 않아야 한다. 팔걸이와 머리받침판이 있어야 한다.
    단, 우선구매대상 및 의무구매대상 인증을 받은 제품이어야 한다.
3. 명세서는 엑셀로 작성해놓고, 이미지도 각각 다운받아놓는다.(*한글보고서에 첨부예정)
4. 아래한글 보고서를 작성한다. 끝
5. 파이참에서 선택부분 실행은 ALT + SHIFT + E
"""

import os
from io import BytesIO
from time import sleep
from urllib.request import urlretrieve as download

import pandas as pd
import win32clipboard # !pip install pywin32
import win32com.client as win32
from PIL import Image   # !pip install Pillow
from openpyxl import Workbook # !pip install openpyxl
from selenium import webdriver  # !pip install selenium
from selenium.common.exceptions import *

def execute_script(script):     # 사이트가 느려서 스크립트 실행이 안 될 경우를 대비.
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(0.5)

DOWNLOAD_DIR = r"C:\Users\달려라\Desktop\imgs"
driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://shopping.g2b.go.kr/")
driver.switch_to_frame('sub')

driver.find_element_by_css_selector('input#kwd.srch_txt').send_keys("작업용 의자")
driver.find_element_by_css_selector('input#kwd.srch_txt').submit()
sleep(1)
# javascript실행으로 클릭을 대신 할 수 있다.(동적으로 움직일 시)
execute_script("javascript:attrNmValLink('5611210201', '등판재질',  'ATTR_269556' , '' ); ")

checkbox_list = driver.find_elements_by_css_selector("ul > li > ul.dLst#dLstDiv > li > input[type='checkbox']")
essential_option = ["메시", "망사"]
except_option = "가죽"

# 등판재질 메시 or 망사 not 가죽
for checkbox in checkbox_list:
    parent = checkbox.find_element_by_xpath('./..') # 현재 element에서 상위 element를
    for i in essential_option:						#  찾음 즉 input위에 li태그
        if i in parent.text and except_option not in parent.text:
            checkbox.click()
execute_script("javascript:toSMPPIntgrSrchGoodsList('');")
sleep(1)
# 좌판재질 메시 or 망사 not 가죽
execute_script("javascript:attrNmValLink('5611210201', '좌판재질',  'ATTR_264449' , '' ); ")
checkbox_list = driver.find_elements_by_css_selector("ul > li > ul.dLst#dLstDiv > li > input[type='checkbox']")
for checkbox in checkbox_list:
    parent = checkbox.find_element_by_xpath('./..')
    for i in essential_option:
        if i in parent.text and except_option not in parent.text:
            checkbox.click()
execute_script("javascript:toSMPPIntgrSrchGoodsList('');")
sleep(1)
# 머리받침판부착 유무.
execute_script("javascript:attrNmValLink('5611210201', '머리받침판부착유무',  'ATTR_106171' , '' ); ")
checkbox_list = driver.find_elements_by_css_selector("ul.dLst > li > input[type='checkbox']")
for checkbox in checkbox_list:
    parent = checkbox.find_element_by_xpath("./..")
    if "유" in parent.text:
        checkbox.click()
execute_script("javascript:toSMPPIntgrSrchGoodsList('');")
sleep(1)
# 팔걸이 유무.
execute_script("javascript:attrNmValLink('5611210201', '팔걸이유무',  'ATTR_259429' , '' ); ")
checkbox_list = driver.find_elements_by_css_selector("ul#dLstDiv > li > input[type='checkbox']")
for checkbox in checkbox_list:
    parent = checkbox.find_element_by_xpath("./..")
    if "유" in parent.text:
        checkbox.click()
execute_script("javascript:toSMPPIntgrSrchGoodsList('');")
sleep(1)

# 100개 리스트
driver.find_element_by_css_selector("option[value='100']").click()
sleep(1)
execute_script("javascript:toSMPPIntgrSrchGoodsList('');")

# 우선구매대상
sleep(2)							# 큰 따움표 안에 큰 따움표가 들어가면 에러가 난다.
driver.find_element_by_css_selector("input[id='priorPrdCrtfcCheck']").click()
sleep(1)
execute_script("javascript:toSMPPIntgrSrchGoodsList('');")
```

> 자료 가져오기 전 페이지 완료 상태

```python
# item_list
item_list = driver.find_elements_by_css_selector("tbody > tr > td > a[href^='javascript:toSMPPGoodsDtlInfo(']")
script_list = []

for i in item_list:	# 스크립트 주소 가져와서 리스트에 저장함.
    script = i.get_attribute("href")
    script_list.append(script)
			# r : 역슬래시가 한개일 경우 오류가 날 수 있는데 r을 써서 오류 방지.
filename = r"C:\Users\달려라\Desktop\excel\chair_list.xlsx"   # 엑셀 파일 생성.
book = Workbook()   # openpyxl.Workbook
book.save(filename)	# 저장.

with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:
    writer.book = book
    writer.sheets = {ws.title: ws for ws in book.worksheets}
    
    for idx, script in enumerate(script_list):
        execute_script(script)
        print(idx)
        sleep(1)	# 원하는 값이 [0]에 있고, 행을 열로 써야해서 transpose()해줌
        spec = pd.read_html(driver.page_source, index_col=0)[0].transpose()
        if idx == 0:	# map(자료형or함수, 데이터): 데이터를 함수실행시킨 값으로 바꿔줌.
            spec.columns = map(lambda a: a.replace(" :", ""), spec.columns)
            spec.to_excel(writer, startrow=0, sheet_name='Sheet', index=False)
        else:  # 두 번째부터는 열 제목을 빼고 출력해야되기때문에.
            spec.to_excel(writer, startrow=writer.sheets['Sheet'].max_row, sheet_name='Sheet', index=False, header=False)
        
        img = driver.find_element_by_css_selector('img[src^="http://img.g2b.go.kr:7070/Resource/CataAttach/XezCatalog/XZMOK/"]').get_attribute('scr')
        # 다운로드에서 타입에러가 뜨는데 왜 그런지 모르겠다.
        download(img, os.path.join(DOWNLOAD_DIR, f'{idx}.png'))
    writer.save()
```

> 한글파일에 이미지 저장까지는 해야되서 몇일은 걸릴 듯 싶다.