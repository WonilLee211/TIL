# 04. 메서드 재정의하기(overring)

## 하위 클래스에서 메서드 재정의 하기

- 오버라이딩(overriding) : 상위 클래스에 정의된 메서드의 구현 내용이 하위 클래스에서 구현할 내용과 맞지 않는 경우 
하위 클래스에서 동일한 이름의 메서드를 재정의 할 수 있음 

- VIPCustomer 클래스의 calcPrice()는 할인율이 적용되지 않음

- 재정의 하여 구현해야 함

VIPCustomer.java
```java
@Override
public int calcPrice(int price) {
	bonusPoint += price * bonusRatio;
	return price - (int)(price * salesRatio);
}
```

## @overriding 애노테이션 (annotation)

- 애노테이션은 원래 주석이라는 의미

- 컴파일러에게 특별한 정보를 제공해주는 역할 

![annotation](./img/annotation.png)

- @overriding 애노테이션은 재정의 된 메서드라는 의미로 **선언부가 기존의 메서드와 다른 경우 에러가 남**

- 생략해도 정상 동작함
  
  - 상위 클래스의 메서드의 시그니처가 변경되었을 때 컴파일 에러를 발생시키기 위해 작성
  - 가독성을 위해 작성

## 형 변환과 오버라이딩 메서드 호출

   Customer vc = new VIPCustomer();

   vc 변수의 타입은 Customer지만 인스턴스의 타입은 VIPCustomer 임
   
   **자바에서는 항상 인스턴스의 메서드가 호출 됨 (가상메서드의 원리)**

   **자바의 모든 메서드는 가상 메서드(virtual method) 임**

   **상위 클래스로 형변환된 인스턴스의 메서드 호출은 하위 클래스의 메서드가 호출됨**

CustomerTest.java
```java
public class CustomerTest {

	public static void main(String[] args) {
		
		Customer customerLee = new Customer(10010, "이순신");
		customerLee.bonusPoint = 1000;
		System.out.println(customerLee.showCustomerInfo());
		
		VIPCustomer customerKim = new VIPCustomer(10020, "김유신");
		customerKim.bonusPoint = 10000;
		System.out.println(customerKim.showCustomerInfo());
		
		int priceLee = customerLee.calcPrice(10000);
		int priceKim = customerKim.calcPrice(10000);
		
		System.out.println(customerLee.showCustomerInfo() + " 지불금액은 " + priceLee + "원 입니다.");
		System.out.println(customerKim.showCustomerInfo() + " 지불금액은 " + priceKim + "원 입니다.");
		
		Customer customerNo = new VIPCustomer(10030, "나몰라");
		customerNo.bonusPoint = 10000;
		int priceNo = customerNo.calcPrice(10000);
		System.out.println(customerNo.showCustomerInfo() + " 지불금액은 " + priceNo  + "원 입니다.");

	}
}

//	Customer(int, String) 생성자 호출
//	이순신님의 등급은 SILVER이며, 보너스 포인트는1000입니다
//	Customer(int, String) 생성자 호출
//	VIPCustomer(int, String) 생성자 호출
//	김유신님의 등급은 VIP이며, 보너스 포인트는10000입니다
//	이순신님의 등급은 SILVER이며, 보너스 포인트는1100입니다 지불금액은 10000원 입니다.
//	김유신님의 등급은 VIP이며, 보너스 포인트는10500입니다 지불금액은 9000원 입니다.
//	Customer(int, String) 생성자 호출
//	VIPCustomer(int, String) 생성자 호출
//	나몰라님의 등급은 VIP이며, 보너스 포인트는10500입니다 지불금액은 9000원 입니다. // 하위 클래스 메서드가 호출됨
```


# 05. 메서드 재정의와 가상 메서드 원리

## 메서드는 어떻게 호출되고 실행 되는가?

- 메서드(함수)의 이름은 주소값을 나타냄

- 메서드는 명령어의 set 이고 프로그램이 로드되면 메서드 영역(코드 영역)에 명령어 set이 위치

- 해당 메서드가 호출 되면 명령어 set 이 있는 주소를 찾아 명령어가 실행됨

- 이때 메서드에서 사용하는 변수들은 스택 메모리에 위치 하게됨

- 따라서 다른 인스턴스라도 같은 메서드의 코드는 같으므로 같은 메서드가 호출됨

- 인스턴스가 생성되면 변수는 힙 메모리에 따로 생성되지만, 메서드 명령어 set은 처음 한번만 로드 됨

```java
public class TestMethod {

	int num;
	
	void aaa() {
		System.out.println("aaa() 호출");
	}
	
	public static void main(String[] args) {
		
		TestMethod a1 = new TestMethod();
		a1.aaa();
		
		TestMethod a2 = new TestMethod();
		a2.aaa();
	}

}
```
![mem](./img/mem.png)

## 가상 메서드의 원리

- 가상 메서드 테이블(vitual method table)에서 해당 메서드에 대한 address를 가지고 있음

- 재정의된 경우는 재정의 된 메서드의 주소를 가리킴<br>
- 
![virtual](./img/virtual.png)<br>

![calcprice](./img/calcprice.png)<br>
