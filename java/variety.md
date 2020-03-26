```java
int n1 = 3;
int n2 = 5;
System.out.println("A is a " + n1 + n2);	// A is a 35
System.out.println("A is a " + (n1 + n2));	// A is a 8
```

> 문자열 + 숫자가 될 경우 문자 + 문자 형식이 돼버린다. 고로 문자열이 된 n1으로 인해 n2도 문자열이 된다.

```java
System.out.println("A");	// 줄 바꿈이 일어난다.
System.out.print("B");		// 줄 바꿈이 일어나지않는다.
```

```java
Scanner sc = new Scanner(System.in);
int a = sc.nextInt();
sc.close();
```

> Scanner 나 입출력이 오고 가는 메소드라면 무조건 close메소드로 닫아줘야 한다.

### 값에 의한 호출(메소드)

**프리미티브 타입의 매개변수 : byte, short, int, long, float, double, char, boolean**

그 밖의 타입들 : String, 배열, 클래스 등등

**프리미티브 타입의 매개변수는 호출된 메서드에서 값을 변경하더라도 호출한 쪽에 영향을 주지 못한다.**

**"값에 의한 호출"** 이기 때문이다. 반면 배열이나 그 밖의 타입들에서는 호출한 쪽에서도 변경된다.