# 01. Object 클래스 - 모든 클래스의 최상위 클래스


## java.lang 패키지

- 프로그래밍시 import 하지 않아도 자동으로 imort됨

- import.java.lang.*;

- 많이 사용하는 기본 클래스들이 속한 패키지

- String, Integer, System...


## 모든 클래스는 Object 클래스를 상속 받는다

- java.lang.Object 클래스

- 모든 클래스의 최상위 클래스는

- 모든 클래스는 Object에서 상속받고, Object 클래스의 메서드 중 일부는 재정의해서 사용할 수 있음

- 컴파일러가 extends Object를 추가함 
  
  **class Student === class Student extends Object**

## toString() 메서드

- 객체의 정보를 String으로 바꾸어서 사용할 때 쓰임
  
- 객체를 출력할 때 출력방식을 정하는 메서드
  
- String이나 Integer 클래스는 이미 재정의 되어 있음

- toString()메서드 재정의 예

```java
class Book{
	
	private String title;
	private String author;
	
	public Book(String title, String author) {
		this.title = title;
		this.author = author;
	}
	
	public String toString() {
		return title + "," + author;
	}
	
}

public class BookTest {

	public static void main(String[] args) {

		Book book = new Book("데미안", "헤르만 헤세");
		
		System.out.println(book);
	}
}
```


# 02. Object 클래스의 메서드 활용

## equals() 메서드

- 두 인스턴스의 **주소 값을 비교**하여 true/false를 반환

- 재정의 하여 두 인스턴스가 논리적으로 동일함의 여부를 구현함

- **인스턴스가 다르더라도 논리적으로 동일한 경우 true를 반환하도록 재정의 할 수 있음**

  (같은 학번, 같은 사번, 같은 아이디의 회원...)
  
## hashCode() 메서드

- hashCode()는 **인스턴스의 저장 주소를 반환함**

- 힙메모리에 인스턴스가 저장되는 방식이 hash 방식

- hash : 정보를 저장, 검색하는 자료구조

- 자료의 특정 값(키 값)에 대한 저장 위치를 반환해주는 해시 함수를 사용

![hash.png](./img/hash.png)

- 두 인스턴스가 같다는 것은?

  두 인스턴스에 대한 equals()의 반환 값이 true
  동일한 hashCode() 값을 반환

- 논리적으로 동일함을 위해 equals() 메서드를 재정의 하였다면 hashCode()메서드도 재정의 하여 동일한 hashCode 값이 반환되도록 한다

Student.java
```java
public class Student {

	private int studentId;
	private String studentName;

	public Student(int studentId, String studentName)
	{
		this.studentId = studentId;
		this.studentName = studentName;
	}
	
	public boolean equals(Object obj) {
		if( obj instanceof Student) {
			Student std = (Student)obj;
			if(this.studentId == std.studentId )
				return true;
			else return false;
		}
		return false;
		
	}
	
	@Override
	public int hashCode() {
		return studentId;
	}
}
```

EqualTest.java
```java
package ch02;

public class EqualTest {

	public static void main(String[] args) {
		Student Lee = new Student(100, "Lee");
		Student Lee2 = Lee;
		Student Shun = new Student(100, "Lee");
		
		System.out.println(Lee == Shun); // false
        // 같은 클래스에서 생성된 인스턴스이고 StudentId가 같을 때 true반환
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

	}
}

```

## clone() 메서드

- 객체의 원본을 복제하는데 사용하는 메서드

- 생성과정의 복잡한 과정을 반복하지 않고 복제 할 수 있음

- clone()메서드를 사용하면 객체의 정보(멤버 변수 값등...)가 동일한 또 다른 인스턴스가 생성되는 것이므로, 객체 지향 프로그램에서의 정보 은닉, 객체 보호의 관점에서 위배될 수 있음

- 해당 클래스의 clone() 메서드의 사용을 허용한다는 의미로 cloneable 인터페이스를 명시해 줌

- clone()를 오버라이딩하면 deep copy를 할 수 있다.

- 이를 위해서는 3가지 조건이 필요하다.

1. Cloneable 인터페이스를 implements하기
2. clone() 메소드를 override하기
3. try - catch 구문을 이용해 CloneNotSupportedException 던지기

Student.java
```java
public class Student implements Cloneable{

    .......

	@Override
	protected Object clone() throws CloneNotSupportedException {
		// TODO Auto-generated method stub
		return super.clone();
	}
}
```

EqualTest.java
```java
    Student Lee3 = (Student)Lee.clone();
	System.out.println(System.identityHashCode(Lee));
	System.out.println(System.identityHashCode(Lee3));
		
```

# 03. String, StringBuilder, StringBuffer 클래스, text block

## String 클래스

- String 선언하기
```java
    String str1 = new String("abc");
    String str2 = "abc";
```

- 힙 메모리에 인스턴스로 생성되는 경우와 상수 풀(constant pool)에 있는 주소를 참조하는 두 가지 방법

- 힙 메모리는 생성될때마다 다른 주소 값을 가지지만, 상수 풀의 문자열은 모두 같은 주소 값을 가짐

```java
package ch03;

public class StringTest {

	public static void main(String[] args) {
		String str1 = new String("abc");
		String str2 = new String("abc");

		System.out.println(str1 == str2); // false
		
		String str3 = "abc";
		String str4 = "abc";
		
		System.out.println(str3 == str4); // true

	}

}

```

- **한번 생성된 String은 불변(immutable)**

- String을 연결하면 기존의 String에 연결되는 것이 아닌 새로운 문자열이 생성됨 ( 메모리 낭비가 발생할 수도 )

- concat() : 초기값이 null이면 에러 발생
  -  더하려는 값을 new String()으로 새로 만든다.
  -  따라서 문자열을 계속해서 붙인다고 가정하면, 붙일 때마다 주소값을 할당받게 되는 것이다.

