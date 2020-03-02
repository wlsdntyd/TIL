## Object(최상위 클래스) 와 오버라이딩

**equals** : 객체가 가진 값을 비교할 때 사용,  오버라이딩을 구현해야 논리적(값)으로 같을 때 True 값을

반환하게 된다. 오버라이딩을 구현하지 않으면 메모리 주소 값을 비교하게 된다.

**toString** : 객체가 가진 값을 문자열로 반환해준다. (ex. StringBuffer >> String)

toString 또한 오버라이딩을 구현해야 값이 제대로 출력되는 경우가 있다. 

**hashCode** : 객체의 해시코드 값 반환. 객체의 메모리 번지를 이용해서 해시코드를 만들어 리턴하기

때문에 객체마다 다른 값을 가지고 있다. 동등성(논리적,값) 비교시 hashCode();를 오버라이딩해야

다른 메모리 번지를 사용할지라도 리턴값을 같게 맞출 수 있고 다음 수행해야할 equals 오버라이딩도

할 수 있기 때문이다. 둘 다 오버라이딩을 잘 했다면 동일한 hashCode가 리턴 될 것이다.

오버라이딩을 두번 한 이유는 hashCode 값이 같고 equals로 리턴 값이 같아야 동등객체(값이같은)

로 인식하기 때문이다.

> 위에 세 개의 메소드는 자주 사용되는 것들로 알고리즘을 공부하게 된다면 반드시 마주치는
>
> 메소드들 이다. 얼른 중급 마치고 문제 좀 풀어보고 알고리즘과 자료구조를 공부하자.

## java.lang 패키지 / 오토박싱

```java
int i = 5;// java.lang 패키지의 클래스에는 기본형 타입을 객체로 변환시켜주는 Wrapper클래스가 있다.
Integer i2 = new Integer(5);	// Integer는 int를 객체(참조형)로 변환시켜준다.
// (밑)이렇게 적어도 new Intger(5)로 처리해준다.
Integer i3 = 5;	// 오토박싱. 기본 타입 데이터를 객체 타입으로 자동 형변환 시켜주는 기능.
int i4 = i3.intValue();	// i3가 객체이기에 intValue();로 값만 넘겨야한다.
int i5 = i3; // java5 부터 구현됨. 오토언박싱 : 객체 타입 데이터를 기본형 타입 데이터로 변환.
```

> 타입 > 객체, 객체 > 타입 : 컴파일 시 Wrapper클래스의 메소드가 자동으로 실행되면서 처리해준다고 보면 됨.

```java
StringBuffer sb = new StringBuffer();
sb.append("hello");		// StringBuffer가 갖고 있는 메소드들은 대부분 자기 자신(this)을
sb.append(" ");			// 반환한다.
sb.append("world!");
System.out.println(sb.toString());
StringBuffer sb2 = new StringBuffer();
StringBuffer sb3 = sb2.append("hello");	// StringBuffer는 자기 자신을 리턴한다.
if(sb2 == sb3){		// 정상 실행됨.sb3 가 sb2를 레퍼런스하므로 주소값이 같아서 같다고 보면 된다.
	System.out.println("sb2 == sb3");
}	// 아래처럼 한번에 작성도 가능하다.
String str2 = new StringBuffer().append("hello ").append("world").toString();
```

> 메소드 체이닝 : 자기 자신을 리턴하여 계속해서 자신의 메소드를 호출하는 방식

## String 클래스의 문제점

**String 클래스는 불변클래스이다.**

```java
String str1 = "hello";		// new String(); >> str1 = "hello";
String str2 = " world";		// new String(); >> str2 = " world";
String str3 = str1 + str2;
// str3 = new StringBuffer().append(str1).append(str2).toString();

String str4 = "";
for(int i = 0; i < 100; i ++) {
	str4 += "*";	// 성능상 굉장히 안 좋다.
}	// new StringBuffer().append(str4).append("*").toString(); 100번 반복된다.

StringBuffer sb = new StringBuffer();
for(int i = 0; i < 100; i ++) {
	sb.append("*");			// 메모리 효율을 훨씬 높일 수 있는 방법.
}
String str5 = sb.toString();
```

## Math 클래스

**Math 클래스는 생성자가 private으로 되어 있기 때문에 new 연산자를 이용하여 객체를 생성할 수 없다.**

하지만 모든 메소드와 속성이 static으로 정의되어 있어서 객체 생성 없이 사용 가능하다.

저번에 배웠던 것처럼 (클래스명.필드), (클래스명.메소드명()) 바로 접근이 가능한 것이다. 

```java
int value1 = Math.max(5, 30);	// 30
int value2 = Math.abs(-10);		// 10
double value3 = Math.random();	// 0.56413 0 ~ 1 random
double value4 = Math.sqrt(25);	// 5
```

> Math 는 싸인, 코싸인, 탄젠트 까지 구할 수 있다.