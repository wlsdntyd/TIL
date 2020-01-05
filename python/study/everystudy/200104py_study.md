```python
import os

def get_txt_list(path):
    set_list = os.listdir(path)
    get_list = []
    for x in set_list:
        if x.endswith('txt'):
            print(x)
get_txt_list('C:\\Users\\달려라\\TIL\\연습')
```

> os 모듈 이용해 텍스트파일 프린트하는 코드.

```python
def Bmi(kg, cm):
    m = cm * 0.01
    bmi = kg / m**2
    print("BMI : %f" % bmi)
    if bmi < 18.5:
        print("마른 체형")
    elif 18.5 <= bmi and bmi < 25.0:
        print("표준")
    elif bmi >= 30.0:
        print("고도 비만")
num = input("사용자의 몸무게와 키를 구분은 콤마로 하여 입력하세요 : ")
kg, cm = num.split(",")
Bmi(int(kg), int(cm))

```

> 비만테스트, 원래는 함수만 표현하면 되지만 그 동안 배운 걸 써먹어봤다. 흠흠 만족

```python
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y
    def get(self):
        result = (self.x,self.y)
        return result
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
        return (self.x, self.y)
po = Point(5,6)
po.setx(10)
po.sety(15)
print(po.get())
print(po.move(10,-5))
```

> 클래스 변수와 인스턴스 변수 각각 접근법과 어떤 식으로 활용하는지 여러번 바꿔보면서 해봤다.

```python
with open('text.txt', 'w') as f:
    for i in range(1,11):
        f.write("%d \n" % i)
```

> 넘나 쉬운 문제.

```python
import os
def print_flist():
    with open('text.txt','wt') as f:
        path = input("경로를 입력하세요 : ")
        list = os.listdir(path)
        for i in list:
            f.write("%s \n" % i)
print_flist()
```

> 경로 입력받아 파일들 입력해주는 코드. 생각이 안나서 정답을 봤다.