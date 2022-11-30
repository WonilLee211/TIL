package annotation4;

public class SingleApply {
	
//	@SingleValue1(value="test")
//	@SingleValue2(name="test2")
	public void apply1() {}
	
//	@SingleValue1 // 불가능
//	@SingleValue2("test3") // 불가능
//	@SingleValue1("test3") // 가능, value만 생략 가능
//	@SingleValue3 // 가능, Default가 선언되어있음
	@SingleValue4 // 가능, Default가 선언되어있음
	public void apply2() {}
	
	
	
}

