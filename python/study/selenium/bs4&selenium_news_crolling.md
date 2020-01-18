```python
from selenium import webdriver
import time
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

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

    html = driver.page_source
    print(html)
    soup = BeautifulSoup(html, 'lxml') # html.parser 보다 속도가 빠름

    contents = soup.select('span.u_cbox_contents')
    contents = [content.text for content in contents]

    nicks = soup.select('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]

    dates = soup.select('span.u_cbox_date')
    dates = [date.text for date in dates]

    replys = list(zip(nicks, dates, contents))

    driver.quit()
    return replys

if __name__ == "__main__":
    start = datetime.now()
    url = 'https://n.news.naver.com/article/001/0011343260'
    reply_data = get_replys(url)

    col = [ '작성자', '날짜', '내용']
    data_frame = pd.DataFrame(reply_data, columns=col)
    data_frame.to_excel('news.xlsx', sheet_name='한국인 실종4명', startrow=0, header=True)
    end = datetime.now()
    print(end - start)
```

> seleniun 과 bs4를 이용한 속도개선 크롤링, 
>
> 댓글 대충 8천개 이상 넘어가는 것을 selenium만으로 크롤링해오려면 40분이 넘어간다.
>
> bs4와 연동시켜 5분으로 속도를 크게 줄였다. 
>
> 데이터를 수집해 올 때는 bs4에서 파싱할 때 html보다 lxml로 파싱하면 속도가 훨씬 빨라진다.