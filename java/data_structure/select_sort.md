#### 선택 정렬 알고리즘

```java
package test;

import java.util.Scanner;

public class SelectSort {
	public static void main(String[] args) {		
		Scanner sc = new Scanner(System.in);
		System.out.print("input array'length : ");
		int num = sc.nextInt();	
		int[] array = new int[num];
		System.out.printf("%d 개의 배열의 숫자를 공백 기준으로 입력하시오 : ", num);
		for(int i=0; i<num; i++)
			array[i] = sc.nextInt();
		sc.close();		
		for(int i=0; i<num-1; i++) {
			for(int j=i; j<num-1; j++) {
				if(array[i]>array[j+1]) {
					int tmp = array[i];
					array[i] = array[j+1];
					array[j+1] = tmp;
				}
			}
		}
		for(int i=0; i<num; i++)
			System.out.print(array[i] + " ");
	}
}
```

