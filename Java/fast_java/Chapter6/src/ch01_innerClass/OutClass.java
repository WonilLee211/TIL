package ch01_innerClass;

public class OutClass {
	
	private int num = 10;
	private static int sNum = 20;
	private InClass inClass;
	
	public OutClass(){
		inClass = new InClass(); // 내부 클래스 생성
	}
	
	class InClass {
		int inNum = 100;
//		static int sInNum = 200; // 에러 남
//		The field sInNum cannot be declared static in a non-static inner type,
//		unless initialized with a constant expression
		
		void inTest() {
			System.out.println("OutClass num = " +num + "(외부 클래스의 인스턴스 변수)");
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 스태틱 변수)");
			System.out.println("InClass inNum = " + inNum + "(내부 클래스의 인스턴스 변수)");

		}
		
//		 static void sTest(){
////			 The method sTest cannot be declared static;
////			 static methods can only be declared in a static or top level type
//		 }
		
	}
	
	public void usingClass() {
		inClass.inTest(); // 내부 클래스 변수를 사용하여 메서드 호출하기
	}
	
	static class InStaticClass {
		
		int inNum = 100;
		static int sInNum = 200;
		
		void inTest() { // 정적 클래스의 일반 메서드
			//num += 10;    // 외부 클래스의 인스턴스 변수는 사용할 수 없음.
			System.out.println("InStaticClass inNum = " + inNum + "(내부 클래스의 인스턴스 변수 사용)"); 
			System.out.println("InStaticClass sInNum = " + sInNum + "(내부 클래스의 스태틱 변수 사용)");
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 스태틱 변수 사용)");

		}
		
		static void sTest() { // 정적 클래스의 static method
			//num += 10;   // 외부 클래스의 인스턴스 변수는 사용할 수 없음.
			//inNum += 10; // 내부 클래스의 인스턴스 변수는 사용할 수 없음
			
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 스태틱 변수 사용)");
			System.out.println("InStaticClass sInNum = " + sInNum + "(내부 클래스의 스태틱 변수 사용)");

		}
	}
}












