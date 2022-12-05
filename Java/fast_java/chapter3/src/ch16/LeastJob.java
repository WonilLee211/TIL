package ch16;

public class LeastJob implements Scheduler {
	
	@Override
	public void sendCallToAgent() {
		System.out.println("대기가 적은 상담원에 우선적으로 상담전화를 배치합니다.");
		
	}
	

}
