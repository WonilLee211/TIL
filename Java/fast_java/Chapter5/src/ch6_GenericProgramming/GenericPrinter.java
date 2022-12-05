package ch6_GenericProgramming;

// 제네릭 클래스 정의
// T : 자료형 매개변수 - 클래스를 사용하는 시점에 실제 사용할 자료형을 지정.
public class GenericPrinter<T> {
	private T material;
	
	public void setMaterial(T material) {
		this.material = material;
	}
	
	public T getMaterial() { // T 자료형을 반환하는 제네릭 메서드
		return material;
	}
	
	public String toString(){
		return material.toString();
	}
}
