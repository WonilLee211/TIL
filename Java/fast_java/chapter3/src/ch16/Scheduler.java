package ch16;

public interface Scheduler {
	public default void getNextCall() {
		System.out.println("상담 전화를 순서대로 대기열에서 가져옵니다.");

	};
	public abstract void sendCallToAgent();
	
}
