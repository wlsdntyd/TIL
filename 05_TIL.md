

- 가상 환경 구축
  - python -m venv venv : 'venv'라는 가상 환경 만듬
  - cd venv : 가상 환경 접근
  - source venv/Scripts/activate : 가상 환경 활성화, 'venv'는 가상 환경 이름
  - pip list : 가상 환경 내 라이브러리 목록 출력
  - deactivate : 가상 환경 종료
  - rm -rf  venv/ : 가상 지움
  - pip freeze : 성공적으로 설치됐는지 확인
  - pandas : 가상 환경 라이브러리 필요시 설치
  - pip install requests : requests 설치 (Python에서 HTTP요청을 보내는 라이브러리)
  - pip install beautifulsoup4 : <<설치 html및XML 파일에서 데이터를 쉽게 Parsing 할 수 있는 라이브러리
  - 버전이 낮을 시 python -m pip install --upgrade pip 설치
  - 안되면 vs code로 실행

- **웹 크롤링**

  - request.get(url).text : url주소의 html을 반환

  - BeautifulSoup(request, 'html.parser') : html을 파싱해준다(분석해준다)

  - ```python
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://finance.naver.com/sise/"
    
    #페이지의 html태그를 가져옴
    request = requests.get(url).text
    
    #html을 파싱함
    soup = BeautifulSoup(request, 'html.parser')
    
    #해당 id의 html을 가져옴 > text만 출력
    kospi = soup.select_one("#KOSPI_now")
    print(kospi.text)
    ```

- 미국 달러 환율 출력

```python
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"

req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
# class를 가져와야 할 땐 상위 id를 선택.
# 태그가 길어질 땐 #exchangeList .valse 로 중간에 공백을 넣어 스킵할 수 있다.
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(exchange.text)
```

- 네이버 실시간 검색어

```python
import requests
from bs4 import BeautifulSoup

url="https://www.naver.com"

req = requests.get(url).text
soup= BeautifulSoup(req, 'html.parser')

# soup.select(): 모든 요소를 리스트로 반환
# 위에와 똑같이 '#PM_ID_ct span.ah_k' 중간에 공백을 두어 실행 가능
search=soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

for item in search:
    print(item.text)
```

- pip install flask 
- alt + shift + k
- jinja 
- 내일 텔레그램 챗봇 20