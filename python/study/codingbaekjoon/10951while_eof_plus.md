```python
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
    except:
        break
    print(A + B)
```

> sys를 이용한 무한 입력 덧셈,,

```python
result = []
for _ in range(5):
    nums = input().split()
    result.append(nums)
for i in range(len(result)):
    print(sum(map(int, result[i])))
```

> 나름 구현해봤지만 위에 거가 정답. EOF에 대해 알아보라는데 End Of File 의 약자이고,
>
> 텍스트 파일의 끝임을 알리기 위한 문자 값이라는 거 밖에 모르겠다.