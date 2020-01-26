```python
n = int(input())

def fiv(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fiv(n-2) + fiv(n-1)
print(fiv(n))
```

> 재귀함수를 이용한 합구하기. n = 5 라면 fiv(3)과 fiv(4)를 구하기 위해 fiv함수에 4가 들어가고 반복하게 된다.