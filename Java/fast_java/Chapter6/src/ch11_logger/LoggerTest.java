package ch11_logger;

public class LoggerTest {

	public static void main(String[] args) {
		MyLogger myLogger = MyLogger.getLogger();
		
		myLogger.log("test");
	}
//	12월 07, 2022 8:13:25 오후 ch11_logger.MyLogger log
//	정보: test
//	12월 07, 2022 8:13:25 오후 ch11_logger.MyLogger log
//	경고: test
//	12월 07, 2022 8:13:25 오후 ch11_logger.MyLogger log
//	심각: test
}
