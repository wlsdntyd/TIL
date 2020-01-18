```python
from selenium import webdriver
import time
import pandas as pd
from datetime import datetime

def get_replys(url,imp_time=5,delay_time=0.5):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(imp_time)
    driver.get(url)

    driver.find_element_by_class_name('u_cbox_btn_view_comment').click()
    time.sleep(1)
    while True:
        try:
            driver.find_element_by_class_name('u_cbox_btn_more').click()
            time.sleep(delay_time)
        except:
            break
    print("end")

    contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    # for content in contents:
    #     content = driver.find_element_by_class_name('u_cbox_contents')
    #     print(content.text)
    contents = [content.text for content in contents]

    nicks = driver.find_elements_by_css_selector('span.u_cbox_nick')
    # for nick in nicks:
    #     print(nick.text)
    nicks = [nick.text for nick in nicks]

    dates = driver.find_elements_by_css_selector('span.u_cbox_date')
    # for date in dates:
    #     print(date.text)
    dates = [date.text for date in dates]
    boxs = list(zip(nicks, dates, contents))
    # for box in boxs:
    #     print(box,"\n")
    driver.quit()   # close와 달리 아예 종료시킴.
    return boxs

if __name__ == "__main__":
    start = datetime.now()
    url = 'https://n.news.naver.com/article/001/0011343260'
    reply_data = get_replys(url)

    col = [ '작성자', '날짜', '내용']
    data_frame = pd.DataFrame(reply_data, columns=col)  # dataframe은 행렬, 엑셀의 시트 같은 개념.
    data_frame.to_excel('news.xlsx', sheet_name='한국인 실종4명', startrow=0, header=True)
    end = datetime.now()
    print(end - start)
```

> 대량의 댓글 크롤링 in 뉴스, pandas를 이용하여 엑셀형식으로 저장까지 한다.