```java
public class StringTest2 {

	public static void main(String[] args) {
		String java = new String("java");
		String android = new String("android");
		System.out.println(System.identityHashCode(java));
		
		java = java.concat(android);
		
		System.out.println(java);
		System.out.println(System.identityHashCode(java));
		
	}
}
```

## StringBuilder, StringBuffer 활용하기

- 내부적으로 가변적인 char[]를 멤버 변수로 가짐 

- 문자열을 여러번 연결하거나 변경할 때 사용하면 유용함

- 새로운 인스턴스를 생성하지 않고 char[] 를 변경함

- StringBuffer는 멀티 쓰레드 프로그래밍에서 동기화(synchronization)을 보장

- 단일 쓰레드 프로그램에서는 StringBuilder 사용을 권장

- **toString()** 메서드로 String반환

- 주소값이 변하지 않음

- null을 StringBuilder에 넣고 더하면 null이라는 문자열이 들어감

```java
public AbstractStringBuilder append(String str) {
    if (str == null)
        return appendNull();
    ...
}

private AbstractStringBuilder appendNull() {
    int c = count;
    ensureCapacityInternal(c + 4);
    final char[] value = this.value;
    value[c++] = 'n';
    value[c++] = 'u';
    value[c++] = 'l';
    value[c++] = 'l';
    count = c;
    return this;
}
```

```java
public class StringBuilderTest {

	public static void main(String[] args) {
		String java = new String("java");
		String android = new String("android");
		
		StringBuilder buffer = new StringBuilder(java);
		System.out.println(System.identityHashCode(buffer));
		buffer.append("android");
		System.out.println(System.identityHashCode(buffer));
		
		java = buffer.toString();
	}
}
```

## text block 사용하기 (java 13)

- 문자열을 """ """ 사이에 이어서 만들 수 있음

- html, json 문자열을 만드는데 유용하게 사용할 수 있음

```java
public class StringTextBlock {

	public static void main(String[] args) {
		
		String strBlock = """
				This 
				is 
				text
				block
				test.""";
		System.out.println(strBlock);
		
		System.out.println(getBlockOfHtml());
		
	}
	
	public static String getBlockOfHtml() {
		    return """
		            <html>

		                <body>
		                    <span>example text</span>
		                </body>
		            </html>""";
		
	}

}

//This
//is
//text
//block
//test.
//<html>
//
//    <body>
//        <span>example text</span>
//    </body>
//</html>

```

# 04. Class 클래스 사용하기

## Class 클래스

- 자바의 모든 클래스와 인터페이스는 컴파일 후 class 파일이 생성됨

- Class 클래스는 컴파일 된 class 파일을 로드하여 객체를 동적 로드하고, 정보를 가져오는 메서드가 제공됨

- Class.forName("클래스 이름") 메서드로 클래스를 동적으로 로드 함

```java
Class c = Class.forName("java.lang.String");
```

- 클래스 이름으로 직접 Class 클래스 가져오기
```java
Class c = String.class;
```

- 생성된 인스턴스에서 Class 클래스 가져오기
```java
String s = new String();
Class c = s.getClass();  //Object 메서드
```

## 동적 로딩

- 컴파일 시에 데이터 타입이 binding 되는 것이 아닌, 실행(runtime) 중에 데이터 타입을 binding 하는 방법

- 프로그래밍 시에는 문자열 변수로 처리했다가 런타임시에 원하는 클래스를 로딩하여 binding 할 수 있다는 장점

- 컴파일 시에 타입이 정해지지 않으므로 동적 로딩시 오류가 발생하면 프로그램의 심각한 장애가 발생가능


## Class의 newInstance()메서드로 인스턴스 생성

- new 키워드를 사용하지 않고 클래스 정보를 활용하여 인스턴스를 생성할 수 있음

## 클래스 정보 알아보기

- **reflection 프로그래밍** : Class 클래스를 사용하여 클래스의 정보(생성자, 변수, 메서드)등을 알 수 있고 인스턴스를 생성하고, 
메서드를 호출하는 방식의 프로그래밍

- 로컬 메모리에 객체 없는 경우, 원격 프로그래밍, 객체의 타입을 알 수 없는 경우에 사용

- java.lang.reflect 패키지에 있는 클래스를 활용하여 프로그래밍

- 일반적으로 자료형을 알고 있는 경우엔 사용하지 않음

StringTest.java
```java
public class StringTest {

	public static void main(String[] args) throws ClassNotFoundException {
		Class c3 =  Class.forName("java.lang.String");
		
		Constructor<String>[] cons =  c3.getConstructors();
		for(Constructor con: cons) {
			System.out.println(con);
		}
		
		System.out.println();
		
		Method[] methods = c3.getMethods();
		for(Method  method : methods) {
			System.out.println(method);
		}
	}

}
```

Person.java
```java
public class Person {
	private String name;
	private int age;
	
	public Person() {};
	
	public Person(String name) {
		this.name = name;
	}
	
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}
	
	public String toString() {
		return name;
	}
}
```

ClassTest.java

```java
public class ClassTest {

	public static void main(String[] args) throws InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException,
						ClassNotFoundException, NoSuchMethodException, SecurityException {
		Person person = new Person("James");
		System.out.println(person);
		
		Class c1 = Class.forName("ch04.Person");
		Person person1 = (Person)c1.newInstance();
		System.out.println(person1);
		
		Class[] parameterTypes = {String.class};
		Constructor cons = c1.getConstructor(parameterTypes);
		
		Object[] initargs = {"김유신"};
		Person personLee = (Person)cons.newInstance(initargs);
		System.out.println(personLee);
	}
}
```
