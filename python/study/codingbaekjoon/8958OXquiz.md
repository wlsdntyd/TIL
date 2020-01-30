```python
n = int(input())

result = 0
num = 0

for _ in range(n):
    st = input("O,X 입력: ")
    for j in st:
        if j == "O":
            num += 1
        elif j == "X":
            for k in range(1, num+1):
                result += k
            num = 0
    if st[-1] == "O":
        for k in range(1, num+1):
            result += k
    print(result)
```

> "OOOXXXOOXO" O의 개수만큼 1+2+3 + 1+2 + 1 을 구하는 문제.
>
> 열심히 풀었는데 출력 초과 오류뜬다.