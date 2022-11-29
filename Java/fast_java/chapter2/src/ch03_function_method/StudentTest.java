package ch03_function_method;

public class StudentTest {

	public static void main(String[] args) {
		
		Student studentLee = new Student();
		studentLee.studentName = "이원일";
		studentLee.address = "구미";
		
		Student studentKim = new Student();
		studentKim.studentName = "김유신";
		studentKim.address = "경주";
		
		studentKim.showStudentInfo();
		
		System.out.println(studentLee);
		System.out.println(studentKim);
		
//		김유신,경주
//		ch03_function_method.Student@7c30a502
//		ch03_function_method.Student@49e4cb85

	}
}
