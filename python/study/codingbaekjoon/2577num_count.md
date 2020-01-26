```python
A = int(input())    # >= 100, < 1000 
B = int(input())
C = int(input())

result = str(A*B*C)
for i in range(10):
    print(result.count(str(i)))
```

> 쉽다.