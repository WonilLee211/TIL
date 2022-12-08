package scoreEvaluationProgram;

public class TestMain {
	
	School goodSchool = School.getInstance();
	Subject korean;
	Subject math;
	Subject dance;

	GenerateGradeReport gradeReport = new GenerateGradeReport();
	
	public static void main(String[] args) {
		
		TestMain test = new TestMain();
		
		test.creatSubject();
		test.createStudent();
		
		String report = test.gradeReport.getReport(); //성적 결과 생성
		System.out.println(report); // 출력
		
	}
	//테스트 과목 생성
	public void creatSubject(){
		
		korean = new Subject("국어", Define.KOREAN);
		math = new Subject("수학", Define.MATH);
		dance = new Subject("방송댄스", Define.DANCE);
		
		dance.setGradeType(Define.PF_TYPE);

		goodSchool.addSubject(korean);
		goodSchool.addSubject(math);
		goodSchool.addSubject(dance);

	}
	
	//테스트 학생 생성
	public void createStudent(){
		
		Student student1 = new Student(211213, "강감찬", korean  );
		Student student2 = new Student(212330, "김유신", math  );
		Student student3 = new Student(201518, "신사임당", korean  );
		Student student4 = new Student(202360, "이순신", korean  );
		Student student5 = new Student(201290, "홍길동", math );
		
		goodSchool.addStudent(student1);
		goodSchool.addStudent(student2);
		goodSchool.addStudent(student3);
		goodSchool.addStudent(student4);
		goodSchool.addStudent(student5);

		korean.register(student1);
		korean.register(student2);
		korean.register(student3);
		korean.register(student4);
		korean.register(student5);
		
		math.register(student1);
		math.register(student2);
		math.register(student3);
		math.register(student4);
		math.register(student5);
		
		//세 명만 등록
		dance.register(student1);
		dance.register(student2);
		dance.register(student3);

		
		addScoreForStudent(student1, korean, 95); 
		addScoreForStudent(student1, math, 56);	
		
		addScoreForStudent(student2, korean, 95); 
		addScoreForStudent(student2, math, 95);	
		
		addScoreForStudent(student3, korean, 100); 
		addScoreForStudent(student3, math, 88);	
		
		addScoreForStudent(student4, korean, 89); 
		addScoreForStudent(student4, math, 95);	
		
		addScoreForStudent(student5, korean, 85); 
		addScoreForStudent(student5, math, 56);
		
		addScoreForStudent(student1, dance, 95);	
		addScoreForStudent(student2, dance, 85); 
		addScoreForStudent(student3, dance, 55);

	}
	
	//과목별 성적 입력
	public void addScoreForStudent(Student student, Subject subject, int point){
		
		Score score = new Score(student.getStudentId(), subject, point);
		student.addSubjectScore(score);
		
	}

//	-------------------------------------
//		국어 수강생 학점 		
//	 이름  |  학번  |중점과목| 점수   
//	-------------------------------------
//	강감찬 | 211213 | 국어	 | 95:S | 
//	-------------------------------------
//	김유신 | 212330 | 수학	 | 95:A | 
//	-------------------------------------
//	신사임당 | 201518 | 국어	 | 100:S | 
//	-------------------------------------
//	이순신 | 202360 | 국어	 | 89:B | 
//	-------------------------------------
//	홍길동 | 201290 | 수학	 | 85:B | 
//	-------------------------------------
//	
//	-------------------------------------
//		수학 수강생 학점 		
//	 이름  |  학번  |중점과목| 점수   
//	-------------------------------------
//	강감찬 | 211213 | 국어	 | 56:D | 
//	-------------------------------------
//	김유신 | 212330 | 수학	 | 95:S | 
//	-------------------------------------
//	신사임당 | 201518 | 국어	 | 88:B | 
//	-------------------------------------
//	이순신 | 202360 | 국어	 | 95:A | 
//	-------------------------------------
//	홍길동 | 201290 | 수학	 | 56:F | 
//	-------------------------------------
	
	
//	-------------------------------------
//		방송댄스 수강생 학점 		
//	 이름  |  학번  |중점과목| 점수   
//	-------------------------------------
//	강감찬 | 211213 | 국어	 | 95:P | 
//	-------------------------------------
//	김유신 | 212330 | 수학	 | 85:P | 
//	-------------------------------------
//	신사임당 | 201518 | 국어	 | 55:F | 
//	-------------------------------------
}
