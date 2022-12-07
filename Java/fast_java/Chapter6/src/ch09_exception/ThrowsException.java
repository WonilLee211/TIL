package ch09_exception;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class ThrowsException {

	public Class loadClass(String fileName, String className) throws FileNotFoundException, ClassNotFoundException{
		FileInputStream fis = new FileInputStream(fileName); //FileNotFoundException 발생
		Class c = Class.forName(className);  //ClassNotFoundException 발생
		return c;
	}

	public static void main(String[] args) {

		ThrowsException test = new ThrowsException();
		
		try {
			test.loadClass("a.txt", "java.lang.String");
		
		}catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
//	java.io.FileNotFoundException: a.txt (지정된 파일을 찾을 수 없습니다)
//	at java.base/java.io.FileInputStream.open0(Native Method)
//	at java.base/java.io.FileInputStream.open(FileInputStream.java:216)
//	at java.base/java.io.FileInputStream.<init>(FileInputStream.java:157)
//	at java.base/java.io.FileInputStream.<init>(FileInputStream.java:111)
//	at Chapter6/ch09_exception.ThrowsException.loadClass(ThrowsException.java:9)
//	at Chapter6/ch09_exception.ThrowsException.main(ThrowsException.java:19)

}
