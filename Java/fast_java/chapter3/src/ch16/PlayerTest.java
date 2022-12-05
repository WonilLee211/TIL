package ch16;

public class PlayerTest {

	public static void main(String[] args) {
		Player player = new Player();
		
		int count = 0;
		
		BeginnerLevel beginnerLevel = new BeginnerLevel(); count++;
		player.updateLevel(beginnerLevel);
		player.play(count);
		
		AdvancedLevel advancedLevel = new AdvancedLevel(); count++;
		player.updateLevel(advancedLevel);
		player.play(count);
		
		SuperLevel superLevel = new SuperLevel(); count++;
		player.updateLevel(superLevel);
		player.play(count);
		
		
	}
//	****** 초급자 레벨입니다. *******
//	천천히 달립니다.
//	jump 못하지롱
//	turn 못하지롱
//	****** 중급자 레벨입니다. *******
//	빨리 달립니다.
//	높이 jump합니다.
//	높이 jump합니다.
//	turn 못하지롱
//	****** 고급자 레벨입니다. *******
//	천천히 달립니다.
//	아주 높이 jump 합니다.
//	아주 높이 jump 합니다.
//	아주 높이 jump 합니다.
//	turn 합니다.

}
