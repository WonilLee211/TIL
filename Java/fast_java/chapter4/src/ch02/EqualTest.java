package ch02;

public class EqualTest {

	public static void main(String[] args) throws CloneNotSupportedException {
		Student Lee = new Student(100, "Lee");
		Student Lee2 = Lee;
		Student Shun = new Student(100, "Lee");
		
		System.out.println(Lee == Shun); // false
		System.out.println(Lee.equals(Shun)); // true
		
		System.out.println(Lee.hashCode()); // 100
		System.out.println(Shun.hashCode()); // 100
			
		Integer i1 = new Integer(100);
		Integer i2 = new Integer(100);
		
		System.out.println(i1.equals(i2)); // true
		System.out.println(i1.hashCode()); // 100
		System.out.println(i2.hashCode()); // 100
		
		System.out.println(System.identityHashCode(i1)); // 2083562754
		System.out.println(System.identityHashCode(i2)); // 1239731077
		
		
	    Student Lee3 = (Student)Lee.clone();
		System.out.println(System.identityHashCode(Lee)); // 557041912
		System.out.println(System.identityHashCode(Lee3)); // 1134712904
	}
}
