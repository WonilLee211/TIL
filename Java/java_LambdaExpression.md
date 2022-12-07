# 02. 람다식(Lambda expression)

## 함수형 프로그래밍과 람다식

- 자바는 객체 지향 프로그래밍 : 기능을 수행하긴 위해서는 객체를 만들고 그 객체 내부에 멤버 변수를 선언하고 기능을 수행하는 메서드를 구현

- 자바 8부터 함수형 프로그래밍 방식을 지원하고 이를 람다식이라 함

- 함수의 구현과 호출만으로 프로그래밍이 수행되는 방식

- 함수형 프로그래밍(Functional Programming: FP) 
    
    함수형 프로그래밍은 순수함수(pure function)를 구현하고 호출함으로써 외부 자료에 부수적인 영향(side effect)를 주지 않도록 구현하는 방식입니다. 순수 함수란 매개변수만을 사용하여 만드는 함수 입니다. 즉, 함수 내부에서 함수 외부에 있는 변수를 사용하지 않아 함수가 수행되더라도 외부에는 영향을 주지 않습니다. 

    함수를 기반으로 하는 프로그래밍이고 입력받는 자료 이외에 외부 자료를 사용하지 않아 여려 자료가 동시에 수행되는 병렬처리가 가능합니다. 
    함수형 프로그래밍은 함수의 기능이 자료에 독립적임을 보장합니다. 이는 동일한 자료에 대해 동일한 결과를 보장하고, 다양한 자료에 대해 같은 기능을 수행할 수 있습니다. 

## 람다식 문법

- 익명 함수 만들기

- 매개 변수와 매개변수를 이용한 실행문 (매개변수) -> {실행문;}

- 두 수를 입력 받아 더하는 add() 함수 예

```java
int add(int x, int y){

    return x+y;
}
```

- 람다식으로 표현

``` java
(int x, int y) -> {return x+y;}

```
- 매개 변수가 하나인 경우 자료형과 괄호 생략가능

```java
str->{System.out.println(str);}
```

- 매개변수가 두 개이상인 경우 괄호를 생략할 수 없음

```java
x, y -> {System.out.println(x+y);}  //오류
```

- 실행문이 한 문장인 경우 중괄호 생략 가능

```java
str-> System.out.println(str);
```

- 실행문이 한 문장이라도 return문(반환문)은 중괄호를 생략할 수 없음

```java
str-> return str.length();  //오류
```

- 실행문이 한 문장의 반환문인 경우엔 return과 중괄호를 모두 생략

```java
(x, y) -> x+y;
str -> str.length;
```


# 03. 함수형 인터페이스와 람다식 구현하여 사용하기

## 함수형 인터페이스 선언하기

- 람다식을 선언하기 위한 인터페이스

- 익명 함수와 매개 변수만으로 구현되므로 **인터페이스는 단 하나의 메서드만을 선언해야함**

- @FunctionalInterface 애노테이션(annotation)

    **함수형 인터페이스라는 의미**, 내부에 여러 개의 메서드를 선언하면 에러남 

    ![error](./img/error.png)

- 람다식 구현과 호출

```java
package ch03_FunctionalInterface;

@FunctionalInterface
public interface MyNumber{
	public abstract int getMax(int x, int y);
}

```

```java
package ch03_FunctionalInterface;

public class TestMyNumber {

	public static void main(String[] args) {
		
		MyNumber max = (x, y) ->(x >= y)? x: y;
		System.out.println(max.getMax(10, 20));
		
//		20
	}

}

```


# 04. 객체지향 프로그래밍 vs. 람다식 구현

## 객체 지향 프로그래밍과 람다식 비교

- 문자열 두 개를 연결하여 출력하는 예제를 두 가지 방식으로 구현해 보자

- 인터페이스 선언

```java
public interface StringConcat {
	
	public void makeString(String s1, String s2);

}
```

- 객체 지향 프로그래밍으로 구현하기

 인터페이스를 구현한 클래스 만들기

