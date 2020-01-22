```python
#10 ~ 1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기

result = list()
for i in range(10, 1001):
    num = 1
    for j in str(i):
        num *= int(j)
    result.append(num)
print(sum(result))	# sum함수가 있으니 밑에는 필요가 없다.

# sums = 0
# for n in result:
#     sums += n
# print(sums)
```

```python
print(eval('+'.join('*'.join(str(x)) for x in range(10, 1001))))
```

> 코딩도장 문제. 두 번째 코드는 맨 처음 x를 리스트로 받지않고 join함수로 중간에 *곱하기를 넣고
>
> +를 넣어줌으로서 eval함수로 계산을 마쳤다.
>
> eval : 문자열로 표시된 산수의 연산값 리턴하는 함수.

```python
names = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'

name_list = names.split(',')
kim_num = 0
lee_num = 0
jaeyoung_num = 0

for name in name_list:
    if name[0] == '김':
        kim_num += 1
    elif name[0] == '이':
        lee_num += 1
for name in name_list:
    if name == '이재영':
        jaeyoung_num += 1

distinct_name = set(name_list)
distinct_name = sorted(distinct_name)
print(distinct_name)
print(f"김씨의 개수는 : {kim_num} 이씨의 개수는 : {lee_num} 이재영의 개수는 : {jaeyoung_num}")
```

> 직접 풀어서 좋긴한데 너무 허접하다.

```python
names = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'
name_list = names.split(',')

one_name = [name[0] for name in name_list]
#1
print("김씨 성 개수: %d 이씨 성 개수: %d" % (one_name.count("김"), one_name.count("이")))
#2
print("이재영 이름 개수 : %d" % name_list.count("이재영"))
#3
print(sorted(set(name_list)))
```

> count와 리스트 형식을 참고하고 다시 풀어봤다. 앞으로는 코드 수를 줄여봐야겠다.

```python
#0~9까지의 문자로 된 숫자를 입력 받았을 때
#0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.
nums = input()
for i in range(10):
    if nums.count(str(i)) == 1:
        continue
    else:
        print("False")
        break
else:
    print("True")
```

> 코딩도장에 있던 문제 깔끔~~하게 푼 거 같다. 남들은 sort해서 풀었던데 뭐 방법은 많으니.