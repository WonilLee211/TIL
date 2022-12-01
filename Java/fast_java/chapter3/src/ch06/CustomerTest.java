package ch06;

import java.util.ArrayList;

public class CustomerTest {

	public static void main(String[] args) {
		
		ArrayList<Customer> customerList = new ArrayList<Customer>();
		
		Customer customerLee = new Customer(10010, "이순신");
		Customer customerShin = new Customer(10020, "신사임당");
		Customer customerHong = new GoldCustomer(10030, "홍길동");
		Customer customerYul = new GoldCustomer(10040, "이율곡");
		Customer customerKim = new VIPCustomer(10050, "김유신", 12345);
		
		customerList.add(customerLee);
		customerList.add(customerShin);
		customerList.add(customerHong);
		customerList.add(customerYul);
		customerList.add(customerKim);
		
		System.out.println("====== 고객 정보 출력 =======");
		
		for( Customer customer : customerList){
			System.out.println(customer.showCustomerInfo());
		}
		
		System.out.println("====== 할인율과 보너스 포인트 계산 =======");
		
		int price = 10000;
		for( Customer customer : customerList){
			int cost = customer.calcPrice(price);
			System.out.println(customer.getCustomerName() +" 님이 " +  + cost + "원 지불하셨습니다.");
			System.out.println(customer.getCustomerName() +" 님의 현재 보너스 포인트는 " + customer.bonusPoint + "점입니다.");
		}
	}

//
//====== 고객 정보 출력 =======
//이순신님의 등급은 SILVER이며, 보너스 포인트는0입니다
//신사임당님의 등급은 SILVER이며, 보너스 포인트는0입니다
//홍길동님의 등급은 GOLD이며, 보너스 포인트는0입니다
//이율곡님의 등급은 GOLD이며, 보너스 포인트는0입니다
//김유신님의 등급은 VIP이며, 보너스 포인트는0입니다 담당 상담원 번호는 12345입니다
//====== 할인율과 보너스 포인트 계산 =======
//이순신 님이 10000원 지불하셨습니다.
//이순신 님의 현재 보너스 포인트는 100점입니다.
//신사임당 님이 10000원 지불하셨습니다.
//신사임당 님의 현재 보너스 포인트는 100점입니다.
//홍길동 님이 9000원 지불하셨습니다.
//홍길동 님의 현재 보너스 포인트는 200점입니다.
//이율곡 님이 9000원 지불하셨습니다.
//이율곡 님의 현재 보너스 포인트는 200점입니다.
//김유신 님이 9000원 지불하셨습니다.
//김유신 님의 현재 보너스 포인트는 500점입니다.

}
