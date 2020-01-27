```python
n = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)
sum_score = sum(score_list)
print(round(sum_score / max_score * 100 / n, 6))
```

> 이 문제는 코딩보단 수학적 개념이 있는지 보는 문제같다. 쉽다.