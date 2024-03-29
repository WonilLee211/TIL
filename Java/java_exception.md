# 08.예외 처리는 왜 해야 하나? 자바에서 제공되는 클래스들

## 프로그램에서의 오류

- 컴파일 오류(compile error) 

  프로그램 코드 작성 중 발생하는 **문법적 오류**

  최근에는 개발 환경(eclipse)에서 대부분의 컴파일 오류는 detection 됨

- **실행 오류(runtime error)** 

  실행 중인 프로그램이 의도 하지 않은 동작(bug)을 하거나 프로그램이 중지 되는 오류

  **실행 오류는 비정상 종료가 되는 경우 시스템의 심각한 장애를 발생할 수 있음**

## 예외 처리의 중요성

- 프로그램의 **비정상 종료를 피하여** 시스템이 원할이 실행되도록 함
  - **런타임 에러를 피하도록 함**

- 실행 오류가 발생한 경우 오류의 과정을 재현하는 것은 현실적으로 힘들다

- 오류가 발생한 경우 log를 남겨서 추후 log 분석을 통해 그 원인을 파악하여 bug를 수정하는 것이 중요

## 오류와 예외 클래스

- **시스템 오류(error)** : 가상 머신에서 발생, 프로그래머가 처리 할 수 없는 오류임

   동적 메모리가 없는 경우, 스택 메모리 오버플로우등

- **예외(Exception)** :프로그램에서 제어 할 수 있는 오류
  
  읽어들이려는 파일이 존재하지 않거나, 네트웍이나 DB연결이 안되는 경우등

- **자바는 안전성이 중요한 언어**로 대부분 프로그램에서 발생하는 **오류에 대해 문법적으로 예외 처리를 해야함**

![error.png](./img/error1.png)  

## 예외 클래스들

- 모든 예외 클래스의 최상위 클래스는 Exception 클래스

![exception1](./img/exception1.png)

- 자바에서는 다양한 예외들에 대해 그 처리를 위한 클래스가 제공되고 있음

![exception2](./img/exception2.png)

- Arithmetic Exception :정수를 0 으로 나눈 경우 발생

- NullPointerException : 초기화 되지 않은 Object를 사용하는 경우

```java
Dog d = null;
System.out.println(dog);
```

- ArrayIndexOutOfBoundsException :배열의 크기를 넘어선 위치를 참조하려는 경우

- FileNotFoundException :참조하는 파일이 지정된 위치에 존재하지 않는 경우

- ClassNotFoundException :

```java
Class.forName(“sis.studentinfo.Student”); //클래스가 로드되지 않은 경우
```

- InterruptedException :Thread.sleep(), join(). Object의 wait()로 non-runnable 상태인 thread를 Runnable하게 만들 수 있도록 사용할 수 있음



# 09. 예외 처리하기와 미루기

## try-catch 문

- try 블록에는 예외가 발생할 가능성이 있는 코드를 작성하고 try 블록 안에서 예외가 발생하믄 경우 catch 블록이 수행됨

![try](./img/try.png)

- 프로그래머가 예외를 처리해줘야 하는 예 (배열의 오류 처리)
```java
public class ArrayExceptionHandling {

	public static void main(String[] args) {
		int[] arr = {1,2,3,4,5};
		try{
			for(int i=0; i<=5; i++){
				System.out.println(arr[i]);
			}
		}catch(ArrayIndexOutOfBoundsException e){
			System.out.println(e);
		}
		System.out.println("비정상 종료되지 않았습니다.");
	}
}
```

- 실행환경이 SE 15버전일 때 import에러 발생
  - 현재는 SE16버전으로 설정 후 정상 실행

## try-catch-finally 문

- finally 블럭에서 파일를 닫거나 네트웍을 닫는 등의 리소스 해제 구현을 함

- **try{} 블럭이 수행되는 경우, finally{} 블럭은 항상 수행 됨**

- 여러 개의 예외 블럭이 있는 경우 각각에서 리소스를 해제하지 않고 finally 블록에서 해제하도록 구현함

- 컴파일러에 의해 예외가 처리 되는 예 (파일 에러 처리)

```java
package ch09_exception;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FileExceptionHandling {

	public static void main(String[] args) {
		
		FileInputStream fis = null;
		try {
			fis = new FileInputStream("a.txt");
		} catch (FileNotFoundException e) {
			System.out.println(e);
			//return;
		}finally{
			if(fis != null){
				try {
					fis.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			System.out.println("항상 수행 됩니다.");
		}
		System.out.println("여기도 수행됩니다.");

//		java.io.FileNotFoundException: a.txt (지정된 파일을 찾을 수 없습니다)
//		항상 수행 됩니다.
//		여기도 수행됩니다.
	}
}

```

## try-with-resources문

- 리소스를 사용하는 경우 close() 하지 않아도 자동으로 해제 되도록 함

