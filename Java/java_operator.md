# 11. 자바의 연산자들 -1 (대입, 부호, 산술, 복합대입, 증감연산자)

## 항과 연산자

- 항(operand) : 연산에 사용되는 값

- 연산자 (operator) : 항을 이용하여 연산하는 기호

## 대입 연산자 (assignment operator)

- 변수에 다른 변수나 값을 대입하는 연산자

- 이항 연산자 중 우선 순위가 가장 낮은 연산자들

- 왼쪽 변수 = 오른쪽 변수(또는 식, 값)

## 부호 연산자

- 단항 연산자 

- 변수의 부호를 유지 하거나(+) 바꿈(-)

- 실제 변수의 부호가 변하려면 대입 연산자를 사용해야 함

## 산술 연산자

- 사칙 연산자 <br>
![add](./img/add.png)

- % 나머지 구하는 연산자, 숫자 n 의 나머지 범위는 0 ~ n-1

## 복합 대입 연산자

- 대입 연산자와 다른 연산자가 함께 쓰임<br>
![multi](./img/multi.png) <br>

## 증가, 감소 연산자

- 단항 연산자

- 변수의 값을 1 더하거나 1 뺄때 사용

- 연산자가 항의 앞에 있는가 뒤에 있는가에 따라 연산 시점과 결과가 달라짐

- 문장(statement)의 끝(;)을 기준으로 연산 시점을 생각해야 함

![add2](./img/add2.png)

# 12. 자바의 연산자들 -2 (관계, 논리 연산자)

## 관계 연산자

- 이항 연산자

- 연산의 결과가 true(참), false(거짓)으로 반환 됨, 비교연산자 라고도 함

- 조건문, 반복문의 조건식으로 많이 사용 됨

![relation](./img/relation.png)

```
package ch12;

public class RealtionalTest {

	public static void main(String[] args) {

		int num1 = 5;
		int num2 = 3;
		
		boolean value = (num1 > num2);
		System.out.println(value);
		
		System.out.println(num1 < num2);
		System.out.println(num1 >= num2);
		System.out.println(num1 <= num2);
		System.out.println(num1 == num2);
		System.out.println(num1 != num2);
	}
}
```
![relationa](./img/relationa.PNG)

## 논리 연산자

- 관계 연산자와 혼합하여 많이 사용 됨

- 연산의 결과가 true(참), false(거짓)으로 반환 됨

![logical](./img/logical.png)

```
package ch12;

public class LogicalTest {

	public static void main(String[] args) {
		
		int num1 = 10;
		int num2 = 20;
		
		boolean flag = (num1 > 0) && (num2 > 0);
		System.out.println(flag);
		
		flag = (num1 < 0) && (num2 > 0);
		System.out.println(flag);
		
		flag = (num1 > 0) || (num2 > 0);
		System.out.println(flag);
		
		flag = (num1 < 0) || (num2 > 0);
		System.out.println(flag);
		
		flag = !(num1 > 0);
		System.out.println(flag);
	}
}
```
![logicala](./img/logicala.PNG)

## 논리 연산에서 모든 항이 실행되지 않는 경우 - 단락 회로 평가 (short circuit evaluation)

- 논리 곱(&&)은 두 항의 결과가 모두 true일 때만 결과가 true

  -- 앞의 항의 결과가 false이면 뒤 항의 결과를 평가하지 않음

- 논리 합(||)은 두 항의 결과가 모두 false일 때만 결과가 false
   
  -- 앞의 항의 결과가 true이면 뒤 항의 결과를 평가하지 않음 

```
package ch12;

public class ShortCircuit {

	public static void main(String[] args) {
		
		int num1 = 10;
		int i = 2;
		
		boolean value = ((num1 = num1 + 10 ) < 10) && ( ( i = i + 2 ) < 10);
		System.out.println(value);
		System.out.println(num1);
		System.out.println(i);
		
		value = ((num1 = num1 + 10 ) < 10) || ( ( i = i + 2 ) < 10);
		System.out.println(value);
		System.out.println(num1);
		System.out.println(i);
		
	}
}
```
![shorta](./img/shorta.PNG)


# 13. 자바의 연산자들 -3 (조건 연산자, 비트 연산자)

## 조건 연산자

- 삼항 연산자

- 조건식의 결과가 true(참)인 경우와 false(거짓)인 경우에 따라 다른 결과가 수행됨 

- if (조건문)을 간단히 표현할 때 사용 할 수 있음


![conditionop](./img/conditionop.png)

```
package ch13;

import java.util.Scanner;

public class ConditionTest {

	public static void main(String[] args) {

		int max;
		System.out.println("입력 받은 두 수중 큰 수를 출력하세요\n ");
		
		Scanner scanner = new Scanner(System.in);
		System.out.println("입력1:");
		int x = scanner.nextInt();
		System.out.println("입력2:");
		int y = scanner.nextInt();
		
		max = (x > y)? x : y;
		System.out.println(max);
	}
}
```

## 비트 연산자

- 대입연산자와 다른 연산자가 함께 쓰임

- 마스크 : 특정 비트를 가리고 몇 개의 비트 값만 사용할 때

- 비트켜기 : 특정 비트들만을 1로 설정해서 사용하고 싶을 때<br>
        예)  & 00001111 ( 하위 4비트 중 1인 비트만 꺼내기)

- 비트끄기 : 특정 비트들만을 0으로 설정해서 사용하고 싶을 때<br>
      예)  | 11110000 ( 하위 4비트 중 0 인 비트만 0으로 만들기)

- 비트 토글 :  모든 비트들을 0은 1로, 1은 0으로 바꾸고 싶을 때

![bit](./img/bit.PNG)

```
package ch13;

public class BitTest {

	public static void main(String[] args) {

		int num1 = 5;  	// 00000101
		int num2 = 10; 	// 00001010
				
		System.out.println(num1 | num2);
		System.out.println(num1 & num2);
		System.out.println(num1 ^ num2);
		System.out.println(~num1);
		
		System.out.println(num1 << 2);
		System.out.println(num1);
		System.out.println(num1 <<= 2);
		System.out.println(num1);
		
	}
}
```

![bita](./img/bita.PNG)

## 연산자 우선순위

![priority](./img/priority.png)

