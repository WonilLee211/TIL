package ch19_decoratorPattern;

public class Mocha extends Decorator{
	
	public Mocha(Coffee coffee) {
		super(coffee);
	}
	
	@Override
	public void brewing() {
		
		System.out.println("Adding Mocha Syrup");
	}
}