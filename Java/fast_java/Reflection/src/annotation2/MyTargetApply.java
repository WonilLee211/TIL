package annotation2;

@MyTarget
public class MyTargetApply {
	@MyTarget
	private String msg;
	
	@MyTarget
	public void call() {
		
	}
	
	public void test(@MyTarget String msg) {
		int val = 100;
	}
	
}
