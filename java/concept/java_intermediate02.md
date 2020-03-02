## java.util 패키지

- 자료구조와 관련된 컬렉션 프레임워크와 관련된 인터페이스와 클래스

- Deprecated : 더 이상 지원하지 않으니 사용하지 않는 것을 권고함.
- List, Set, Collection, Map 은 자료구조, 즉 컬렉션 프레임워크와 관련된 인터페이스.

 ## 컬렉션 프레임워크 ( 자료 구조 )

**java.util 패키지에는 자료를 다룰 수 있는 자료구조 클래스가 다수 존재한다.**

**이러한 자료구조 클래스들을 컬렉션 프레임워크(뼈대)라고 한다.**

- 자료구조란 자료를 저장할 수 있는 구조. 다양한 방법을 제공하는 것을 컬렉션 프레임워크라 한다.
- 컬렉션 프레임워크에서 가장 기본이 되는 interface는 Collection인터페이스이다.
- Collection 인터페이스는 여기에 자료가 있다라는 것을 표현.
- 중복도 허용하고, 자료의 저장 순서를 기억하지 못 하는 것이 Collection 인터페이스.
- 대표적인 메소드에는 add(), size(), (반복자)iterator() 메소드.
- 더 자세한 내용은 https://programmers.co.kr/learn/courses/9/lessons/256 여기를 보자.(너무 길어,,,)
- 자료구조에는 Set(중복허용 X), List(순서가 있고 중복이 허용됨), Map(Key, Value) 이 있다.

## Generic ( 일반적인 )

```java
public class Box {
	private Object obj;	// Object 최상위 클래스의 객체를 선언한다.
	public void setObj(Object obj) {// 최상위 클래스이기에 자손(자식)들을 받아들일 수 있다.
		this.obj = obj;
	}
	public Object getObj() {
		return obj;
	}
}
```

```java
public class BoxExam {
	public static void main(String[] args) {
		Box box = new Box();
		box.setObj(new Object());
		Object obj = box.getObj();
		
		box.setObj("hello");// Object 클래스가 매개변수로 받아들이고 있으므로 오류가 없다.
		String str = (String)box.getObj();	// 리턴 타입이 Object여서 String으로 형 변환.
		System.out.println(str);
		
		box.setObj(1);	// 위쪽과 비슷한 상황.
		int value = (int)box.getObj();
		System.out.println(value);
	}
}
```

> Generic 을 사용하지 않은 예.

```java
public class Box<E> {		// E 라는 가상의 클래스이자 타입
	private E obj;
	public void setObj(E obj) {
		this.obj = obj;
	}
	public E getObj() {		// 리턴 형식도 String은 String인 것처럼 E로 받는다.
		return obj;
	}
}
```

```java
public class BoxExam {
	public static void main(String[] args) {
		Box<Object> box = new Box<>();
		box.setObj(new Object());
		Object obj = box.getObj();
		
		Box<String> box2 = new Box<>();	// 가상 E클래스에 String클래스를 적용시킴.
		box2.setObj("hello");
		String str = box2.getObj();		// 형 변환 필요성이 없어짐.
		
		Box<Integer> box3 = new Box<>();	// 가상 E클래스에 Integer클래스 적용.
		box3.setObj(1);
		int value = (int)box3.getObj();
	}
}
```

> Generic을 사용한 예.

