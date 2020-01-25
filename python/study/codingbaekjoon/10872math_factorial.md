```python
n = int(input())
result = 1
for i in range(n, 0, -1):
    result = result * i
print(result)
```

> 간단한 수학 팩토리얼 코드화.

```python
n = int(input())
result = 1

for i in range(1, n+1):
    result *= i
print(result)
```

> 뭐 굳이 range를 거꾸로 돌릴 필요가 없지.

```python
result = 1
for i in range(1, int(input())+1):
    result *= i
print(result)
```

> 오 풀이보니 input이 range함수 안에 들어가도 되구나,,,