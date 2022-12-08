package ch20_Thread;


// 다른 클래스를 상속받은 경우 implement Runnable로 thread 구현
class MyThread2 implements Runnable{

	@Override
	public void run() {
		int i;
		for(i=0; i<200; i++){
			
			System.out.print(i + "\t");			
		}
	}
}

public class ThreadTest2 {

	public static void main(String[] args) {
		
		System.out.println("main start");
		
		MyThread2 mth = new MyThread2();
		Thread th1 = new Thread(mth);
		th1.start();
		
		Thread th2 = new Thread(new MyThread2());
		th2.start();
		
		System.out.println("main end");
		
//		main start
//		main end
//		0	1	2	3	0	1	2	3 ...	

	}

}
