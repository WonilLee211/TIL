package scoreEvaluationProgram;

import java.util.ArrayList;

public class Student {
	
	private int studentId;    		//학번
	private String studentName;		//이름
	private Subject majorSubject;	//중점 과목
	
	//학생의 성적 리스트 
	//addSubjectSocre() 메서드가 호출되면 리스트에 추가 됨
	private ArrayList<Score> scoreList = new ArrayList<Score>(); 
	
	// Student 생성자. 매개변수 : 아이디, 이름, 중점과목
	public Student( int studentId, String studentName, Subject majorSubject){
		this.studentId = studentId;
		this.studentName = studentName;
		this.majorSubject = majorSubject;
	}
	
	// 속성별 getter, setter
	public void addSubjectScore(Score score){
		scoreList.add(score);
	}
	
	public int getStudentId() {
		return studentId;
	}

	public void setStudentId(int studentId) {
		this.studentId = studentId;
	}

	public String getStudentName() {
		return studentName;
	}

	public void setStudentName(String studentName) {
		this.studentName = studentName;
	}

	public Subject getMajorSubject() {
		return majorSubject;
	}

	public void setMajorSubject(Subject majorSubject) {
		this.majorSubject = majorSubject;
	}

	public ArrayList<Score> getScoreList(){
		return scoreList;
	}
	
	public void setScoreList(ArrayList<Score> scoreList) {
		this.scoreList = scoreList;
	}

	
	
	
}
