package ch09_reference_data_type;

public class Student {
	
	int studentID;
	String studentName;
	
	Subject korea = new Subject();
	Subject math = new Subject();
	
	public void setKoreaSubject(String name, int score) {
		korea.subjectName = name;
		korea.score = score;
	}
	
	public void setMathSubject(String name, int score) {
		math.subjectName = name;
		math.score = score;
	}
	
	public void showStudentScore() {
		int total = korea.score + math.score;
		System.out.println(studentName + " 학생의 총점은 " + total + " 점입니다.");
	}
}
