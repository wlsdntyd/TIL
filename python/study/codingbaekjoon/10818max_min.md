```python
import sys

nums = int(input())
num_list = sys.stdin.readline().split()
num_list = list(map(int, num_list))
print(max(num_list),min(num_list))
```

> 출력은 알맞은데 오답.

```python
import sys

nums = int(input())
num_list = sys.stdin.readline().split()
num_list = list(map(int, num_list))
min = 1000000	# min은 함수명이랑 동일해서 웬만해선 같게 쓰지 않는게 좋다.
max = -1000000	# max도 동일.
for i in range(nums):
    if num_list[i] <= min:
        min = num_list[i]
    if num_list[i] >= max:
        max = num_list[i] 
print(min,max)
```

> 어려운 문제같진 않은데 시간을 꽤나 쓰게 만든 문제. 그래도 풀었으니,,,