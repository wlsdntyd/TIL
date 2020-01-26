```python
result = []
for _ in range(10):
    num = int(input())
    result.append(num%42)

for i in result:
    while result.count(i) > 1:
        result.remove(i)
print(len(result))
```

> 리스트 형식이라 직접 중복제거.

```python
result = set()

for _ in range(10):
    num = int(input())
    result.add(num%42)
print(len(result))
```

> set자료형으로 더 깔끔하게 코드화.