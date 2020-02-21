## 배열

```java
int[] array1 = new int[4];	// 4개의 int형 변수가 들어갈 수 있는 배열.
array1[2] = 3;				// index 접근.
int[] array2 = new int[]{1,2,3,4,5};	// 선언과 동시에 초기화.
```

```java
public static void main(String[] args) {
	int[] array1 = new int[100];
	int sum = 0;
	for(int i = 0; i < array1.length; i++) {
		array1[i] = i + 1;
		sum += array1[i];
	}
	System.out.println(sum);
}								// 결과는 5050
```

```java
int[][] array4 = new int[3][4];		// 2차원 배열,[[1,2,3,4],[1,2,3,4],[1,2,3,4]] 형태
array4[0][0] = 10;	// 첫 번째 배열 안의 첫 번째 데이터.
------------------------------
int[][] array5 = new int[3][];	// 가변크기의 2차원 배열.
array5[0] = new int[1];	// [0] 의 크기를 정수 1개로 정해줌.
array5[1] = new int[2]; // [1] 의 크기를 정수 2개로 정해줌.
------------------------------
int[][] array6 = {{1}, {2,3}, {4,5,6}};	// 선언과 동시에 초기화.
```

```java
int[][] array = {{1}, {1,2}, {1,2,3}, {1,2,3,4}};

for(int i = 0; i < array.length; i++){				// 2중 배열 일 때 for문으로 접근.
	System.out.println(i + 1 + "번째 줄을 출력합니다.");
	for(int j = 0; j < array[i].length; j++){
		System.out.println(array[i][j] + " ");
	}
	System.out.println("");
}
```

```java
int[] iarr = {10, 20, 30, 40, 50};
for(int value:iarr){			// 타입 값을 받아줄 변수명 : 출력하고 싶은 자료구조.
	System.out.println(value);
}
------------------
10
20
30
....
```

## Class

```java
public class Car {

}
```

```java
public calss CarExam {
	public static void main(String args[]){
		Car c1 = new Car();
		Car c2 = new Car();
	}
}
```

> new 연산자는 new 연산자 뒤에 나오는 생성자(Car)를 이용하여 메모리에 객체를 만들라는 명령.
>
> 메모리에 만들어진 객체를 인스턴스(instance)라고 한다. 새로 만들어졌기에 인스턴스라 한다.
>
> 이렇게 만들어진 객체를 참조하는(reference,레퍼런스,가리키는) 변수가 c1, c2 이다.

## String 클래스

**자바에서 가장 많이 사용하는 String클래스**

> String은 int나 char, float 같이 기본 타입이 아니라 참조형 타입이다.
>
> 참조형 타입에는 기본 타입을 제외한 모든 것이 들어있다. 클래스 같은.

```java
String str1 = "hello";		// 클래스 객체를 만들 땐 new를 사용해야하지만 String만 예외.
String str2 = "hello";		// 하지만 new를 안 썼기때매 객체를 생성한 게 아님.
// "hello" 라는 문자열이 메모리 중에서 상수가 저장되는 영역에 저장된다. 상수는 변하지 않는 값.
// str2는 str1이 참조하는 인스턴스를 str2도 참조한다.
```

```java
String str3 = new String("hello"); // new연산자를 사용했기에 새로운 인스턴스 생성.
String str4 = new String("hello"); // 다시 new연산자를 썼으므로 서로 다른 새로운 인스턴스 생성.
// 참조변수
boolean st;
st = str3.equals(str4);			// 문자열이 같은지를 묻는 함수로 요건 true가 맞다.
System.out.println(st);			// 결과 true
st = (str3 == str4);
System.out.println(st);			// 결과 false
st = (str1 == str2);
System.out.println(st);			// 결과 true
str4.substring(3);				// 결과 "lo"	(3index부터 마지막까지)
// substring은 slicing을 통해 뒷 부분을 출력해준다. 새로운 String 참조가 이루어짐.
```

> String은 다른 클래스와 다르게 new를 사용하지 않고 사용할 수 있으므로 메모리를 아끼려면
>
> new를 사용하지 않고 사용하는 것이 좋다. 또한 String 클래스는 불변이여서 값을 수정할 수 없다.
>
> 따라서 메소드를 호출해도 String 내부의 값은 변하지 않는다. 따라서 메소드를 통한 반환 값은
>
> 새로운 String을 생성해서 반환하는 것이다.

## Field(필드, 속성)

```java
public class Car{
	String name;	// Car 클래스의 이름 속성(field)
	int price;		// Car 클래스의 가격 속성
	String kind;	// Car 클래스의 종류 속성
}
```

## 메소드 (클래스가 가지고 있는 기능)

> 필드가 물체(Class)의 상태(속성)이라면 그 물체의 행동에 해당하는 것이 메소드다.
>
> 메소드는 입력값이 있고 반환하는 값은 반환값, 리턴값이라 한다.
>
> 이때 입력값은 매개변수(Parameter)와 인자(Argument)가 있다
>
> 매개 변수(Parameter)는 받아들이는 변수, 인자는 함수 호출 시 전달되는 값, 넣는 값