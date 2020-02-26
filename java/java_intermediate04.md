## Calendar (추상 클래스)

- Date의 단점을 보완하고 등장한 Calendar 클래스
- Calendar 클래스의 인스턴스를 생성하려면 (static)메소드 getInstance()를 사용해야 한다.
- 메소드를 호출하면 내부적으로 자식 클래스(GregorianCalendar)의 인스턴스가 생성되면서
-  그 객체를 리턴하므로 Calendar클래스에 매핑한다. 즉 이제 Calendar 객체가 사용 가능하다는 것.

```java
Calendar cal = Calendar.getInstance();	// 위에 설명 적어놨다.
// YEAR나 MONTH 들은 상수다. final static형식이므로 클래스명.타입명 으로 접근해야한다.
int y = cal.get(Calendar.YEAR);
int m = cal.get(Calendar.MONTH) + 1;	// MONTH는 0부터 시작하므로 +1을 붙여야한다.
int d = cal.get(Calendar.DATE);
cal.add(Calendar.HOUR, 5);	// 시간을 5시간 후로 수정하는 법.-5 도 가능.
.... // 시간, 분, 초 등등 많다.
```

## java.time 패키지

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Month;

public class Main{
	
    public static void main(String[] args){
    	LocalDateTime timePoint = LocalDateTime.now();	// static메서드로 접근 후 매핑.
    	System.out.println(timePoint);
    	LocalDate ld1 = timePoint.toLocalDate();
    	System.out.println(ld1);
    	Month mon = timePoint.getMonth();
    	int h = timePoint.getHour();
    	int m = timePoint.getMinute();
    	System.out.println(ld1.getYear() + "년" + mon.getValue() + "월" + ld1.getDayOfMonth() + "일" + h + "시" + m + "분");
    }
}
```

## IO 패키지 (input output)

- 자바 IO는 크게 byte단위 입출력과 문자 단위 입출력 클래스로 나뉩니다.
- byte단위 입출력 클래스는 모두 **InputStream과 OutputStream** 라는 추상클래스를 상속받아 만들어진다.
- 문자(char)단위 입출력클래스는 모두 **Reader와 Writer**라는 추상클래스를 상속받아 만들어진다.
- 위 네 가지의 추상 클래스를 받아들이는 생성자가 있다면 다양한 입출력방법을 제공하는 클래스다.
- 위의 추상클래스들을 받아들이는 생성자가 없다면 어디로부터 입력받고,쓸것인지를 나타내는 클래스다.
- 파일로부터 입력받고 쓰기 위한 클래스 : FileInputStream, FileOutputStream, FileReader, FileWriter
- 배열로부터 입력받고 쓰기 위한 클래스 :
  -  ByteArrayInputStream, ByteArrayOutputStream, CharReader, CharWriter
- DataInputStream, DataOutputStream같은 클래스는 다양한 데이터 형을 입력받고 출력한다.
- PrintWriter는 다양하게 한줄 출력하는 println()메소드를 가지고 있다.
- BufferedReader는 한줄 입력받는 readLine()메소드를 가지고 있다.
- 이런 클래스들은 다양한 방식으로 입력하고, 출력하는 기능을 제공한다. 장식 클래스라고 한다.

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Main{
	
    public static void main(String[] args){
    	FileInputStream fis = null;	// try 바깥에서도 선언을 해주어 더 효율적이게 함.
    	FileOutputStream fos = null;// null은 객체가 의미없는 값을 가리키게 한 것으로
    	try {						// 인스턴스가 생성된 것이 아니다. Just 선언만 한 거다.
			fis = new FileInputStream("src/test/Calculator.java");
			fos = new FileOutputStream("calculator.txt");
			int readData = -1;	// 읽어들일 것이 없다면 -1 이므로 처음부터 -1로 초기화.
			while((readData = fis.read()) != -1) {	// 읽어들일 게 있다면 양수 리턴.
				fos.write(readData);	// 1바이트 씩 읽어들이고 1바이트 씩 저장한다.
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				fos.close();
				fis.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
    } // 한 글자 한 글자 읽어서 쓰기때문에 글자 수 만큼 반복실행된다. 매우 비효율적이다.
}	// 실제 출력결과를 보면 엄청 많이 반복되는걸 볼 수 있다.
```

> read()메소드는 정수(int) 4바이트 중 마지막 바이트를 읽어들인 1바이트를 저장해서 리턴한다.
>
> 4바이트인 이유는 파일로 부터 읽어오는 문자 하나를 리턴하기때문인데, char 자료형은 2바이트로
>
> 2^16 - 1 범위를 가지는데 이 범위를 만족하는 가장 작은 자료형이 int형(4바이트)이여서 4바이트가
>
> 된 것이다. 그리고 더 이상 읽어들일 것이 없다면 -1을 리턴한다. 매우 비효율적인 처리다.
>
> 밑에서는 한번에 처리하는 법을 보여줄 것이다. 잘 보고 기억해두자.

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Main2{
	
    public static void main(String[] args){
    	
    	FileInputStream fis = null;
    	FileOutputStream fos = null;
    	try {
			fis = new FileInputStream("src/test/Calculator.java");
			fos = new FileOutputStream("calcul.txt");
			
			byte[] buffer = new byte[512];
			int dataCount = -1;
			
			while((dataCount = fis.read(buffer)) != -1) {
				System.out.println(dataCount);
				fos.write(buffer, 0, dataCount);
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				fos.close();
				fis.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
    }
}
```

> 위 방법은 512바이트 크기를 처음부터 정해서 문자열 하나씩 읽어오는게 아닌 read(512byte)을 이용해서
>
> 한 번에 읽고 쓰는 방법을 구현했다. 실제로 운영체제에서 데이터를 한번 가져올때 512바이트씩 가져오기
>
> 때문에 위에서 byte의 크기를 512로 정한 것이다. 쓸 때는 write(크기, 0, 읽어 온 크기) 로 쓰게 된다.
>
> 위 방법은 실제로 실행해보면 512바이트를 넘지않는다면 딱 한번만 반복되는 것을 알 수 있다.
>
> 아주 효율적인 처리 방법이라 볼 수 있다. 잘 알아두자 개념까지. 