- python

  - input 함수

  - 가상 

    - python -m venv venv
    - source venv/scripts/activate
    - pip list
    - deactivate
    - rm -rf  venv/
    - pip freeze > requirements.txt
    - pip install -r requirements.txt
    - pandas
    - pip install requests
    - pip list
    - pip install beautifulsoup4
      - 버전이 낮을 시 python -m pip install --upgrade pip 설치
      - 안되면 vs code로 실행
    - 코스피 지수 출력

    ```python
    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://finance.naver.com/sise/'
    
    # request = requests.get(url)
    request = requests.get(url).text
    
    soup = BeautifulSoup(request, 'html.parser')
    kospi = soup.select_one("#KOSPI_now")
    # print(soup)
    print(kospi.text) # 코스피 지수 숫자만 출력
    ```

    - 미국 달러 환율 출력

  ```python
  import requests
  from bs4 import BeautifulSoup
  
  url = "https://finance.naver.com/marketindex/"
  
  req = requests.get(url).text
  soup = BeautifulSoup(req, 'html.parser')
  exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
  print(exchange.text)
  ```

  