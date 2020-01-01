```python
class Math:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result

    def sub(self,num):
        self.result -= num
        return self.result

    def mul(self,num):
        self.result *= num
        return self.result

    def div(self,num):
        self.result /= num
        self.result = int(self.result)
        return self.result

    def sum(self):
        return print(self.result)
calculator = Math()
while True:
    cal = input("덧셈:+ ,빼기:-, 곱하기:*, 나누기:/ 중 에 입력하시오: ")
    if cal == "+":
        num = int(input("숫자를 입력하세요: "))
        calculator.add(num)
        calculator.sum()
    elif cal == "-":
        num = int(input("숫자를 입력하세요: "))
        calculator.sub(num)
        calculator.sum()
    elif cal == "*":
        num = int(input("숫자를 입력하세요: "))
        calculator.mul(num)
        calculator.sum()
    elif cal == "/":
        num = int(input("숫자를 입력하세요: "))
        calculator.div(num)
        calculator.sum()
    else:
        break
```

> 혼자서 만들어 본 계산기. 재밌다. 클래스에 익숙해지려고 일부러 한 번 만들어봤다.
>
> 여기는 혼자 만들어 본 코드만 올려봐야겠다.