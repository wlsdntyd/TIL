## 조건문

```java
if(x > y) {
	System.out.println("x가 크다")
}else if(x < y) {
	System.out.println("y가 크다")
}else {
	System.out.println("x와 y가 같다")
}

if(true)	// 중괄호가 없을 땐 첫 문장만 실행된다.
	System.out.println("true")
System.out.println("false")	// 중괄호가 없으므로 if문 안에서 실행되는게 아님.
```

```java
A ^ B; >> A, B 둘 중에 하나라도 true면 true, 둘 다 같은 경우 false
```

## 삼항연산자

```java
int b1 = (5>4) ? 100:70;	// true라면 100 false라면 70
```

## switch문

```java
String a = "java"

switch(a) {
	case "c":
		System.out.println("c")
        break;						// break가 없으면 해당하는 case부터 맨 아래까지 다 실행된다.
	case "c++":
		System.out.println("c++")
        break;
	case "python":
		System.out.println("python")
        break;
	case "java":
		System.out.println("java")
        break;
	default:						// 위 case조건을 만족하는 경우가 없다면 실행.
		System.out.println("It is what language?")
}
```

> break가 없는 경우 그 밑 case는 다 실행된다는 것을 알아두자.

```java
int a = 7	// 여름
String season = ""
switch(a) {
	case (1):
	case (2):
	case (3):
		season = "겨울"
}
```

> case 하나 하나마다 안 적고 효율적으로 처리하는 법.

## while 문

```java
int total = 0;
int i = 1;
while(i < 100) {
	System.out.println(total);
	total += i
	i++;
}
```

```java
int num = 1;
while(true) {
	num *= 2
	if(num > 500) {
        System.out.println(num)
        break;
    }
}
```

```java
int value = 0;
Scanner scan = new Scanner(System.in);

do{						// do는 무조건 한번은 실행되는 구문. 반복 조건 일치 시 계속 실행.
	value = scan.nextInt();	// nextInt는 정수값을 입력받아서 반환해줌.
	System.out.println("입력받은 수는 " + value + "입니다");
}while(value != 10);	// value가 10일 경우 반복 중단. 10이 아닐 경우 반복
```

> java에서의 while 쓰는 법

## for 문

```java
public class ForExam {
	public static void main(String[] args) {
		int total = 0;
		for(int i = 0; i <= 100; i++){
			if(i % 2 != 0){		// 나머지가 0이 아닌 경우 즉 홀수인 경우 실행됨.
				continue;		// continue문장을 만나면 for문 처음으로 돌아감.
			}					// 따라서 total에 i값이 안 더해짐.
			total += i;			// i가 짝수일 때만 total에 더해짐.
		}						// 중간에 빠져나오고 싶다면 break문을 활용하면 됨.
		System.out.println(total);
	}
}
```

