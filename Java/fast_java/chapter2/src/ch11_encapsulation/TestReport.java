package ch11_encapsulation;

public class TestReport {

	public static void main(String[] args) {

		MakeReport report = new MakeReport();
		String builder = report.getReport();
		System.out.println(builder);
		
//		===========================================
//		  이름	   주소 		  전화번호  
//		===========================================
//		James 	Seoul Korea 010-2222-3333
//		Tomas 	NewYork US 	010-7777-0987
//		===========================================



	}

}
