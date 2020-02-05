```python
s = input()		#1157
s = s.upper()
t = set(s)
s_list = list()
t_list = list()

for i in t:
    t_list.append(s.count(i))

for i in s:
    s_list.append(s.count(i))

if t_list.count(max(t_list)) > 1:
    print("?")
else:
    print(s[s_list.index(max(s_list))])
```

> 열심히 풀었으나 시간초과. 출력은 알맞게 나온다.