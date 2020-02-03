```python
s = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    s.add(i)

for num in range(1, 10001):
    if num not in s:
        print(num)
```

> 셀프넘버 구하는 문제. 재밌다.
>
> 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 
>
> 다음 수는 51 + 5 + 1 = 57이다.