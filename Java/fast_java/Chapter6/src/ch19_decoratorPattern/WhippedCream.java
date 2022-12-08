package ch19_decoratorPattern;

public class WhippedCream extends Decorator{

	public WhippedCream(Coffee coffee) {
		super(coffee);
	}
	
	public void brewing() {
		System.out.println("Adding WhippedCream");
	}
}

