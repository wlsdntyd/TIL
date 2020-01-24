```python
A,B,C = map(int, input().split())	# map으로 정수형으로 바꿔주니 정답이네,,

if A >= B and A <= C:
    print(A)
elif A >= C and A <= B:
    print(A)
elif B >= A and B <= C:
    print(B)
elif B >= C and B <= A:
    print(B)
elif C >= A and C <= B:
    print(C)
elif C >= B and C <= A:
    print(C)
```

> 세 개의 숫자 주어졌을 때 중간 값 출력하는 문제. 노가다로 풀긴했지만 그래도 알맞게 출력되는데
>
> 틀렸다고 나온다. map으로 정수형으로 바꿔주니 정답,,,