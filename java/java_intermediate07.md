## Synchronized (동기화) 메소드와 Synchronized Block

전체 코드는 이전 문서 끝에를 참고하면 된다.

```java
public synchronized void playMusicA() {
		for(int i = 0; i < 10; i ++) {
			System.out.println("Funny Music!");
		try {
			Thread.sleep((int)Math.random() * 1000);
		} catch(Exception e) {
			e.printStackTrace();
			}
		}
	}
```

```java
public void playMusicC() {
	for(int i = 0; i < 10; i ++) {
		synchronized (this) {
		System.out.println("Cafe Music!");
		}
	try {
		Thread.sleep((int)Math.random() * 1000);
	} catch(Exception e) {
		e.printStackTrace();
		}
	}
}
```

> synchronized를 메소드 앞에 붙이면 해당 메소드의 실행이 끝난 후 다음 메소드가 실행된다.
>
> synchronized를 붙이지 않은 메소드들은 synchronized가 붙은 것과 별개로 실행된다.
>
> synchronized를 사용하는 것은 모니터링 락을 획득하는 것이고 해당 부분이 끝나야 대기하던
>
> 다음 synchronized가 붙은 메소드나 블록이 다시 순차적으로 모니터링 락을 획득하고 실행이 끝나야
>
> 다시 다음 synchronized로 넘어갈 수 있다. 마지막에 대기하는 쓰레드가 너무 오래 기다려야 한다면
>
> 메소드에 synchonized를 붙이기 보단 문제가 있을 것 같은 부분에만 블록 형식으로 사용하면 된다.
>
> 또한 **쓰레드가 시작하는 순서**는 코드의 순서와 다르게 JVM과 운영체제가 결정하므로 순서가
>
> 매번 다르게 결정된다

## 쓰레드와 상태제어

<img src="C:\Users\달려라\TIL\TIL\java\Thread_state_control.jpg" style="zoom:50%;" />

**쓰레드가 3개가 있다면 JVM은 시간을 잘게 쪼개어 세 개의 쓰레드를 한 번씩 돌아가면서 실행한다.**

**이것이 빠르게 일어나다 보니 쓰레드가 모두 동시에 동작하는 것처럼 보이는 것이다.**

- 쓰레드는 실행가능 상태인 Runnable 과 실행 상태인 Running 상태로 나뉜다.
- 쓰레드는 실행 중 Thread.sleep() 이나 Object이 갖고 있는 wait()메소드가 호출되면 블록상태가 된다.
- Thread.sleep()은 특정 시간이 지나면 스스로 블록상태를 빠져나와 Runnable이나 Running상태가 된다.
- wait()메소드는 다른 쓰레드가 notify()나 notifyAll()메소드를 호출하기 전에는 블록상태가 해제되지 않는다.
- wait()은 sleep()이랑 다르게 모니터링 락을 놓게 되어 다른 쓰레드가 notify()해줘야 한다.
- Thread의 yield(양보)메소드는 다른 쓰레드에게 실행을 양보한다.
- 쓰레드는 다른 쓰레드와 독립적으로 실행하는 것이 기본이다. 하지만 다른 쓰레드의 종료를 기다려야 하는
- 경우가 생길 시에는 join()메소드를 사용하면 된다.
- https://widevery.tistory.com/28 여기를 참조해서 데몬 쓰레드까지 개념을 잘 익히자.

```java
package test;	// join 사용한 예.

public class JoinTest extends Thread {
	
	public void run() {
		for(int i = 0; i < 5; i ++) {
			System.out.println(i);
			try {
				Thread.sleep(1000);
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

public class testExam {
	
	public static void main(String[] args) {
		JoinTest jt = new JoinTest();
		jt.start();
		System.out.println("시작");
		try {
			jt.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("종료!");
	}
}
```

> 위에는 join 함수의 예를 보여주고 있다. Runnable과 다르게 Thread를 상속받고 있으므로 Thread를
>
> 따로 생성하지 않아도 start()메소드를 사용할 수 있다.

```java
package test;	// wait과 notify의 사용 예.

public class WaitTest extends Thread {
	int total;
	
	public void run() {
		synchronized (this) {	// 동기화 블록을 설정. 
		for(int i = 0; i < 5; i ++) {
			System.out.println(i + "를 더합니다.");
			total += i;
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		notify();	// wait하고 있는 다른 쓰레드를 깨움.
		}
	}
}
```

```java
package test;

public class waitExam {

	public static void main(String[] args) {
		WaitTest wt = new WaitTest();
		wt.start();
		// main쓰레드가 위의 쓰레드보다 아래의 wt블록을 먼저 실행될 시 wait()만나면서 정상 작동.
		synchronized (wt) {
			try {
				System.out.println("b가 완료될 때 까지 기다립니다.");
				wt.wait();	// 정지됨. 위의 쓰레드가 notify해줘야 됨.
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println("Total is : " + wt.total);
		}
	}
}
```

> wiat과 notify는 동기화된 블록 안에서 사용해야 한다는 것을 알아두자.

## 데몬 쓰레드

**Daemon 이란 보통 리눅스와 같은 유닉스 계열의 운영체제에서 백그라운드로 동작하는 프로그램을 말한다.**

데몬 쓰레드를 만드는 방법은 쓰레드에 데몬 설정을 하면 된다. 또한 데몬 쓰레드는 일반 쓰레드(main 등)가

모두 종료되면 강제적으로 종료된다. 보통 백그라운드에서 특별한 작업을 처리해야 할 때 사용한다.

```java
package test;

public class DaemonThread implements Runnable {
	
	public void run() {
		while(true) {
			System.out.println("데몬 쓰레드가 실행 중 입니다.");
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
                break;	// Exception 발생 시 break를 안 적으면 빠져나올 수가 없다.
			}			// break를 걸어서 빠져나오게 해주자.
		}
	}
	public static void main(String[] args) {
		Thread thread = new Thread(new DaemonThread());	// Runnable을 구현했기 때문에
		thread.setDaemon(true);							// Thread객체를 생성해야 한다.
		thread.start();
		// 메인 쓰레드가 1초 뒤에 종료되도록 설정. 데몬 쓰레드는 다른 쓰레드 모두 종료되면 종료.
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("메인 쓰레드가 종료됩니다.");
	}
}
```

