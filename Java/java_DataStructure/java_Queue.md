# 04. 큐(Queue) 구현하기

## Queue의 특징

- 맨 앞(front) 에서 자료를 꺼내거나 삭제하고, 맨 뒤(rear)에서 자료를 추가 함

- Fist In First Out (선입선출) 구조 

- 일상 생활에서 일렬로 줄 서 있는 모양

- 순차적으로 입력된 자료를 순서대로 처리하는데 많이 사용 되는 자료구조

- 콜센터에 들어온 문의 전화, 메세지 큐 등에 활용됨

- jdk 클래스 : ArrayList

## 연결 리스트를 활용하여 Queue 구헌하기

MyListQueue.java
```java
package ch5_queue;

import ch3.MyLinkedList;
import ch3.MyListNode;

interface IQueue {
	public void enQueue(String data);
	public String deQueue();
	public void printAll();
}

public class MyListQueue extends MyLinkedList implements IQueue{
	MyListNode front;
	MyListNode rear;

	public MyListQueue()
	{
		front = null;
		rear = null;
	}
	
	//Queue 내부 구조는 LinkedList
	@Override
	public void enQueue(String data)
	{
		MyListNode newNode;
		if(isEmpty())  //처음 항목
		{
			newNode = addElement(data); // data를 가진 노드가 생성되어 반환된다.
			front = newNode;
			rear = newNode;
		}
		else
		{
			newNode = addElement(data);
			rear = newNode; // 끝에 추가하기
		}
		System.out.println(newNode.getData() + " added");
	}

	
	@Override
	public String deQueue()
	{
		if(isEmpty()){
			System.out.println("Queue is Empty");
			return null;
		}
		String data = front.getData(); // 제일 앞 데이터를 반환하고
		front = front.next; // 잘라내기
		if( front == null ){  // 마지막 항목
			rear = null;
		}
		return data;
	}
}

```

MyListQueueTest.java
```java
package ch5_queue;

public class MyListQueueTest {

	public static void main(String[] args) {


		MyListQueue listQueue = new MyListQueue();
		listQueue.enQueue("A");
		listQueue.enQueue("B");
		listQueue.enQueue("C");
		listQueue.enQueue("D");
		listQueue.enQueue("E");
		
		System.out.println(listQueue.deQueue());
		listQueue.printAll();

	}
//	A added
//	B added
//	C added
//	D added
//	E added
//	A
//	A+->B+->C+->D+->E

}

```




