package ch02;

public class CustomerTest {

	public static void main(String[] args) {
		
		Customer customerLee = new Customer();
		customerLee.setCustomerName("이원일");
		customerLee.setCustomerID(10010);
		customerLee.bonusPoint = 1000;
		System.out.println(customerLee.showCustomerInfo());
//		이원일님의 등급은 silver이며, 보너스 포인트는1000입니다
		
		VIPCustomer customerKim = new VIPCustomer();
		customerKim.setCustomerName("김유신");
		customerKim.setCustomerID(10020);
		customerKim.bonusPoint = 10000;
		System.out.println(customerKim.showCustomerInfo());
//		김유신님의 등급은 VIP이며, 보너스 포인트는10000입니다


	}

}
