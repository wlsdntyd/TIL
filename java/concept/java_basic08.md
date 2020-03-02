## Throws (오류 발생)

```java
public class ExceptionExam3 {
    public static void main(String args[]) {
        int i = 10;
        int j = 0;
        try {		// throws 가 함수에 있으므로 try ... catch ... 로 오류를 잡아야한다.
            int k = divide(i, j);
            System.out.println(k);
        } catch(IllegalArgumentException e) {
            System.out.println("0으로 나누면 안됩니다.");
        }
    }	// throws 는 함수를 호출한 곳에서 처리를 해야한다는 것을 의미.
    public static int divide(int i, int j) throws IllegalArgumentException {
        if(j == 0) {
            throw new IllegalArgumentException("0으로 나눌 수 없어요.");
        }	// 강제 오류 발생시키는 throw.
        int k = i / j;
        return k;
    }
}
```

> throw 는 강제로 오류를 발생시킨다.
>
> throws 는 함수에 적고 에러가 발생하는 부분에 try ... catch ... 로 처리를 해줘야 정상 실행된다.

## 사용자 정의 Exception

- Exception : 반드시 오류를 처리해야 하는 Exception, 예외 처리하지 않으면 컴파일 오류 발생

  checked Exception, 예외 처리는 try ... catch ... 문을 이용한다.

- RuntimeException : unChecked Exception, 예외 처리하지 않아도 컴파일 시 오류 발생 안한다.

```java
public class BizException extends RuntimeException {
	public BizException(String msg) {
		super(msg);		// 부모 클래스 RuntimeException에 전달.
	}
	public BizException(Exception ex) {
		super(ex);		// 에러 ex를 부모 클래스에 전달.
	}
}

public class BizServide {	// RuntimeException을 상속받은 BizException 클래스 처리.
	public void bizMethod(int i) throws BizException {	// Exception클래스와 동일하게.
		System.out.println("비지니스 로직이 시작합니다.");
		if(i < 0) {
			throw new BizException("매개변수 i는 0 이상이어야 합니다.");
		}
		System.out.println("비니지스 로직이 종료됩니다.");
	}
}

public class BizExam {
	public static void main(String[] args) {
		BizService biz = new BizService();
		biz.bizMethod(5);
		try {					// 음수 값을 넘길 경우 Exception이 발생하므로
			biz.bizMethod(-3);	// try catch 블록으로 처리해야 한다.
		} catch(Exception ex) {
			ex.printStackTrace();
		}
	}
}
```

> 살짝 까리한 부분이 있지만 크게 중요할 거 같진않다.