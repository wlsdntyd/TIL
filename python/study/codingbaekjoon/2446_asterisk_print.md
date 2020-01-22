```python
# N(1 ≤ N ≤ 100)
n = int(input())
for i in range(-n+1,n):
    i = abs(i) + 1
    print(" "*(n-i)+"*"*(i*2-1)+" "*(n-i))
```

> 2445번에서 절대값 이용하는게 마음에 들어서 풀었는데 출력이 안맞는다고 한다.
>
> 출력 잘 되는데 왜 그런지 모르겠다. 모래시계 문제.

```python
# N(1 ≤ N ≤ 100)
n = int(input())
for i in range(1,n+1):
    print(" "*(i-1)+"*"*(2*(n-i)+1)+" "*(i-1))
for i in range(1,n):
    print(" "*(n-i-1)+"*"*(2*i+1)+" "*(n-i-1))
```

> 채점이 안되서 다시 풀음,,, 또 잘못된 출력.

```python
# N(1 ≤ N ≤ 100)
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(" ", end="")
    for k in range(2*(n-j)-1):
        print("*", end="")
    for a in range(i):
        print(" ", end="")
    print("")
for i in range(1,n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    for a in range(n-i):
        print(" ", end="")
    print("")
```

> 요것도 잘못된 출력.

```python
# N(1 ≤ N ≤ 100)
n = int(input())
for i in range(1,n+1):
    print(" "*(i-1)+"*"*(2*(n-i)+1))
for i in range(1,n):
    print(" "*(n-i-1)+"*"*(2*i+1))
```

> 정답. 뒤에 공백이 필요없는데 자꾸 공백을 만들어냈다.ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 아 열받아