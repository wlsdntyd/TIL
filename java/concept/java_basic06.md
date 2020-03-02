## super와 부모생성자

```java
public Bus(){	// super()가 없어도 부모 클래스의 기본 생성자가 자동으로 호출된다.
	super();	// 부모 클래스의 생성자 메소드
}
```

```java
public Bus(){
	super("소방차");	// 문자열을 매개변수로 받는 부모 생성자 메소드일 경우
}					  // 이런 식으로 적으면 정상 실행된다.
```

>부모 클래스를 상속받는 자식 클래스를 인스턴스화 할 때 부모의 생성자 메소드가 실행되고 다음
>
>본인(자식) 클래스의 생성자 메소드가 실행된다. 실행되면서 초기화를 해주는 것이다.
>
>만약 부모 클래스에 기본 생성자 메소드가 아닌 매개변수를 받는 생성자 메소드라면,
>
>super();(부모 클래스) 를 이용해서 괄호() 안에 받는 매개변수 값을 넣어주면 된다.
>
>super는 부모 클래스의 메소드나 필드를 필요로 할 때도 사용할 수 있다.

```java
public class Bus extends Car {
	int fee;
    public Bus(String name, int number, int fee) {
        super(name, number);	// 부모 클래스 Car의 생성자 메소드를 받는 방법.
        this.fee = fee;
    }
}
```

## 클래스 형변환

```java
Car car = new Bus();		// Car는 부모 클래스 Bus는 Car를 상속받는 자식 클래스.
car.run();
car.ppangppang();	// 메소드가 Bus 자식 클래스의 것이라면 오류가 난다.

Bus bus = (Bus)car;	// car객체(부모)를 자식 타입으로 형변환.
bus.run();
bus.ppangppang();	// 정상 작동됨.
```

> 객체들 끼리도 상속 관계에 있다면 형변환이 가능하다.

