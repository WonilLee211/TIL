# 06. 생성자에 대해 알아봅시다 (constructor)

## 생성자

- 생성자 기본 문법
<modifier><class_name>([<argument_list])
{
	[<statements]
}

- 객체를 생성할 때 new 키워드와 함께 사용   - new Student();

- 생성자는 일반 함수처럼 기능을 호출하는 것이 아니고 객체를 생성하기 위해 new 와 함께 호출 됨

- 객체가 생성될 때 변수나 상수를 초기화 하거나 다른 초기화 기능을 수행하는 메서드를 호출 함

- 생성자는 반환 값이 없고, 클래스의 이름과 동일

- 대부분의 생성자는 외부에서 접근 가능하지만, 필요에 의해 private 으로 선언되는 경우도 있음


## 기본 생성자 (default constructor)

- 클래스에는 반드시 적어도 하나 이상의 생성자가 존재

- 클래스에 생성자를 구현하지 않아도 new 키워드와 함께 생성자를 호출할 수 있음

- 클래스에 생성자가 하나도 없는 경우 컴파일러가 생성자 코드를 넣어 줌 

    public Student(){}  

-  매개 변수가 없음, 구현부가 없음

## 생성자 만들기

- 컴파일러가 제공해 주는 기본 생성자외에 필요에 의해 생성자를 직접 구현 할 수 있음

Student.java
```java
public class Student {

	public int studentNumber;
	public String studentName;
	public int grade;
	
	public Student(int studentNumber, String studentName, int grade) {
		this.studentNumber = studentNumber;
		this.studentName = studentName;
		this.grade = grade;
	}
	
	public String showStudentInfo() {
		return studentName + "학생의 학번은 " + studentNumber + "이고, " + grade + "학년 입니다.";
	}
}
```

StudentTest.java
```java
public class StudentTest {

	public static void main(String[] args) {

		//Student studentLee = new Student();
		
		Student studentLee = new Student(12345, "Lee", 3);
		
		String data = studentLee.showStudentInfo();
		System.out.println(data);
	}

}
```

# 07. 여러가지 생성자를 정의하는 생성자 오버로딩 (overloading)

## 생성자 정의 하기

- 생성자를 구현해서 사용할 수 있음

- 클래스에 생성자를 따로 구현하면 기본 생성자 (default constructor)는 제공되지 않음

- 생성자를 호출하는 코드(client 코드)에서 여러 생성자 중 필요에 따라 호출해서 사용할 수 있음

UserInfo.java
```java
public class UserInfo {

	public String userId;
	public String userPassWord;
	public String userName;
	public String userAddress;
	public String phoneNumber;
	
    // 기본생성자 형태로 호출해서 입력할 수 있음
	public UserInfo(){}
	
	public UserInfo(String userId, String userPassWord, String userName) {
		this.userId = userId;
		this.userPassWord = userPassWord;
		this.userName = userName;
	}
	
	public String showUserInfo() {
		return "고객님의 아이디는 " + userId + "이고, 등록된 이름은 " + userName + "입니다."; 
	}
}
```

UserInfoTest.java
```java
public class UserInfoTest {

	public static void main(String[] args) {

		UserInfo userLee = new UserInfo();
		userLee.userId = "a12345";
		userLee.userPassWord = "zxcvbn12345";
		userLee.userName = "Lee";
		userLee.phoneNumber = "01034556699";
		userLee.userAddress = "Seoul, Korea";
		
		System.out.println(userLee.showUserInfo());
		
		UserInfo userKim = new UserInfo("b12345", "09876mnbvc", "Kim");
		System.out.println(userKim.showUserInfo());
	}
}
```


# 08. 복습해봅시다 (객체 구현하기)

## 다음 설명에 해당되는 객체를 구현하고 해당 정보를 출력해 보세요

1. 키가 180 이고 몸무게가 78 킬로인 남성이 있습니다. 이름은 Tomas 이고 나이는 37세입니다.

2. 음식점에 배달 주문이 들어왔습니다.
       
       주문 접수 번호 : 202011020003
       주문 핸드폰 번호 : 01023450001
       주문 집 주소 : 서울시 강남구 역삼동 111-333
       주문 날짜 : 20201102
       주문 시간 : 130258
       주문 가격 : 35000
       메뉴 번호 : 0003


```java
package ch08_constructor_practice;

public class UserInfo {
	public String userName;
	public int age;
	public int height;
	public int weight;
	public boolean isMale;
	
	public int showUserInfo() {
		return this.age;
	}
}

package ch08_constructor_practice;

public class OrderInfo {
	
	public long orderNumber;
	public int phoneNumber;
	public String address;
	public int date;
	public int time;
	public int price;
	public int menuNumber;
	
	public OrderInfo(long orderNumber, int phoneNumber, String address, int date, int time, int price, int menuNumber) {
		this.orderNumber = orderNumber;
		this.phoneNumber = phoneNumber;
		this.address = address;
		this.date = date;
		this.time = time;
		this.price = price;
		this.menuNumber = menuNumber;	
	}

}

package ch08_constructor_practice;

public class UserOrderTest {

	public static void main(String[] args) {
		UserInfo user = new UserInfo();
		user.userName = "Tomas";
		user.age = 37;
		user.weight = 78;
		user.height = 180;
		user.isMale = true;
		
		System.out.println(user.showUserInfo());
		
		OrderInfo order = new OrderInfo(202011020003L, 01023450001, "서울시 강남구 역삼동 111-333", 20201102, 130258, 35000, 0003);
		
		System.out.println(order.orderNumber);
	}

}

```

