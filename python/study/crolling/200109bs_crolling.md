```python
import requests
from bs4 import BeautifulSoup
# 특정 url에 접속하는 요청(request)객체를 생성.
request = requests.get("http://www.dowellcomputer.com/main.jsp")

# 접속한 이후의 웹 사이트 소스코드 추출.
html = request.text

# html 소스코드를 파이선 객체로 변환. beautifulsoup
soup = BeautifulSoup(html,'html.parser')
links = soup.select('td > a')	# 늘 말하지만 리스트 형식 반환.

for link in links:
    if link.has_attr('href'):   # 속성 값 href를 가지고 있는 객체들을 가져옴.iterable
        if link.get('href').find('notice') != -1:
            print(link.text)
```

> get('속성').find('해당 속성의 텍스트') 함수는 해당 텍스트를 포함하지 않고 있다면 -1을 반환하기에
>
> (!= -1) -1이 아니라면을 사용했다. 

```python
from bs4 import BeautifulSoup
import requests

class Conversation:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
    def __str__(self):	# 인스턴스 객체를 print할 때 문자열을 출력해주는 메서드?인 듯 하다.
        return "질문: " + self.question + "\n답변: " + self.answer + "\n"
    
def get_subjects():
    subjects = []
    url = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = url.text
    soup = BeautifulSoup(html,'html.parser')
    divs = soup.findAll('div', {'class' : 'thrv_wrapper thrv_text_element'})# 오타주의
    for div in divs:
        links = div.findAll('a')
        for link in links:
            subject = link.text
            subjects.append(subject)
    return subjects
    
subjects = get_subjects()
print("총 ", len(subjects), "개의 주제를 찾았습니다.")
print(subjects)
```

```python
conversations = []
i = 1

for sub in subjects:
    print('(', i, '/', len(subjects), ')', sub)
    req = requests.get("https://basicenglishspeaking.com/" + subjects[0])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    qnas = soup.findAll('div', {"class": "sc_player_container1"})
    
    for qna in qnas:
        if qnas.index(qna) % 2 == 0:
            q = qna.next_sibling	# 다음 형제 찾기(부모나 자식은 안됨)
        else:						# div태그가 끝나고 텍스트가 있어서 사용하게 
            a = qna.next_sibling
            c = Conversation(q, a)
            conversations.append(c)
    else:
        for c in conversations:		# for else 배운 거 적용해봄. 잘 출력된다.
            print(str(c))
        
    i += 1
    
    if i == 10:
        break
print("총 ", len(conversations), "개의 대화를 찾았습니다.")
```

> 저번에 한 번 했던 거지만 이번엔 최대한 스스로 문제를 해결했다. 대화 출력이 한번에 이루어지는게 
>
> 보기 싫어서 for else문을 잘 이용해봤다.

```python
from bs4 import BeautifulSoup as bs
import requests

MEMBER_DATA = {
    'memberID' : 'wlsdntyd',
    'memberPassword' : '123123'
}

with requests.Session() as s:	# session 클라이언트와 서버 사이 링크가 설정되는 것.
    request = s.post('http://dowellcomputer.com/member/memberLoginAction.jsp', data=MEMBER_DATA)

print(request.text)
```

```python
request = s.get('http://dowellcomputer.com/member/memberUpdateForm.jsp?ID=wlsdntyd')
soup = bs(request.text, 'html.parser')
result = soup.findAll('input', {"name" : "memberEmail"})	# find로 접근하는게 더 낫다.
Email = result[0].get('value')	# findAll은 iterable 형식이라 인덱스 번호로 접근해야한다.
print(Email)
```

> 위에 코드는 로그인이 잘 이루어지나 확인하는 거고 밑에는 정보 페이지에서 본인 이메일 주소를 크롤링
>
> 해오는 코드다. session 링크가 설정된다고 적어놨는데 필요한 자원을 하나로 모을 수 있는 연결이라 한다.
>
> post방식으로 정보를 보내고 s.get은 s에 requests.Sesson()정보가 담겨 있어 get만 쓴 거 같다.
>
> findAll로 불러오면 iterable형식이라는 것과 이에 접근할 땐 인덱스 번호로 접근해야한다는 것을 알아두자.