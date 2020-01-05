import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

req = requests.get(url).text
data = BeautifulSoup(req, 'html.parser')
sel = '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k'
search = data.select(sel)

for item in search:
    print(item.text)
