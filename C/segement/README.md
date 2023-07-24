# 데이터 세그먼트 구조

- 지역변수
- 전역변수
- 정적변수
- 데이터 세그먼트 구조

## 지역변수

중괄호 `{}`는 하나의 지역으로 취급한다.

해당 지역에서 정의된 변수는 바깥 지역에서 정의된 같은 이름의 변수를 완전히 가리개 된다.

또한, 바깥 지역에서 안쪽 지역에 정의된 변수를 사용할 수 없다.

```c
#include <stdio.h>
int main(){
    {int b = 4;}

    printf("%d \n", b);

    return 0;
}
// 컴파일 에러 : test2.c:8:23: error: ‘a’ undeclared (first use in this function)
```

## 전역변수

어떤 지역에도 속하지 않는 변수를 의미한다.
```c
#include <stdio.h>
int global = 0;
int function(){
    global++;
    return 0;
}
int main(){
    global = 10;
    function();
    printf("%d", global);
    return 0;
}
// 11
```

## 변수의 생존기간

일반적으로 정의된 변수들은 자신이 정의된 지역을 빠져나갈 때 파괴됨

중괄호를 벗어날 때 해당 변수가 사라지게 됨

## 정적변수

지역을 빠져나가도 파괴되지 않는 변수

```c
#include <stdio.h>
int * function(){
    static int a = 2;
    return &a;
}
int main(){
    int* pa = function();
    printf("%d \n", *pa);
    return 0;
}
// 2
```

`function`을 호출하지 않더라도 `a` 정적변수는 이미 선언되어 있는 상태이다.

`function`함수가 여러 번 반복되어 실행하더라도, `a`정적변수는 한번만 초기화된다.

전역변수와 동일하게 정의 시 특별한 값으로 지정하지 않는 한, 0으로 자동 초기화됨

## 데이터 세그먼트 구조

![image](https://github.com/WonilLee211/TIL/assets/109330610/3f552b2d-4cea-41c8-87ee-fbc34df646a1)

C언어 자체적으로는 스택이나 힙 영역을 따로 구분하지 않습니다.

프로그램이 실행될 때 코드와 데이터가 메모리 상에 올라가게 된다.

메모리 상에 적재되는 내용을 크게 두 가지로 분류한다.

1. 코드 세그먼트(code segment)
2. 데이터 세그먼트(data segment)
    1. 데이터 영역
    2. Read-Only 데이터 영역


<br>

### 읽기 전용 데이터(Read-Only) Data

값을 절대 변경할 수 없는 영역

궁극적으로 보호받는 영역


### data

정적 변수 및 전역 변수의 위치

<br>

### stack

지역변수가 위치

지역변수가 늘어나면 크기가 아래로 증가하다가 지역변수가 파괴되면 스택의 크기가 위로 줄어듦

스택이 늘어나는 방향은 메모리 주소가 낮아지는 방향


## 변수 별 메모리 배치

```c
/* 메모리의 배치 모습 */

#include <stdio.h>
int global = 3;
int main() {
  int i;
  char *str = "Hello, Baby";
  char arr[20] = "WHATTHEHECK";

  printf("global : %p \n", &global);
  printf("i : %p \n", &i);
  printf("str : %p \n", str);
  printf("arr : %p \n", arr);
}
// global : 177010
// i : 1af8c8
// str : 1175a28
// arr : 1af8a0
```

![image](https://github.com/WonilLee211/TIL/assets/109330610/6aaefd61-78b1-48c6-99b4-025af16d957f)