## Set ( interface )

**중복이 없고 순서도 없는 자료구조, Hashset과 TreeSet이 있다.**

**인터페이스이기에 클래스처럼 객체를 생성하지 못 한다. 또한 구현을 해야 사용 가능.**

**인터페이스나 추상 클래스 외의 클래스에는 생성자 메소드가 실행된다는 것 까지 기억해두자.**

**Car c1 = new Bus();** 여기서 Car는 부모(추상 이거나 인터페이스거나), Bus는 자식. 

c1은 Bus에서 오버라이딩한 메소드들만 사용할 수 있다. 이런 개념으로 바로 밑 코드가 구현된거 같다.

```java
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Main {
									
	public static void main(String[] args) {
		Set<String> set1 = new HashSet<>();	
		// Set을 구현한 클래스인 생성된 HashSet객체를 이용하여 Set인터페이스에 매핑.
		boolean flag1 = set1.add("kim");	// 값을 저장하고 중복되면 false 반환,
		boolean flag2 = set1.add("lee");	// 중복되지 않으면 true 반환.
		boolean flag3 = set1.add("kim");
		boolean flag4 = set1.add("jin woo");
		
		System.out.println(set1.size());	// 3
		System.out.println(flag1);	// true
		System.out.println(flag2);	// true
		System.out.println(flag3);	// false
		
		Iterator<String> iter = set1.iterator();
		// Iterator 인터페이스를 구현하기 위해 set1.iterator()를 이용.
		while(iter.hasNext()) {	// 꺼낼 것이 있다면 true 반환.
			String str = iter.next(); // 값 하나를 꺼내고 자동으로 다음 것을 참조한다.
			System.out.println(str);
		}
	}
}
-----------------------
3
true
true
false
jin woo
lee
kim
```

> 값을 저장한 순서와 다르게 마지막 것부터 출력되는 것을 보니 lifo방식 즉 스택 구조를 갖고 있는 거 같다.

## List (interface)

**중복이 허용되고 순서가 있는 자료구조.**

```java
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		List<String> list = new ArrayList<>();	// List 또한 인터페이스므로 ArrayList로
		list.add("kim");						// List를 구현시켜줘야 함.
		list.add("lee");	// set의 add와 다르게 중복이 되도 값을 저장시켜줌 true 반환.
		list.add("kim");
		System.out.println(list.size());
        
		for(int i = 0; i < list.size(); i ++) {
			System.out.println(list.get(i));	// String str = list.get(i);
		}										// 굳이 이렇게 안 적어도 되니.
        
        List<String> list2 = new ArrayList<>();
        for(String str : list) {	// list의 값을 저장할 땐 한번에 처리하는게 아니고
            list2.add(str);			// 문자열을 하나씩 불러와 저장해야한다.
        }
	}
}
```

## Map (interface)

```java
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class Main{
	
    public static void main(String[] args){
    	Map<Integer, String> map = new HashMap<>();	// Map은 HashMap으로 매핑.
    	map.put(1, "java");	// put(key, value) 형식으로 저장.
    	map.put(2, "C ++");
    	map.put(3, "python");	// Map에서 key는 중복될 수 없다.
        map.put(3, "Ruby");		// 마지막에 작성한 것이 적용되어 python은 Ruby로 바뀐다.
    	
    	Set<Integer> keys = map.keySet();
    	Iterator iter = keys.iterator();
    	while(iter.hasNext()) {
    		int key = (int)iter.next();
    		String value = map.get(key);
    		System.out.println(key + " : " + value);
    	}
    }
}
```

> Map<Integer, String> map = new HashMap<>(); 이 부분에 대해 부연 설명을 하자면,
>
> Map은 인터페이스고 HashMap은 Map을 구현한 클래스이기에 HashMap객체를 생성할 수 있고
>
> 인터페이스나 추상 클래스는 객체 생성이 불가능하기에 Map의 객체가 생성된게 아니라
>
> HashMap객체가 Map으로 매핑하는 것이다. 생성된게 아니라 매핑됐다는 것 잘 알아두자.

