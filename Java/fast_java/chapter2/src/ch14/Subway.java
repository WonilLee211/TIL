package ch14;

public class Subway {
	int lineNumber;
	int passengerCount;
	int money;
	
	public Subway(int busNumber) {
		this.lineNumber = busNumber;
	}
	public void take(int money) {
		this.money += money;
		this.passengerCount ++;
	}
	public void ShowSubwayInfo() {
		System.out.println(lineNumber + "라인 지하철의 승객은 " + passengerCount + "명 이고, 수입은 " + money + "원 입니다");
	}

}
