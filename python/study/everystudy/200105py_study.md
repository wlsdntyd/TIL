```python
def sum(a,b):
    print(a+b)
a = sum(5,6)
print(a)

def div(a,b):
    return a / b
b = div(10,5)
#########################
11
None
```

> 지금껏 변수에 함수를 대입한다고 해서 함수가 실행이 되지 않을거라 생각했는데 실행이 된다.
>
> 다만 두 번째 함수는 리턴값에 프린트가 없어서 출력이 되지 않았을 뿐, 실행이 되서 b에 2라는 값이
>
> 들어가 있는 상태이다. **변수에는 함수가 대입이 되는게 아니고 리턴값이 들어가는거다.**
>
> sum함수를 보면 리턴값이 없으므로 a에 들어간 값은 None(거짓)이다.

```python
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
    
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4    # 4개씩 반복되므로 4로 나눠야됨
    num = int(num)

    for i in range(num + 1):
        name = lines[4*i].rstrip('\n')      # 오른쪽에 있는 줄바꿈 문자 지워서 입력시킴
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break

if __name__ == "__main__":
    run()
```

> 주소록 프로젝트. 힘들었다. 솔직히 크게 어려운 부분은 없는 코드지만 이상하게 시간을
>
> 많이 할애했던 코드, 툴을 파이참으로 바꿨는데 비쥬얼보다 좋은 거 같다.

```python
a = [{'s' : 1, 'd' : 2, 'f' : 3},{'s' : 4, 'd' : 5, 'f' : 6}]
print(a)
for i in a:
    print(i['s'])
    print(i['d'])
    print(i['f'])
```

> 당연히 되는 코드지만 헷갈렸던 부분,,,

```python
import win32com.client

explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True
```

> 인터넷 익스폴로어 창 여는 코드, 신기하다.

```python
class Parent:
    house = "yong-san"
    def __init__(self):
        self.money = 10000

class Child1(Parent):
    def __init__(self):
        super().__init__()
        pass

class Child2(Parent):
    def __init__(self):
        pass

child1 = Child1()
child2 = Child2()

print('Child1', dir(child1))
print('Child2', dir(child2))
```

> 클래스 변수는 부모 클래스를 상속받은 자식 클래스에는 존재하지만 인스턴스 변수(self.money)는
>
> super()._init__() (부모클래스의 생성자 메서드를 호출)을 쓰지 않으면 가져올 수 없다.

```python
from bs4 import BeautifulSoup as bs
from pprint import pprint	# print보다 심플하게 보여주는 함수
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
soup = bs(html.text, 'html.parser')
data1 = soup.find('div',{'class':'detail_box'})	# find함수: 하나만 찾아줌.
data2 = data1.findAll('dd')	# finAll함수: 다 찾아줌. 리스트 형식 반환
pprint(data2[0])	# 리스트 형식이여서 첫번째 데이타를 가져올 수 있음.
```

> dd태그가 많을 때 어떻게 접근할지 몰랐는데 깔끔하게 정리되서 좋다.