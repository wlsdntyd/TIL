```python
n = int(input())

for _ in range(n):
    num = 0
    result = 0
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
> 초기화를 제대로 안 해줘서 삽질 좀 했다. 그래도 잘 풀었으니 만족.