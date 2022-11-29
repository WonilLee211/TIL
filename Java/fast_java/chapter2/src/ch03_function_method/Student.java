package ch03_function_method;

public class Student {
	
	public int sdudentID;
	public String studentName;
	public String address;
	
	public void showStudentInfo() {
		System.out.println(studentName + "," + address);
		
	}
	
	public String getStudentName() {
		return studentName;
	}

}
