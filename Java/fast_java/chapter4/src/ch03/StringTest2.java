package ch03;

public class StringTest2 {

	public static void main(String[] args) {
		String java = new String("java");
		String android = new String("android");
		System.out.println(System.identityHashCode(java)); //93122545
		
		java = java.concat(android);
		
		System.out.println(java); // javaandroid
		System.out.println(System.identityHashCode(java)); // 2083562754
		

	}

}
