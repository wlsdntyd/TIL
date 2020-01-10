```python
x = input("숫자를 입력하세요 구분자는 쉼표: ")
x = x.split(",")
x = list(x)
n = len(x)

if n % 2 == 1:
    result = x[int((n-1)/2)]
    print(result)
elif n % 2 == 0:
    num = x[int(n / 2)]
    numi = x[int(n / 2 - 1)]
    result = (int(num) + int(numi)) / 2
    print(result)
```

> 코딩도장에서 풀어 본 문제. 리스트 갯수가 홀수면 가운데 값 출력 짝수면 양쪽 평균 출력.