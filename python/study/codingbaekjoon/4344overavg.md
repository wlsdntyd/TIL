```python
C = int(input())

for _ in range(C):
    N = list(map(int, input().split()))
    student_num = N[0]
    score_list = N[1:]
    A = sum(score_list) / student_num
    over_num = 0
    for score in score_list:
        if score >= A:
            over_num += 1
    S = round(over_num / student_num * 100, 3)
    print(str(S) + '%')
```

> 4344번 문제  왜 틀렸는지 모르겠다. 시간이 넉넉하지 않아서 패스,,,