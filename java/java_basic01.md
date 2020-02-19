## 변수

```java
int a;
String b;
a = 1;
b = "hello java";
--------------------
int a = 1;
String b = "hello java"
double circleArea;
```

> 변수 사용하는 법. & 변수명이 두 단어 이상일 땐 뒷 단어 첫 문자를 대문자로 하는 것이 좋다.

```java
class Animal {
	......
}
Animal cat;
```

> Animal 이라는 클래스를 만들고 Animal 자료형 변수 cat을 생성.
>
> cat 변수에는 Animal 자료형에 해당되는 값만 담을 수 있다.

```java
final int J;
J = 10;
-------
J = 5; // 에러.
```

> 상수(변하지않는 값)를 사용할 때는 final을 변수 타입 앞에 붙여준다. 상수 데이터는 대분자로 표기하는
>
> 것이 관례.  처음 값이 주어지면 다시 초기화할 수 없다.

## 주석

```java
/*
프로그램의 저작권
이 프로그램의 저작권은 홍길동에게 있습니다.
*/
public class Myprogram {
	......
}
```

> 블록 주석 처리 방법.

```java
int age; // 동물의 나이
```

> 라인 주석 처리 방법.
>
> 이클립스에서 주석처리할 부분을 선택한 후  **``CTRL + /``** 을 입력하면 주석 처리 된다. 한번 더 누르면
>
> 해제(Toggle)된다. toggle >> (on/off)두 상태 중 하나 선택할 때 쓰는 키.



## Main 메소드

