package ch6_GenericProgramming;

//  Object로 제네릭 클래스를 구현하는 경우 형변환을 해야 함
public class ThreeDPrinter{

	private Object material;
	
	public void setMaterial(Object material) {
		this.material = material;
	}
	
	public Object getMaterial() {
		return material;
	}
}
