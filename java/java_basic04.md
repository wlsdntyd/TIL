## 변수의 scope 와 static

> scope : 변수의 사용 가능함 범위.
>
> static : 정적 변수

```java
public class Calculator{
	int globalResult = 10;	// 인스턴스 변수, 인스턴스(객체) 생성 시 할당되는 부분.
	static int localResult = 20;	// 클래스 변수, 인스턴스가 없어도 할당되는 부분.
}
```

> static 변수, 즉 클래스 변수는 클래스의 인스턴스를 만들지 않아도 사용할 수 있다. (클래스명.변수명)
>
> static 을 붙이면 공간이 하나만 할당되며 공유가 된다. 즉 여러 인스턴스에서 초기화를 하면
>
> 마지막 것이 적용이 되는 것이다.

## static 메서드(정적 메서드)

> static 메서드는 객체의 생성 없이 호출이 가능하고, 객체에서는 호출이 불가능하다.
>
> 또한 static 메서드 안에서는 인스턴스 변수 접근이 불가능하다.
>
> 전역으로 자주 사용할 메서드를 static 메서드로 만들어 사용한다. 불필요한 코드 수를 줄일 수 있다.

## enum 타입 클래스 (참조 자료형)

```java
enum Gender {
	Male, Female;
}

public class EnumExam {
	public static void main(String[] args) {
	Gender Person1;
	Gender Person2;
	Person1 = Gender.Male;	// 정상 실행.
	Person2 = "Male";	// 실행(comfile) 오류.
	}
}
```

> enum 클래스는 Male 과 Female 이란 타입을 가진 참조 자료형으로,
>
> String 타입이라 볼 수 없으며 enum 클래스 안에서 생성한 타입만 값으로 쓸 수 있으므로
>
> Person2 에서는 오류가 난 것을 볼 수 있다.

## 생성자

> 모든 클래스는 인스턴스화 될 때 생성자(new)를 사용한다.
>
> 생성자를 만들지 않았다면 매개변수가 없는 생성자가 컴파일할 때 자동으로 만들어진다.

```java
public class Car{
	String name;
	int number;
	
	public Car(String name){
		this.name = name;	// 받는 변수(매개변수) name과 객체(인스턴스) 변수 name
	}						// 이 같기 때문에 this.name(객체 변수)로 적어야됨.
}
---------------------------
public static void main(String args[]){
	Car c1 = new Car("택시");	// 매개변수가 있기에 "택시"를 적어줘야 한다.
	System.out.prinkln(c1.name);
}
```

> this 는 현재 객체, 자기 자신을 나타낸다.
>
> 클래스 안에서 자기 자신이 가지고 있는 메소드를 사용할 때도 this.메소드명()으로 호출할 수 있다.

## 메소드 오버로딩

**매개변수의 유형과 개수를 다르게 하여 같은 이름의 메소드를 여러 개 가질 수 있도록 하는 기술.**

```java
class MyClass2{
	public int plus(int x, int y){
		return x + y;
	}
	public int plus(int x, int y, int z){
		return x + y + z;
	}
	public String plus(String x, String y){
		return x + y;	// ("123","465") >> "123465"
	}
}
```

> 셋 다 정상적으로 실행된다.

## 생성자 오버로딩

```java
public class Car{
	String name;
	int number;
	
	public Car(){
	}
	
	public Car(String name, int number){
		this.name = name;
		this.number = number;
	}
	
	public Car(){			 // this는 자신의 생성자를 호출한다.
		this("이름없음", 0);  // 따라서 바로 위 생성자 메소드를 호출하게 되므로 this()로
	}					    // 적을 수 있다.
	
	public Car(){
		this.name = "뛰뛰";	// this는 자신의 생성자를 호출하는데 이미 위에 생성자 메서드가
		this.number = 123;	 // 존재함으로 중복이 일어나게 된다.
	}						 // 그러므로 위에 방식처럼 적어야한다. this("...", 123);
}
	
```

> this 는 자신의 생성자 메소드를 호출한다는 것을 알아두자.