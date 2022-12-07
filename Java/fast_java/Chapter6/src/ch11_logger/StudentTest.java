package ch11_logger;

public class StudentTest {

	public static void main(String[] args) {
		
		MyLogger myLogger = MyLogger.getLogger();
		
		String name = null;
		try{
			Student student = new Student(name);
			
		}catch( StudentNameFormatException e ){
			myLogger.warning(e.getMessage());
		}
		
		try{
			Student student = new Student("Edward Jon Kim Test");
		}catch ( StudentNameFormatException e){
			myLogger.warning(e.getMessage());
		}
		
		Student student = new Student("James");
	}
//	12월 07, 2022 8:17:20 오후 ch11_logger.MyLogger warning
//	경고: name must not be null
//	12월 07, 2022 8:17:20 오후 ch11_logger.MyLogger warning
//	경고: 이름이 너무 길어요
}
