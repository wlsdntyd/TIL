```python
for i in range(5):
    print("*", end = "")
```

> 알고리즘 들어가기 전 연습문제 푸는 중.

```python
for j in range(5):
    for i in range(5):
        print("*", end = "")
    print("")
```

> 별(*) 다섯 개씩 다섯 줄 출력 코드. 이젠 눈 감고 푼다.

```python
for i in range(1,6):
    print("*" * i)
```

> 내려가면서 별을 하나에서 다섯개까지 출력하는 코드. 껌이다.

```python
i = 5
while i > 0:
    print("*" * i)
    i -= 1
```

> 내려가면서 증가, 여기서도 for문을 사용하려했는데 생각이 안났다.

```python
i = 1
j = 4
while i < 6 and j >= 0:
    print(" " * j + "*" * i)
    i += 1
    j -= 1
```

> 오른쪽 정렬, 내려갈수록 길어지는 코드. 스스로 푼거긴 한데 이렇게 풀어도 되는지는 모르겠다.
>
> 좀 더 효율적인 방법은 없을까

```python
i = 0
j = 5
while i < 5 and j > 0:
    print(" " * i + "*" * j)
    i += 1
    j -= 1
```

> 쉽다 쉬워

```python
i = 1
k = 4
for j in range(10):
    if i % 2 == 1 and i < 10:
        print(" " * k + "*" * i)
        i += 1
        k -= 1
    else:
        i += 1
```

> 트리(삼각형) 형식 출력, 요건 오분정도 걸린듯. 스스로 했다는 거에 만족하자.

```python
i = 10
k = 0
for j in range(10):
    if i % 2 == 1 and i > 0:
        print(" " * k + "*" * i)
        i -= 1
        k += 1
    else:
        i -= 1
```

> 역삼각형 출력, 위에 거에서 조금만 바꾸면 된다.

```python
apart = [[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]
arrears = [101, 203, 301, 404]

for i in range(4):
    for j in range(4):
        if apart[i][j] not in arrears:
            print(f"{apart[i][j]}호에 신문이 배달되었습니다.")
```

> 일부 세대 제외 신문 배달 코드. 와 푸는데 좀 오래 걸렸다. 처음엔 막 쓰다가 안되서 종이에 틀을 갖추고
>
> 코드를 짜니 할만했다. 스스로 해낸게 짜릿하다.

```python
for j in range(5):
	for i in range(j):
		print(' ', end = '')
    for i in range(2*(5-j)-1):
    	print('*', end = '')
    print("")
```

> 역삼각형 출력 정답지. 코드 분석 해보니 확실히 잘 짜여져있다. 저런 계산들을 한다는게 신기하다.