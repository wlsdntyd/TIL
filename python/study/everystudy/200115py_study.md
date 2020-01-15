```python
try: ... 

except: ... 

else: ....		# try문이 정상적으로 다 실행되면 실행, for else 문과 똑같다
```

```python
def distance(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return dx, dy
start = (1, 1)
end = (5, 3)
dx, dy = distance(start, end)
print('dx:', dx, 'dy:', dy)
```

> 간단한 문제인데 못 풀었다

dir(set) >> set 자료형에 대한 함수들이 출력된다.

```python
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
char_dict = {}
for idx, elem in enumerate(char_list):
    char_dict[idx+1] = elem
print(char_dict)
```

```python
num_list = range(1, 21)
list(filter( lambda x: x % 3 != 0, num_list))
```

> filter map 처리하는 방식이 비슷하다.

```python
hexa_string1 = '48 45 4C 4C 4F'
hexa_string2 = '47 47 4F 52 45 42'
def show_hex_to_ch(hexa_string):
    hexa_list = hexa_string.split(" ")
    for hexa in hexa_list:
        print(chr(int(hexa, 16)), end="")
    print()

show_hex_to_ch(hexa_string1)
show_hex_to_ch(hexa_string2)
```

```python
t = time.time() + (100 * 24 * 60 * 60)
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
```

> 현재부터 100일이 지난 뒤 시간