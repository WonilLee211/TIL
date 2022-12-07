package ch09_exception;

public class AutoCloseTest {

	public static void main(String[] args) {

		AutoCloseObj obj = new AutoCloseObj();
    	try (obj){
			throw new Exception();
		}catch(Exception e) {
			System.out.println("예외 부분 입니다");
		}
    	
//    	리소스가 close() 되었습니다
//    	예외 부분 입니다
	}
}
