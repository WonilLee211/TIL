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
