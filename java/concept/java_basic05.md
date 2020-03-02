## 접근제한자

**접근 제한자 : 클래스 내에서 멤버의 접근을 제한하는 역할을 한다.**

- **종류**

- public : 어떤 클래스든 접근할 수 있다, 다른 패키지에서도 접근 가능

- protected : 자기 자신, 같은 패키지, 서로 다른 패키지더라도 상속받은 자식 클래스에서는

  접근할 수 있다.

- private : 자기 자신만 접근할 수 있다. (같은 클래스)

- 접근제한자를 적지 않으면 default 접근 제한자(**자기 자신과 같은 패키지에서만 접근 가능**)

```java
public class AccessObj{
	private int i = 1;	// 자기 자신만 접근
	int k = 2;	// default 접근 제한자
	public int p = 3;	// 어떤 클래스든 접근
	protected int p2 = 4;	// 같은 패키지, 다른 패키지일 경우 상속받을 경우
}
```

## 추상 클래스(abstract : 추상적인)

**구체적이지 않은 클래스를 의미한다. 독수리, 타조는 구체적인 새지만,**

**새, 포유류 같은 것은 구체적이지 않다. 이런 것을 구현한 클래스를 추상 클래스라고 한다.**

```java
public abstract class Bird{		// 추상 클래스는 인스턴스(객체)를 생성할 수 없다.
	public abstract void sing();	// 구현되지 않은 추상 메소드, 실행 불가능.
	
	public void fly(){
		System.out.println("날다.");
	}
}
```

> 추상 클래스는 class 앞에 abstract를 적어야하며,추상메소드에선 리턴 타입 앞에 abstract를 적어야 한다.

```java
public class Duck extends Brid{
	@Override			// 추상 클래스를 상속받았으므로 추상 메소드를 구현해야함.
	public void sing() {
		System.out.println("꽥꽥!!우허허헝 ㅠㅠ");
	}
}
```

```java
public class DuckExam {
	public static void main(String[] args) {
        Duck duck = new Duck();	// Bird는 추상 클래스이므로 객체를 생성할 수 없다.
        duck.sing();
        duck.fly();
        if(Bird.class.isInstance(duck)) {		// 정상 실행. 추상 클래스를 상속받았다고
            System.out.println("It's a True!")	// Bird의 객체가 아닌 것이 아니다. 맞다!
        }
    }
}
```

