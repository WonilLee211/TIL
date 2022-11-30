package reflection;

public class test01 {

	public static void main(String[] args) {
		try {
			exam();
		}catch (ClassNotFoundException e) {
			e.printStackTrace();
		}

	}
	
//	클래스를 접근하는 3가지 방법
	private static void exam() throws ClassNotFoundException {
		
		// 1. 클래스 이름.class	
		Class<?> clz = Dog.class;
		
		// 2. Class.forName("패키지 포함 클래스 명");
		Class<?> clz2 = Class.forName("reflection.Dog");
		
		// 3. 객체(인스턴스).getClass()
		Dog d = new Dog();
		Class<?> clz3 = d.getClass();
		
		System.out.println(clz == clz2); //true
		System.out.println(clz2 == clz3); // true
		
		String name = clz.getName(); // 기본은 풀패키지명
		String sName = clz.getSimpleName();
		
		System.out.println(name); // reflection.Dog
		System.out.println(sName); // Dog

		
	}

}
