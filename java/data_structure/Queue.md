#### Queue

> 아 힘들어,,

```java
package test;

import java.util.NoSuchElementException;

class Queue<T> {
	class Node<T> {
		private T data;
		private Node<T> next;	
		public Node(T data) {
			this.data = data;
			next = null;
		}
	}
	private Node<T> first;
	private Node<T> last;
	public void add(T data) {
		Node<T> t = new Node<T>(data);
		if(last == null) {
			last = t;
			first = last;
		}
		last.next = t;
		last = t;
	}
	public T remove() {
		if(first == null)
			throw new NoSuchElementException();
		T data = first.data;
		first = first.next;	
		if(first == null)
			last = null;	
		return data;
	}
	public T peek() {
		if(first == null)
			throw new NoSuchElementException();
		return first.data;
	}
	public boolean isEmpty() {
		return (first == null);
	}
}
public class Test {
	public static void main(String[] args) {
		Queue<Integer> q = new Queue<Integer>();
		q.add(5);
		q.add(4);
		q.add(3);
		q.add(2);
		System.out.println(q.peek());
		System.out.println(q.remove());
		System.out.println(q.remove());
		System.out.println(q.remove());
		System.out.println(q.isEmpty());
		System.out.println(q.remove());
		System.out.println(q.isEmpty());
	}
}
```

