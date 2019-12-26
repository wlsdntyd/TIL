import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

# request = requests.get(url)
request = requests.get(url).text

soup = BeautifulSoup(request, 'html.parser')
kospi = soup.select_one("#KOSPI_now")
# print(soup)
print(kospi.text)