```python
st = input("문자열을 입력하세요 : ")

result = st[0]
count = 1

for i in range(1, len(st)):
    if st[i] == result[-1] and i == len(st) - 1:
        result = result + str(count+1)

    elif st[i] == result[-1]:
        count += 1
        
    else:
        result = result + str(count) + st[i]
        count = 1
print(result)
```

> 문자열 압축 문제. 잘 푼 거 같긴한데 풀이보니 아직 한참멀었다.

```python
s = 'aabcccaaaaass'

result = s[0]
count  = 0

for st in s:
    if st == result[-1]:
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)
print(result)
```

> 풀이에 있던 코드 문자열을 바로 for문으로 돌렸다. 난 왜 멍청하게 굳이 range를 썻지...

```python
st = input("문자열을 입력하세요 : ")

result = st[0]
count = 0

for i in st:
    if i == result[-1]:
        count += 1
    else:
        result = result + str(count) + i
        count = 1
result = result + str(count)
print(result)
```

> 문자열로 다시 풀어봤다. 위에 코드랑 똑같아서 좀 그러네,,,,,,