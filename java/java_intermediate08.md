## 람다식

람다식은 다른 말로 익명 메소드 라고도 한다.

```java
package test;	// Runnable을 이용하여 쓰레드 생성.

public class lamdaExam {
	public static void main(String[] args) {
		new Thread(new Runnable() {public void run() {
			for(int i = 0; i < 10; i ++) {
				System.out.println("hello");
			}
		}}).start();
	}
}
```

> 자바는 메소드만 매개변수로 전달할 방법이 없다. 인스턴스만 전달할 수 있어서 run메소드를 갖고 있는
>
> Runnable객체를 만들어서 전달해야한다.

> 메소드만 전달이 되면 편리할텐데 방법이 없기 때문에 매번 객체를 통해 매개변수로 전달해야 했다.
>
> 이런 부분을 해결한 것이 람다표현식이다. 밑에가 람다표현식.

```java
package test;	// lamda 식을 이용한 run함수 호출 및 실행.

public class lamdaExam {
	public static void main(String[] args) {
		new Thread(()-> {	// 이 부분이 람다표현식이다.
			for(int i = 0; i < 10; i ++) {
				System.out.println("hello");
			}
		}).start();	// 실행이 되고 run메소드가 실행된다.
	}
}
```

> 람다식은 ()->{ ...... } 이런 식으로 쓰인다. 다른 말로는 익명 메소드.
>
> JVM은 Thread 생성자를 보고 ()->{ ...... } 여기에 무엇이 와야할지 대상을 추론한다.
>
> Thread생성자 api를 보면 Runnable인터페이스를 받아들이는 것을 알 수 있다.
>
> JVM은 Thread생성자가 Runnable인터페이스를 구현한 객체가 와야 하는 것을 알게 되고 자동으로
>
> Runnable을 구현하는 객체를 만들어서 매개변수로 넣어준다.

```java
package test;

public interface Compare {		// 두 값을 비교하는 함수 인터페이스 작성.
	public int compareTo(int value1, int value2);
}
```

```java
package test;

public class CompareExam {
	public static void exec(Compare compare) {
		int k = 10;
		int m = 20;
		int value = compare.compareTo(k, m);	// 이미 두 인자는 k와 m으로 정해져있다.
		System.out.println(value);
	}

	public static void main(String[] args) {
		exec((i,j)->{	// (i,j)는 함수명(인자1,인자2)의 형태이다.
			return i - j;	// 두 값은 위에 10과 20이므로 -10이 리턴된다.
		});
	}
}
```

> (인터페이스 메소드의 매개변수) -> {인터페이스 메소드 구현} 이 형식이다. 일일이 클래스를 만들고
>
> 객체를 생성하는 번거로움을 확실히 줄여준다. 기본은 끝냈다. 문제풀러 가자.