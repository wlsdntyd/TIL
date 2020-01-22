```python
# N(1 ≤ N ≤ 100)
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    for k in range(2*n-2*j-2):	# ,(콤마)에 한 칸 띄어쓰기가 포함되어있는 듯 하다.
        print(" ", end="")		# +기호로 이으면 -2가 필요가 없다.
    for a in range(i):
        print("*", end="")
    print("")
for i in range(1,n):
    for j in range(n-i):
        print("*", end="")
    for k in range(2*n-2*j-2):
        print(" ", end="")
    for j in range(n-i):
        print("*", end="")
    print("")
```

> 2445번 별찍기 8번 문제. 크,,,,

```python
n = int(input())
for i in range(1,n+1):
    print("*"*i+" "*((n-i)*2)+"*"*i)
for i in range(1, n):
    print("*"*(n-i)+" "*(2*i)+"*"*(n-i))
```

> 감이 좀 생겨서 짧게 구현.

```python
n = int(input())
for i in range(-n+1,n):
    print("*"*(n-abs(i))+" "*(2*abs(i))+"*"*(n-abs(i)))
```

> 절대값 이용해서 더 짧게.