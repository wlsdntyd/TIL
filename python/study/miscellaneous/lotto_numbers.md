```python
import random

def lotto(num):
    for _ in range(num):
        result = set()
        while len(result) < 6:
            number = random.randint(1,45)
            result.add(number)
        result = sorted(result)
        print(result)

if __name__ == '__main__':
    num = int(input("출력할 로또 개수를 입력하세요 : "))
    lotto(num)
```

> set 말고 list로 하려다 조건이 까다로워 시간 많이 날려먹음. 요게 깔끔하네.

```python
import random

num = int(input())
for _ in range(num):
    print(random.sample(range(1,46),6))
```

> random 과 sample 를 이용한 로또번호 뽑기. 완전 간단.