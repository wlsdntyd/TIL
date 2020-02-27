## Annotatio (어노테이션)

- 클래스나 메소드 위에 @(at) 기호로 이름이 시작한다.
- 사용자가 직접 만들 수도 있지만 그럴 일은 거의 없다 볼 수 있다.

```java
package test;		// Annotation 페이지.

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)	// 실행 시 감지하기 위해 RUNTIME으로 해줌.
public @interface Count100 {
	
}
```

```java
package test;

public class Hello {
	@Count100		// 사용할 메소드 위에 작성.
	public void hello() {
		System.out.println("hello");
	}
}
```

```java
package test;

import java.lang.reflect.Method;

public class Main{
	
    public static void main(String[] args){
    	Hello hell = new Hello();
    	
    	try {
			Method method = hell.getClass().getDeclaredMethod("hello");
			if(method.isAnnotationPresent(Count100.class)) {
				for(int i = 0; i < 10; i ++) {
					hell.hello();
				}
			} else {
				System.out.println("it's none!");
			}
		} catch (NoSuchMethodException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SecurityException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
}
```

> if 문을 보면 hello메소드가 @Count100 이라는 어노테이션이 설정되어있다면 실행된다는 것을 알 수 있다.

## Thread (쓰레드)

**동시에 여러가지 작업을 동시에 수행할 수 있게 하는 것.**

- 프로세스 : 현재 실행되고 있는 프로그램
- 자바는 JVM 에 의해 실행된다. 자바 프로그램도 프로세스로 실행하는 것이다.

```java
package test;

public class Hello extends Thread {		// Thread 클래스를 상속받아야 사용할 수 있다.
	String str;
	
	public Hello(String str) {
		this.str = str;
	}
	
	public void run() {	// Thread의 메소드 run()을 오버라이딩해야 한다.
		for(int i = 0; i < 10; i ++) {
			System.out.println(str);
			try {
				Thread.sleep((int)Math.random() * 1000);// 너무 빨라서 텀을 줘야 알 수 있다.
			} catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
}
```

```java
package test;

public class Main{
	
    public static void main(String[] args){
    	Hello h1 = new Hello("H");
    	Hello h2 = new Hello("E");
    	
    	String a = "jinwoo";
    	h1.start();
    	h2.start();				// 함수명을 호출하면 안되고 Thread는 start()메소드로 실행해야
    	System.out.println(a);	// Thread의 기능을 수행할 수 있다.
    }
}
```

> 간단히 Thread 사용하는 법.

## Thread (implements Runnable) 사용

Thread 클래스를 상속받아 사용해도 되지만 클래스 특성 상 두 개의 클래스를 상속받는게 불가능해서

Runnable 인터페이스를 구현해서 Thread클래스의 기능을 이용할 수 있다.

Runnable의 장점은 오버라이드 할 run()메소드를 자동으로 호출해준다.

```java
package test;

public class TestThread implements Runnable {
	String str;
	
	public TestThread(String str) {
		this.str = str;
	}
	
	@Override
	public void run() {
		for(int i = 0; i < 10; i ++) {
			System.out.println(str);
			try {
				Thread.sleep((int)Math.random());
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}

```

```java
package test;

public class Main{
	
    public static void main(String[] args){
    	TestThread th1 = new TestThread("hi");
    	TestThread th2 = new TestThread("hello");
    	
    	Thread t1 = new Thread(th1);	// Runnable은 start()메소드를 갖고 있지 않아
    	Thread t2 = new Thread(th2);	// Thread클래스의 도움을 받아야 한다.
    	
    	t1.start();
    	t2.start();
    	System.out.println("ggggggggg");
    }
}
```

## Thread 와 공유 객체

```java
package test;	// 뮤직 박스라는 공유 객체.

public class MusicBox {

	public void playMusicA() {
		for(int i = 0; i < 10; i ++) {
			System.out.println("Funny Music!");
		try {	// 1초 이하의 시간동안 열번 반복하기 위해 이렇게 적었다.
			Thread.sleep((int)Math.random() * 1000);
		} catch(Exception e) {
			e.printStackTrace();
			}
		}
	}
	
	public void playMusicB() {
		for(int i = 0; i < 10; i ++) {
			System.out.println("Lonely Music!");
		try {
			Thread.sleep((int)Math.random() * 1000);
		} catch(Exception e) {
			e.printStackTrace();
			}
		}
	}
	
	public void playMusicC() {
		for(int i = 0; i < 10; i ++) {
			System.out.println("Cafe Music!");
		try {
			Thread.sleep((int)Math.random() * 1000);
		} catch(Exception e) {
			e.printStackTrace();
			}
		}
	}
}
```

```java
package test;	// Thread , 뮤직 박스를 가지는 Thread 객체 MusicPlayer.

public class MusicPlayer extends Thread {
	int type;
	MusicBox musicBox;
	
	public MusicPlayer(int type, MusicBox musicBox) {
		this.type = type;
		this.musicBox = musicBox;
	}
	
	public void run() {
		switch (type) {
		case 1 : musicBox.playMusicA();	break;
			
		case 2 : musicBox.playMusicB();	break;
			
		case 3 : musicBox.playMusicC(); break;
		}
	}
}
```

```java
package test;		// 하나의 객체(뮤직박스)를 여개 개의 Thread(플레이어)가 사용함.

public class MusicBoxExam {

	public static void main(String[] args) {
		MusicBox box = new MusicBox();
		
		MusicPlayer kim = new MusicPlayer(1, box);
		MusicPlayer lee = new MusicPlayer(2, box);
		MusicPlayer kang = new MusicPlayer(3, box);
		
		kim.start();
		lee.start();
		kang.start();
	}
}
```



