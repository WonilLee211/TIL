package ch16;

public class SuperLevel extends PlayerLevel{

	@Override
	public void run() {
		System.out.println("천천히 달립니다.");
		
	}

	@Override
	public void jump() {
		System.out.println("아주 높이 jump 합니다.");
		
	}

	@Override
	public void turn() {
		 System.out.println("turn 합니다.");
		
	}

	@Override
	public void showLevelMessage() {
		System.out.println("****** 고급자 레벨입니다. *******");
		
	}

}
