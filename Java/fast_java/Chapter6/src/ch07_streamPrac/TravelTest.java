package ch07_streamPrac;

import java.util.ArrayList;
import java.util.List;

public class TravelTest {

	public static void main(String[] args) {
		TravelCustomer customerLee = new TravelCustomer("이순신", 40, 100);
		TravelCustomer customerKim = new TravelCustomer("김유신", 20, 100);
		TravelCustomer customerHong = new TravelCustomer("홍길동", 13, 50);
		
		List<TravelCustomer> customerList = new ArrayList<>();
		customerList.add(customerLee);
		customerList.add(customerHong);
		customerList.add(customerKim);
		
		System.out.println("== 고객 명단 추가된 순서대로 출력 ==");
		customerList.stream().forEach(s -> System.out.println(s));
		customerList.stream().map(s -> s.getName()).forEach(s-> System.out.println(s));
//		== 고객 명단 추가된 순서대로 출력 ==
//		name: 이순신 age: 40 price: 100
//		name: 홍길동 age: 13 price: 50
//		name: 김유신 age: 20 price: 100
//		이순신
//		홍길동
//		김유신
		
//		int total = customerList.stream().map(s->s.getPrice()).sum();
//		The method sum() is undefined for the type Stream<Integer>
		int total = customerList.stream().mapToInt(s->s.getPrice()).sum();
		System.out.println("총 여행 비용은 :" + total + "입니다");
//		총 여행 비용은 :250입니다
		
		System.out.println("== 20세 이상 고객 명단 정렬하여 출력 ==");
		customerList.stream().filter(c-> c.getAge() >= 20).map(c -> c.getName()).sorted().forEach(c -> System.out.println(c));
//		== 20세 이상 고객 명단 정렬하여 출력 ==
//		김유신
//		이순신
	}
}
