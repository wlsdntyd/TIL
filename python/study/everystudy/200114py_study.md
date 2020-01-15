```python
import pickle
with open('C:\dev\\test1.bin', 'wb') as f:
    list1 = ['1', 2, 3, 4, 5]
    pickle.dump(list1,f)
#     f.write(bytes(list1))
```

```python
with open('C:\dev\\test1.bin', 'rb') as f:
    result = pickle.load(f)
    print(result)
```

> 바이너리 모드를 통한 문자열 데이터 저장 및 불러오기

```python
with open('C:\dev\\text.txt', 'rt') as f:
    while True:
        data = f.readline()
        if not data:
            break
        print(data, end="")	# 줄 바꿈 문자열을 포함하고 있으므로 end를 쓴다
```

```python
class Car:
    # list1 = [] <<< car1 인스턴스와 car2 인스턴스가 겹쳐지면 오류나서 클래스 변수에는 적지 않음
    def __init__(self):
        self.list1 = []
    def add_option(self, option):
        self.list1.append(option)
    def show_option(self):
        return self.list1
car1 = Car()
car2 = Car()
car1.add_option('전동 트렁크')
car1.add_option('통풍 시트')
car2.add_option('뒷자리 에어백')
car2.add_option('하이패스')
print(car1.show_option())
print(car2.show_option())
```

> car1, car2가 둘 다 전역변수를 쓰게 되면 값이 중복되어져서 생성자 함수 안에 적어야한다.

```python
class Pizza:
    def __init__(self):
        self.result = []
    def add_topping(self, topping):
        self.result.append(topping)	# self.result += [topping] 이렇게 적어도 된다.
    def remove(self,topping):
        if topping in self.result:
            self.result.remove(topping)
    def show_topping(self):
        return self.result
p1 = Pizza()
p1.add_topping('치즈')
p1.add_topping('베이컨')
p1.add_topping('고구마')
p2 = Pizza()
p2.add_topping('소시지')
p2.add_topping('불고기')
p2.add_topping('피망')
p2.remove('소시지')
print(p1.show_topping())
print(p2.show_topping())
```

```python
import random
class EachSum:
    def __init__(self):
        self.total = 0
    def compute(self, num):
        while True:
            s = num % 10	# self.total += num % 10 깔끔
            num = num // 10
            self.total += s
            if num == 0:
                break
        return self.total
each = EachSum()
total = each.compute(12345)
print('합계', total)
```

```python
import random
class SelectMenu:
    def __init__(self, lists):
        self.lists = lists      
    def get_menu(self):
        num = random.randint(0, 3)	# randint(0,len(self.lists))
        result = self.lists[num]
        return result
menu = SelectMenu(['짬뽕', '초밥', '쌀국수', '주꾸미'])
print(menu.get_menu())
```

```python
with open('document.txt', 'rt') as f:
    texts = f.read()
texts = texts.replace("\n", " ")
texts = texts.split(" ")  # 반환 값이 리스트 형식이다.
result = {}
for text in texts:
    num = texts.count(text)
    result[text] = num
    while True:
        if text in texts:
            texts.remove(text)
        else:
            break
print(result)
```

> 강의 시간에 내주신 문제. 다른 방식으로 접근하려는데 머리만 아프다.

```python
import operator

with open('document.txt', 'rt') as f:
    texts = f.read()
texts = texts.replace("\n", " ")
texts = texts.split(" ")  # 반환 값이 리스트 형식이다.
result = {} # = dic()
for text in texts:
    if text in result:
        result[text] = result[text] + 1	# 반복하면서 같은 단어가 있을 때 마다 1씩 증가
    else:
        result[text] = 1	# 같은 단어가 없다면 그냥 1
result_list = sorted(result.items(), key = operator.itemgetter(1), reverse = True)
result_list = list(result_list)
print(result_list[:5])
```

> 