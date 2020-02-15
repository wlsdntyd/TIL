```python
a, b = input().split()

a = int(a[2] + a[1] + a[0])
b = int(b[2] + b[1] + b[0])
if a > b:
    print(a)
else:
    print(b)
```

```python
a, b = input().split()

def reverse(k):
    k = k[::-1]
    return int(k)

print(max(reverse(a), reverse(b)))
```

```python
print(max([int(i[::-1]) for i in input().split()]))
```

> 인덱스를 활용하니 편안하다.