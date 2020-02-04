```python
N = int(input())    # 1보다 크고 1000보다 작거나 같다.

count = 0
for i in range(1, N+1):
    try:
        s = str(i)
        f = int(s[0])
        c = int(s[1])
        t = int(s[2])
    except:
        pass
    if i < 100:
        count += 1
    elif i >= 100 and f - c == c - t:
        count += 1
print(count)
```

> 주어진 숫자 밑 범위에서 한수의 개수 출력하는 문제.
>
> 한수 : 각 자리수의 차(공차)가 등차수열을 이루는 숫자.
>
> 한수에는 1~99는 무조건 포함된다.