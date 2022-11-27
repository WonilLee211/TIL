package ch10;

public class ConstantTest {

	public static void main(String[] args) {

		final int MAX_NUM = 100;
		final int MIN_NUM;
		
		MIN_NUM = 0;
		
		System.out.println(MAX_NUM); // 100
		System.out.println(MIN_NUM); // 0
//		MAX_NUM = 1000; // 에러 발생
	}

}
