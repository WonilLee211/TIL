package ch04;

public class CustomerTest {

	public static void main(String[] args) {
		
		Customer customerLee = new Customer(10010, "이순신");
		customerLee.bonusPoint = 1000;
		System.out.println(customerLee.showCustomerInfo());
		
		VIPCustomer customerKim = new VIPCustomer(10020, "김유신");
		customerKim.bonusPoint = 10000;
		System.out.println(customerKim.showCustomerInfo());
		
		int priceLee = customerLee.calcPrice(10000);
		int priceKim = customerKim.calcPrice(10000);
		
		System.out.println(customerLee.showCustomerInfo() + " 지불금액은 " + priceLee + "원 입니다.");
		System.out.println(customerKim.showCustomerInfo() + " 지불금액은 " + priceKim + "원 입니다.");
		
		Customer customerNo = new VIPCustomer(10030, "나몰라");
		customerNo.bonusPoint = 10000;
		int priceNo = customerNo.calcPrice(10000);
		System.out.println(customerNo.showCustomerInfo() + " 지불금액은 " + priceNo  + "원 입니다.");

	}
//	Customer(int, String) 생성자 호출
//	이순신님의 등급은 SILVER이며, 보너스 포인트는1000입니다
//	Customer(int, String) 생성자 호출
//	VIPCustomer(int, String) 생성자 호출
//	김유신님의 등급은 VIP이며, 보너스 포인트는10000입니다
//	이순신님의 등급은 SILVER이며, 보너스 포인트는1100입니다 지불금액은 10000원 입니다.
//	김유신님의 등급은 VIP이며, 보너스 포인트는10500입니다 지불금액은 9000원 입니다.
//	Customer(int, String) 생성자 호출
//	VIPCustomer(int, String) 생성자 호출
//	나몰라님의 등급은 VIP이며, 보너스 포인트는10500입니다 지불금액은 9000원 입니다.
}
