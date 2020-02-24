## Interface (상호 작용)

```java
public interface TV{		// 추상 클래스와 다르게 abstract를 붙이지 않는다.
	public int MAX_VOLUME = 100;	// 상수로 선언 및 초기화.
	public int MIN_VOLUME = 0;

	public void turnOff();	// interface 여서 추상 메소드와 다르게 abstract 붙이지 않음.
	public void turnOn();
	public void changeVolume(int volume);
	public void changeChannel(int channel);
    
    default int plus(int i, int j){	// interface에서 default 메소드는 추상 메소드와
        return i + j;				// 다르게 구현이 가능하다.자식에서 오바라이딩도 가능함.
    }								// 오버라이딩 시 default는 빼고 적어야함.
    
    public static int multiply(int i, int j){	// static 메소드는 클래스 소유의 메소드로서
        return i * j;							// interface(name).method(name)으로
    }											// 호출이 가능하다. 객체에서 접근 불가능.
}
```

> 보통 상수 선언 시 final 을 붙이는데 interface의 경우 컴파일 시 자동으로 상수 처리를 해준다.
>
> 메소드 또한 마찬가지로 컴파일 시 abstract가 자동으로 붙여져서 처리된다.

```java
public static final int MAX_VOLUME = 100;	// 컴파일 시 자동으로 final(상수) 처리 됨.
public static final int MIN_VOLUME = 100;

public abstract void on();		// 컴파일 시 자동으로 abstact 처리 됨.
public abstract void off();
public abstract void volume();
public abstract void channel();
```

> static 이 final 앞에 붙는 이유는 인터페이스를 사용하는 클래스가 몇개든 상수라는 변하지 않는 고정 값을
>
> 항상 가지게 만들어 주기 때문이다. static이 붙으면 클래스 변수 취급이 되고 객체 생성 시 가지는 값이
>
> 아닌 클래스가 가지는 고유한 변수이다. 그러므로 인터페이스에서 static 사용 시 어디서든 변하지 않는
>
> 고정값을 원하는 경우 사용한다고 봐야한다.

```java
public class LedTV implements TV{	// implements : 구현하다
	public void on(){
		System.out.println("turn on");
	}
	public void off(){				// TV interface를 구현하기 위해 추상 메소드들을
		System.out.println("turn off");	// 다 구현해야함.
	}
	......
}
```

> 추상 클래스는 인스턴스를 만들 수 없으므로 TV interface 함수들을 다 구현해줘야함.

```java
public static void main(String args[]){
	TV tv1 = new LedTV();	// TV에서 선언한 추상 메소드들만 사용 가능함. 
	LedTV tv2 = new LedTV();	// 사용가능 하지만 TV인터페이스가 필요 없어짐.
	LedTV tv3 = (LedTv)tv1;		// TV의 tv1을 LedTV로 형변환 >> LedTV의 메소드 구현 가능.
}
```

## 내부 클래스

```java
public class InnerExam1{
	class Cal1{				// 바깥부터 하나씩 접근.
		int value = 0;
		public void plus(){
			value ++;
		}
    }  
    static class Cal2{		// 클래스 소유의 static 클래스이므로 객체 생성 없이 바로 접근 가능
        int value = 0;
		public void plus(){
			value ++;
        }
	}
    
    public void exec(){		// 메소드 안에 클래스 사용법.
        class Cal3{
            int value2 = 0;
            public void plus(){
                value2 ++;
            }
        }
        Cal3 cal3 = new Cal3();		// 함수 실행 시 객체 생성과 구현된 것들이 실행된다.
        cal3.plus();
        System.out.println(cal3.value);	// 1
    }
	public static void main(String args[]){
		InnerExam1 t = new InnerExam1();		// Cal1 생성.
		InnerExam1.Cal1 cal = t.new Cal1();
		cal.plus();
		System.out.println(cal.value);	// 1
        
        InnerExam1.Cal2 cal2 = new InnerExam1.Cal2();	// Cal2 생성. 바로 가능.
        cal2.plus();
        System.out.println(cal2.value);	// 1
	}
}
```

> class 안에 class 형식인 경우 제일 바깥 class부터 생성 후 접근.

**객체 생성 없이 사용할 수 있는 static 메소드, static 변수(클래스명.변수명), static 클래스(클래스.클래스)**

```java
// 추상 클래스 Action
public abstract class Action{
	public abstract void exec();
}

// Action 상속받는 MyAction 클래스
public class MyAction extends Action{
	public void exec(){
		System.out.println("exec");
	}
}

public class ActionExam{
	public static void main(String args[]){
		Action action1 = new MyAction();
		action1.exec();	// 정상 실행.
	
		Action action2 = new Action() {	// 상속받을 클래스를 만들 필요가 없을 경우 사용.
			@Override					// 다른 클래스에서 사용되지 않을 경우 이용한다.
			public void exec(){			// 그래서 요건 익명 클래스라 한다.
				System.out.println("exec");
			}
		};
		action2.exec();		// 정상 실행.
	}
}
```

