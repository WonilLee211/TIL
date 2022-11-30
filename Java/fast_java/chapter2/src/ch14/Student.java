package ch14;

public class Student {
	String name;
	int grade;
	int money;
	
	public Student(String name, int money) {
		this.name = name;
		this.money = money;
	}
	public void takeBus(Bus bus) {
		bus.take(1000);
		money -= 1000;
	}
	public void takeSubway(Subway subway) {
		subway.take(1200);
		money -= 1200;
	}
	public void takeTaxi(Taxi taxi, int fee) {
		taxi.take(fee);
		money -= fee;
	}
	public void showInfo() {
		System.out.println(name + "님의 남은 돈은 " + money + "원입니다.");
	}
}
