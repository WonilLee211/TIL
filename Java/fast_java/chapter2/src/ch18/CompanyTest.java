package ch18;

public class CompanyTest {

	public static void main(String[] args) {
		Company company1 = Company.getInstance();
		Company company2 = Company.getInstance();
		
		System.out.println(company1);
		System.out.println(company2);
//		ch18.Company@7c30a502
//		ch18.Company@7c30a502
		
	}

}
