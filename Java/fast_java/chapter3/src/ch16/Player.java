package ch16;

public class Player {
	PlayerLevel level;

	
	public void getLevel() {
		
		level.showLevelMessage();
		
	}
	
	public void updateLevel(PlayerLevel playerLevel) {
		
		level = playerLevel;
	}
	
	final public void play(int count) {
		getLevel();
		level.go(count);
		
	}
	
}
