package ch10_access_modifier;

public class BirthDayTest {

	public static void main(String[] args) {
		
		BirthDay date =  new BirthDay();
		
		date.setDay(30);
		date.setMonth(11);
		date.setYear(2022);
		
//		date.month = 100; // 이런 방식은 private으로 걸러냄
	
	}
}