- 자바 7부터 제공되는 구문

- **리소스를 try() 내부에서 선언해야만 함**

- close()를 명시적으로 호출하지 않아도 try{}블록에서 열린 리소스는 정상적인 경우나 예외가 발생한 경우 **모두 자동으로 해제됨**

- 해당 리소스 클래스가 **AutoCloseable 인터페이스를 구현 해야 함**

  - 구현한 클래스 객체를 try 매개변수로 전달해줘야 함

- **FileInputStream의 경우에는 AutoCloseable을 구현하고 있음**

- **자바 9 부터 리소스는 try() 외부에서 선언하고 변수만을 try(obj) 와 같이 사용할 수 있음** 

![auto](./img/auto.png)

- AutoCloseable인터페이스 구현 실습

```java
public class AutoCloseObj implements AutoCloseable{

	@Override
	public void close() throws Exception {
		System.out.println("리소스가 close() 되었습니다");
	}
}
```

```java
package ch09_exception;

public class AutoCloseTest {

	public static void main(String[] args) {

		AutoCloseObj obj = new AutoCloseObj();
    	try (obj){
			throw new Exception();
		}catch(Exception e) {
			System.out.println("예외 부분 입니다");
		}
    	
//    	리소스가 close() 되었습니다
//    	예외 부분 입니다
	}
}

```

## 예외 처리 미루기

- 예외 처리는 예외가 발생하는 문장에서 try-catch 블록으로 처리하는 방법과 이를 사용하는 부분에서 처리하는 방법 두 가지가 있음

- `throws`를 이용하면 예외가 발생할 수 있는 부분을 사용하는 문장에서 예외를 처리할 수 있음


```java
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

```

## 하나의 try{}블록에서 예외가 여러개 발생하는 경우

- 여러개의 예외가 발생하는 경우 예외를 묶어서 하나의 방법으로 처리할 수도 있고,

```java
	try {
	test.loadClass("a.txt", "java.lang.String");
	} catch (FileNotFoundException | ClassNotFoundException e) {
		e.printStackTrace();
	}
```

- 각각의 예외를 따로 처리할 수도 있음

```java
	try {
		test.loadClass("a.txt", "java.lang.String");
	
	}catch (FileNotFoundException e) {
		e.printStackTrace();
	} catch (ClassNotFoundException e) {
		e.printStackTrace();
	}catch (Exception e) {
		e.printStackTrace();
	}
```
- Exception 클래스를 활용하여 defualt 처리를 할 때 Exception 블록은 맨 마지막에 위치해야 함


# 10. 사용자 정의 예외 클래스와 그 활용

## 사용자 정의 예외 클래스 구현하기

- 자바에서 제공되는 예외 클래스외에 프로그래머가 직접 만들어야 하는 예외가 있을 수 있음

- 기존 예외 클래스중 **가장 유사한 예외 클래스에서 상속 받아 사용자 정의 예외 클래스를 만든다**.

- **기본적으로 Exception 클래스를 상속**해서 만들 수 있음

## 패스워드에 대한 예외 처리 하기

- 패스워드를 입력할 때 다음과 같은 경우 오류처리를 합니다.

    비밀번호는 null일 수 없습니다.

    비밀번호의 길이는 5이상입니다.

    비밀번호는 문자로만 이루어져서는 안됩니다.(하나이상의 숫자나 특수문자를 포함)


```java
public class PasswordException extends IllegalArgumentException{
	
	public PasswordException(String message) {
		super(message);
	}
}
```


```java
public class PasswordTest {

	private String password;
	
	public String getPassword(){
		return password;
	}
	
	public void setPassword(String password) throws PasswordException{
		
		if(password == null){
			throw new PasswordException("비밀번호는 null 일 수 없습니다");
		}
		else if( password.length() < 5){
			throw new PasswordException("비밀번호는 5자 이상이어야 합니다.");
		}
		else if (password.matches("[a-zA-Z]+")){
			throw new PasswordException("비밀번호는 숫자나 특수문자를 포함해야 합니다.");
		}
		
		this.password = password;
	}
	
	public static void main(String[] args) {

		PasswordTest test = new PasswordTest();
		String password = null;
		try {
			test.setPassword(password);
			System.out.println("오류 없음1");
		} catch (PasswordException e) {
			System.out.println(e.getMessage());
		}
		
		password = "abcd";
		try {
			test.setPassword(password);
			System.out.println("오류 없음2");
		} catch (PasswordException e) {
			System.out.println(e.getMessage());
		}
		
		password = "abcde";
		try {
			test.setPassword(password);
			System.out.println("오류 없음3");
		} catch (PasswordException e) {
			System.out.println(e.getMessage());
		}
		
		password = "abcde#1";
		try {
			test.setPassword(password);
			System.out.println("오류 없음4");
		} catch (PasswordException e) {
			System.out.println(e.getMessage());
		}
	}
}
```



