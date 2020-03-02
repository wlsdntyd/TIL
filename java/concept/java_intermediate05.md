## 다양한 타입의 출력

```java
import java.io.DataOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class Main2{
	
    public static void main(String[] args){
    	try( // try() 안에 close해야 할 객체를 만들어주면 자동으로 close메소드를 실행한다.
    			DataOutputStream dos = new DataOutputStream(new FileOutputStream("data.txt"));	// () 소괄호로 묶었어도 ;(세미콜론) 쓰는 걸 잊지말자.
    		){
    		dos.writeInt(100);
    		dos.writeChars("kimjinwoo");
    	} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
}
```

> DataOutputStream은 다양한 타입을 저장 할 수 있게 해준다. int,boolean,double,char,chars ...

## 다양한 타입의 입력

```java
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Read {

	public static void main(String[] args) {	
		try(
			DataInputStream dis = new DataInputStream(new FileInputStream("data.txt"));
				) {
				int a = dis.readInt();
				double b = dis.readDouble();
				String c = dis.readLine();
				System.out.println(a + " " + b + c);
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	}
}
```

> try() 로 생성된 입력객체를 묶어주면서 자동으로 close()된다. 데이터를 가져올 땐 저장한 순서로
>
> 가져와야 한다는 점이 까다로운 거 같다.

#### 데코레이터 패턴(Decorator Pattern)

> 객체에 추가적인 요건(기능)을 동적으로 첨가하는 방식, 서브클래스를 만드는 것을 통해
>
> 기능을 유연하게 확장할 수 있는 방법 제공.

## Char 단위 입출력(Console)

char 단위 입출력 클래스는 클래스 이름이 Reader나 Writer로 끝이 난다.

- System.in - 키보드 의미.(InputStream)
- BufferedReader - 한 줄씩 입력 받기위한 클래스, 또한 생성자에 InputStream을 입력받는 생성자가 없다.
- System.in은 InputStream 타입이므로 BufferedReader 의 생성자에 바로 들어갈 수 없어서
- InputStreamReader 클래스를 이용해야 한다.

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Read {

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String st = null;	// 변수의 scope(범위)를 위해 바깥에 선언한다.
		try {				// 왜냐면 출력이 try문 바깥에서 이루어지고 있기 때문에.
			st = br.readLine();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println(st);
	}
}

```

## Char 단위 입출력(File)

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class Read {

	public static void main(String[] args) {
		BufferedReader br = null;	// 한 줄씩 읽어들이기 위해 BufferedReader를 씀.
		PrintWriter pw = null;
		try {
			br = new BufferedReader(new FileReader("src/test/Read.java"));
			pw = new PrintWriter(new FileWriter("copy.txt"));
			String line = null;
			while((line = br.readLine()) != null) {
				pw.println(line);	// readLine메소드는 더 이상 읽을게 없을 때 null반환.
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			pw.close();
			try {
				br.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
```

> PrintWriter 클래스는 생성자 함수에 writer기능이 있어서 굳이 매개변수로 FileWriter를 받을 필요는 없다.
>
> 거의 다 왔다 힘내자...