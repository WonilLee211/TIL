package ch01_innerClass;

public class InnerTest {

	public static void main(String[] args) {
		
		OutClass outClass = new OutClass();
		System.out.println("외부 클래스 이용하여 내부 클래스 기능 호출");
		outClass.usingClass();
		System.out.println();
//		외부 클래스 이용하여 내부 클래스 기능 호출
//		OutClass num = 10(외부 클래스의 인스턴스 변수)
//		OutClass sNum = 20(외부 클래스의 스태틱 변수)
//		InClass inNum = 100(내부 클래스의 인스턴스 변수)
		
		 // 외부 클래스를 이용하여 내부 클래스 생성
		OutClass.InClass inClass = outClass.new InClass();
		System.out.println("외부 클래스 변수를 이용하여 내부 클래스 생성");
		inClass.inTest();
//		외부 클래스 변수를 이용하여 내부 클래스 생성
//		OutClass num = 10(외부 클래스의 인스턴스 변수)
//		OutClass sNum = 20(외부 클래스의 스태틱 변수)
//		InClass inNum = 100(내부 클래스의 인스턴스 변수)
		
		//외부 클래스 생성하지 않고 바로 정적 내부 클래스 생성
		OutClass.InStaticClass sInClass = new OutClass.InStaticClass();
		System.out.println("정적 내부 클래스 일반 메서드 호출");
		sInClass.inTest();
		System.out.println();
//		정적 내부 클래스 일반 메서드 호출
//		InStaticClass inNum = 100(내부 클래스의 인스턴스 변수 사용)
//		InStaticClass sInNum = 200(내부 클래스의 스태틱 변수 사용)
//		OutClass sNum = 20(외부 클래스의 스태틱 변수 사용)

		
		System.out.println("정적 내부 클래스의 스태틱 메소드 호출");
		OutClass.InStaticClass.sTest();
//		정적 내부 클래스의 스태틱 메소드 호출
//		OutClass sNum = 20(외부 클래스의 스태틱 변수 사용)
//		InStaticClass sInNum = 200(내부 클래스의 스태틱 변수 사용)
	}

}
