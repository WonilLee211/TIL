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
