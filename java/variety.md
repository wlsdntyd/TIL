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