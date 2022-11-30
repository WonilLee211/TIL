package ch14;

public class Taxi {
	int TaxiNumber;
	int money;
	
	public Taxi(int TaxiNumber) {
		this.TaxiNumber = TaxiNumber;
	}
	public void take(int money) {
		this.money += money;
	}
	public void ShowTaxiInfo() {
		System.out.println("챠량번호 " + TaxiNumber + " 택시의 수익은 "+ money + "원 입니다");
	}
}
