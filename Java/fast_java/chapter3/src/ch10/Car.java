package ch10;

public abstract class Car {
	
	public abstract void drive();
	public abstract void stop();
	
	public void startCar() {
		
		System.out.println("시동을 켭니다.");
		
	}
	
	public void turnOff() {
		System.out.println("시동을 끕니다.");
	}
	
//	template method로 하위클래스의 전체적인 흐름을 정의하고 재정의 못하도록 함
	final void run() {
		startCar();
		drive();
		stop();
		turnOff();
	}
}
