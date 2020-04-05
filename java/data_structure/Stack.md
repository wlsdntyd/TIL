#### Stack 구현

```java
package test;

class Stack<T> {	
	class Node<T> {		
		private T data;
		private Node<T> next;		
		public Node(T data) {
			this.data = data;
		}		
	}	
	private Node<T> top;	
	public void push(T data) {
		Node<T> t = new Node<T>(data);
		t.next = top;
		top = t;
	}	
	public T pop() {
		if(top == null)
			System.out.println("no data");
		T data = top.data;
		top = top.next;
		System.out.println(data);
		return data;
	}
	public void peek() {
		System.out.println(top.data);
	}	
	public boolean isEmpty() {
		return top == null;
	}
}
public class DataStack {
	public static void main(String[] args) {
		Stack<Integer> s = new Stack<>();
		s.push(1);
		s.push(2);
		s.push(3);
		s.push(4);
		s.peek();
		s.pop();
		s.pop();
		System.out.println(s.isEmpty());
		s.pop();
		s.pop();
		System.out.println(s.isEmpty());
	}
}
```

> 후 힘들었다.