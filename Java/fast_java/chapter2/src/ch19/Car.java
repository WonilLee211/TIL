package ch19;

public class Car {
	
	private int carNum;
	private static int serialNumber = 10001;
	
	public Car() {
		this.carNum = Car.serialNumber++;
	}
	
	public int getCarNum() {
		return this.carNum;
	}
	
}
