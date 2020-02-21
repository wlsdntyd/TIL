## 배열

```java
int[] array1 = new int[4];	// 4개의 int형 변수가 들어갈 수 있는 배열.
array1[2] = 3;				// index 접근.
int[] array2 = new int[]{1,2,3,4,5};	// 선언과 동시에 초기화.
```

```java
public static void main(String[] args) {
	int[] array1 = new int[100];
	int sum = 0;
	for(int i = 0; i < array1.length; i++) {
		array1[i] = i + 1;
		sum += array1[i];
	}
	System.out.println(sum);
}								// 결과는 5050
```

```java
int[][] array4 = new int[3][4];		// 2차원 배열,[[1,2,3,4],[1,2,3,4],[1,2,3,4]] 형태
array4[0][0] = 10;	// 첫 번째 배열 안의 첫 번째 데이터.
------------------------------
int[][] array5 = new int[3][];	// 가변크기의 2차원 배열.
array5[0] = new int[1];	// [0] 의 크기를 정수 1개로 정해줌.
array5[1] = new int[2]; // [1] 의 크기를 정수 2개로 정해줌.
------------------------------
int[][] array6 = {{1}, {2,3}, {4,5,6}};	// 선언과 동시에 초기화.
```

```java
int[][] array = {{1}, {1,2}, {1,2,3}, {1,2,3,4}};

for(int i = 0; i < array.length; i++){				// 2중 배열 일 때 for문으로 접근.
	System.out.println(i + 1 + "번째 줄을 출력합니다.");
	for(int j = 0; j < array[i].length; j++){
		System.out.println(array[i][j] + " ");
	}
	System.out.println("");
}
```

```java
int[] iarr = {10, 20, 30, 40, 50};
for(int value:iarr){			// 타입 값을 받아줄 변수명 : 출력하고 싶은 자료구조.
	System.out.println(value);
}
------------------
10
20
30
....
```

## Class

```java
public class Car {

}
```

```java
public calss CarExam {
	public static void main(String args[]){
		Car c1 = new Car();
		Car c2 = new Car();
	}
}
```

> new 연산자는 new 연산자 뒤에 나오는 생성자를 이용하여 메모리에 객체를 만들라는 명령.
>
> 메모리에 만들어진 객체를 인스턴스(instance)라고도 한다.
>
> 이렇게 만들어진 객체를 참조하는 변수가 c1, c2 이다.