package ch14;

public class TakeTransTest {

	public static void main(String[] args) {
		Student James = new Student("James", 5000);
		Student Tomas = new Student("Tomas", 10000);
		Student Edward = new Student("Edward", 20000);
		
		Bus bus100 = new Bus(100);
		Subway subwayGreen = new Subway(2);
		Taxi taxi1 = new Taxi(4885);
		
		// 객체를 파라미터로 전달
		James.takeBus(bus100);
		Tomas.takeSubway(subwayGreen);
		Edward.takeTaxi(taxi1, 10000);
		
		James.showInfo();
		Tomas.showInfo();
		Edward.showInfo();
	
//		James님의 남은 돈은 4000원입니다.
//		Tomas님의 남은 돈은 8800원입니다.
//		Edward님의 남은 돈은 10000원입니다.
	}

}
