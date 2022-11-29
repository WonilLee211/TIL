package ch09_reference_data_type;

public class StudentTest {

	public static void main(String[] args) {
		Student studentLee = new Student();
		
		studentLee.studentID = 100;
		studentLee.studentName = "이원일";
		studentLee.setKoreaSubject("국어", 90);
		studentLee.setMathSubject("수학", 100);
		
		studentLee.showStudentScore();
	}

}
