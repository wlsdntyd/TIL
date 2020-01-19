```python
def nums_sum(num):
    sums = 0
    while num:
        sums += num
        num -= 1
    print(sums)

num = int(input())
nums_sum(num)
```

> range 말고 for문 말고 진짜 간단하게 짜보고 싶어서 만들어 본 num까지의 숫자 합 코드.