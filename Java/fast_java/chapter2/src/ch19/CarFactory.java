package ch19;

public class CarFactory {
	
	// private 생성자 선언
	private CarFactory() {}
	
	// 인스턴스 생성
	private static CarFactory instance = new CarFactory();
	
	// 외부에서 유일한 참조 메서드 선언
	public static CarFactory getInstance() {
		if (instance == null) {
			instance = new CarFactory();
		}
		return instance;
	}
	public Car createCar() {
		Car car1 = new Car();
		return car1;
	}
}
