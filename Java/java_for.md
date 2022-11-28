# 19. 반복문 - for 문

## for문의 수행 순서

![for](./img/for.png)


## for문 예제 (while과 비교)

- 1부터 10까지 더한 결과를 출력하세요
```java
package ch19;

public class ForTest {

	public static void main(String[] args) {
		
		int count =0;
		int sum = 0;
		
		for( int i = 0 ; i<10; i++, ++count) {  //10번
			sum += count;
			//count++;
			System.out.println(i); // 0 ~ 9
			System.out.println(count); // 0 ~ 9
		}
		System.out.println(sum); // 45

	}

}


```

## 각 반복문별 적용 예시

![loop](./img/loop.png)


## for문의 문장 생략

- 초기화식 생략 : 이미 이전에 값이 초기화 되어 for 내부에서 값을 지정할 필요가 없는 경우

   ![for1](./img/for1.PNG)

- 조건식 생략 : 반복 수행에 대한 조건이 수행문 내부에 있는 경우
   
   ![for2](./img/for2.PNG)

- 증감식 생략 : 증감식에 대한 연산이 복잡하거나 다른 변수의 연산 결과값에 결정되는 경우
   
   ![for3](./img/for3.PNG)

- 무한 반복

   ![for4](./img/for4.PNG)


## 참고 하세요

    i+1 과 i++은 다릅니다.
    i+1 자체는 i 값이 증가되지 않습니다. 증가하기 위해서는 대입연산자를 써야합니다.
    하지만 i++은 i = i+1, i+=1 과 동일한 의미입니다.
    따라서 값을 1씩 증가하려고 한다면 i++을 사용하세요

# 20. 반복문이 여러 번 포개진 중첩 반복문

## 중첩 반복문이란?

- 반복문 내부에 또 다른 반복문이 있음

- 여러 겹으로 반복문을 겹쳐서 구현 가능 (단 수행시간에 문제가 발생할 수 있음)

- 외부 반복문과 내부 반복문 간의 변수 값 변화에 유의 하며 구현하여야 함


## 구구단을 for와 while로 구현해 보자

```java
package ch20;

public class NestedLoopTest {

	public static void main(String[] args) {
		int dan = 2;
		int count = 1;
		
		for( dan = 2; dan <= 9; dan++) {
			
			for(count = 1; count <=9; count++) {
				
				System.out.println( dan + "X" + count + "=" + dan * count);
			}
			System.out.println();
		}
		
		dan = 2;
		while( dan <= 9 ) {
			count = 1;
			while (count <= 9) {
				
				System.out.println( dan + "X" + count + "=" + dan * count);
				count++;
				
			}
			dan++;
			System.out.println();
		}
	}
}

```

