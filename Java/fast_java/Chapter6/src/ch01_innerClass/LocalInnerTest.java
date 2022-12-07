package ch01_innerClass;

public class LocalInnerTest {

	public static void main(String[] args) {
		
		Outer out = new Outer();
		Runnable runner = out.getRunnable(10);
		runner.run();
		
//		i =10
//		num = 100
//		localNum = 10
//		outNum = 100(외부 클래스 인스턴스 변수)
//		Outer.sNum = 200(외부 클래스 정적 변수)

	}

}
