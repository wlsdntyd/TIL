```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
from tqdm import tqdm
import time
import os
import zipfile

def get_images(keyword):
    print("접속중")
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(30)
	# implicitly_wait: 브라우저 드라이버가 페이지 호출을 해당 시간(초)동안 대기해주는 것.
    url = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}'
    driver.get(url)

    # 페이지 스크롤 다운
    body = driver.find_element_by_css_selector('body')	# html에서 body태그 선택.
    for _ in range(3):	# 필요한 인자가 없다면 _로 써도 된다.
        body.send_keys(Keys.PAGE_DOWN)	# 스크롤 다운 진행 됨.
        time.sleep(1)	# time.sleep()을 안 쓰면 너무 빨라서 다 실행이 안 된다.

    # 이미지 링크 수집
    imgs = driver.find_elements_by_css_selector('img._img')	# img태그의 _img클래스 찾음
    result = []
    for img in tqdm(imgs):  # tqdm: 반복이 완료될 때 까지 0~100%로 표시해줌.
        if 'http' in img.get_attribute('src'):	# 다른 것 까지 불러와 버려서 'http'가 없는
            result.append(img.get_attribute('src'))	# 것 들은 포함시키지 않음.

    driver.close()
    print("수집완료")

    # 폴더 생성
    print("폴더 생성")
    if not os.path.isdir(f'./{keyword}'): # 해당 폴더가 있다면 True 없다면 False
        os.mkdir(f'./{keyword}')	# 폴더가 없으면 not으로 인해 True가 되어 폴더를 생성한다.

    # 다운로드
    print("다운로드")
    for index, link in tqdm(enumerate(result)):
        start = link.rfind('.') # 오른쪽에서 부터 해당 문자를 찾아 인덱스 번호 반환
        end = link.rfind('&')
        filetype = link[start:end]  # '.jpg', '.png' 확장자가 다른 경우를 대비해 적음

        urlretrieve(link, f'./{keyword}/{keyword}{index}{filetype}')
    print("다운로드 완료")

    # 압축 .zip(확장자명) 붙이는 것을 잊지말자.
    zip_file = zipfile.ZipFile(f'./{keyword}.zip', 'w') # 빈 압축파일 생성.

    for image in os.listdir(f'./{keyword}'):    # 해당 폴더에 있는 파일들을 리스트로 묶음.
        print(image, "압축파일에 추가 중")
        zip_file.write(f'./{keyword}/{image}', compress_type=zipfile.ZIP_DEFLATED) #암기
    zip_file.close()
    print("압축 완료")
if __name__ == "__main__":
    keyword = input("수집할 키워드를 입력하세요 : ")
    get_images(keyword)
```

> 검색어를 입력받아 페이지 스크롤 다운을 이용해 더 많은 이미지 다운하기.
>
> tqdm은 참 신기하다. 요긴하게 써먹을 수 있을 거 같다.
>
> 16일 수정. 압축 추가하고 함수로 바꿔서 다른 폴더에서도 불러와서 쓸 수 있게 끔 만들었다.