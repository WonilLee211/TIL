package ch20_Thread;

class PriorityThread extends Thread{
	
	public void run() {
		int sum = 0;
		
		Thread t = Thread.currentThread();
		System.out.println(t + "start");
		
		for(int i = 0; i < 1000000; i++) {
			sum += 1;
		}
		System.out.println(t.getPriority() + "end");
	}
}

public class PriorityTest {

	public static void main(String[] args) {
		
		int i;
		for(i = Thread.MIN_PRIORITY; i <= Thread.MAX_PRIORITY; i++){
			
			PriorityThread pt = new PriorityThread();
			pt.setPriority(i);
			pt.start();
			
//			Thread[Thread-0,1,main]start
//			Thread[Thread-1,2,main]start
//			Thread[Thread-2,3,main]start
//			Thread[Thread-3,4,main]start
//			Thread[Thread-4,5,main]start
//			Thread[Thread-5,6,main]start
//			Thread[Thread-6,7,main]start
//			Thread[Thread-7,8,main]start
//			Thread[Thread-8,9,main]start
//			Thread[Thread-9,10,main]start
			
			// thread 종료 시점은 매번 다르다.
//			3end
//			7end
//			9end
//			6end
//			2end
//			5end
//			4end
//			1end
//			10end
//			8end

		
		}
	}
}
