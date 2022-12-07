package ch01_innerClass;

public class AnonymousInnerTest {

	public static void main(String[] args) {

		Outer2 out = new Outer2();
		
		Runnable runnable = out.getRunnable(10);
		runnable.run();
//		10
		
		out.runner.run();
	//	100
	//	Runnable 이 구현된 익명 클래스 변수

	}
}