```java
public class StringConCatImpl implements StringConcat{

	@Override
	public void makeString(String s1, String s2) {
		System.out.println( s1 + "," + s2 );
	}
}
```
 클래스를 생성하고 메서드 호출하기

```java
public class TestStringConcat {

	public static void main(String[] args) {

		String s1 = "Hello";
		String s2 = "World";
		StringConCatImpl concat1 = new StringConCatImpl();
		concat1.makeString(s1, s2);
    }
}
```

- 람다식으로 구현하기

```java
StringConcat concat2 = (s, v)->System.out.println(s + "," + v ); //System.out.println(i);
concat2.makeString(s1, s2);
```

## 익명 객체를 생성하는 람다식

- 자바에서는 객체 없이 메서드가 호출 될 수 없음

- 람다식을 구현하면 익명 내부 클래스가 만들어지고, 이를 통해 익명 객체가 생성됨

```java
StringConcat concat3 = new StringConcat() {
			
	@Override
	public void makeString(String s1, String s2) {
			
		System.out.println( s1 + "," + s2 );
	}
};
		
concat3.makeString(s1, s2);
```

- 익명 내부 클래스에서와 마찬가지로 람다식 내부에서도 외부에 있는 지역 변수의 값을 변경하면 오류가 발생함

## 함수를 변수처럼 사용하는 람다식

변수는...
	
	특정 자료형으로 변수를 선언 한 후 값을 대입함   int a = 10;

	매개 변수로 전달하여 사용함 		int add(int x, int y)

	메서드의 반환 값으로 반환 하기		return num;


- 인터페이스형 변수에 람다식 대입하기

  함수형 인터페이스
```java
interface PrintString{
	
	void showString(String str);
}
```

```java
PrintString lambdaStr = s->System.out.println(s);  //람다식을 변수에 대입
lambdaStr.showString("hello lambda_1");
```

- 매개변수로 전달하는 람다식
```java
showMyString(lambdaStr); 

public static void showMyString(PrintString p) {
	p.showString("hello lambda_2");
}
```

- 반환 값으로 쓰이는 람다식

```java
public static PrintString returnString() {         //반환 값으로 사용
		return s->System.out.println(s + "world");
}


PrintString reStr = returnString();  
reStr.showString("hello ");
```


# 06. 연산 수행에 대한 구현을 할 수 있는 reduce()연산

## reduce() 연산

- 정의된 연산이 아닌 프로그래머가 직접 구현한 연산을 적용
```java
T reduce(T identify, BinaryOperator<T> accumulator)
```

- 최종 연산으로 스트림의 요소를 소모하며 연산을 수행

- 배열의 모든 요소의 합을 구하는 reduce() 연산 구현 예

```
Arrays.stream(arr).reduce(0, (a,b)->a+b));
```
- reduce() 메서드의 두 번째 요소로 전달되는 람다식에 따라 다양한 기능을 수행 할 수 있음

- 람다식을 직접 구현하거나 람다식이 긴 경우 BinaryOperator를 구현한 클래스를 사용 함

## BinaryOperator를 구현하여 배열에 여러 문자열이 있을 때 길이가 가장 긴 문자열 찾기 예

- 에러 발생

```java
package ch06_reduce;

//import java.util.Arrays;
import java.util.function.BinaryOperator;

class CompareString implements BinaryOperator<String>{

	@Override
	public String apply(String s1, String s2) {
		
		if(s1.getBytes().length >= s2.getBytes().length) return s1;
		else return s2;
		
	}
}

public class ReduceTest {

	public static void main(String[] args) {
		
		String[] greetings = {"안녕하세요~~~", "hello", "Good morning", "반갑습니다^^"};
//		System.out.println(Arrays.stream(greetings).reduce("", (s1, s2)-> 
//	        {
//	        	if (s1.getBytes().length >= s2.getBytes().length) 
//	                        return s1;
//	        	else return s2;
//	        })
//		); 

		
//		String str = Arrays.stream(greetings).reduce(new CompareString()).get();
		//BinaryOperator를 구현한 클래스 이용
//		System.out.println(str);
		
	}
}

```




