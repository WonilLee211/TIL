package ch20_Thread;

class MyThread extends Thread{
	
	public void run() {
		int i;
		
		for(i=0; i < 200; i++) {
			System.out.println(i + "\t");
		}
	}
}

public class ThreadTest {
	public static void main(String[] args) {
		
		System.out.println(Thread.currentThread());
//		Thread[main,5,main]

		MyThread th1 = new MyThread();
		th1.start();
		
		MyThread th2 = new MyThread();
		th2.start();

	}
}