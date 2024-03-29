# Pointer

- 포인터에 대한 이해
- `*, &` 단항 연산자의 의미
- 상수 포인터(`const int*, int* const`)


## 정의

- 메모리 상에 위치한 특정 데이터가 저장된 주소값을 보관하는 변수
- `(포인터에 주소값이 저장되는 데이터의 형) *(포인터의 이름);`
- `(포인터에 주소값이 저장되는 데이터의 형)* (포인터의 이름);`
- `int* p;` : `int` 형 데이터의 주소값을 저장하는 포인터, `p`
- `ìnt *p;`

## &연산자

- 단항 연산자
- 피연산자의 주소값을 불러옴
    - `&(주소값을 계산할 데이터);`

```c
#include <stdio.h>

int main() {
    int a;
    a = 2;

    printf("%p \n", &a);
    return 0;
}
// 0x7fff80505b64
```

- 위 출력값은 64비트 운영체제에서는 16자리 주소값이 찍혀야 하지만, 짤린 것

```c
#include <stdio.h>

int main() {
    int *p;
    int a;
    p = &a;

    printf("포인터 p에 들어 있는 값 : %p \n", p);
    printf("int 변수 a가 저장된 주소 : %p \n", &a);

    return 0;
}
// 포인터 p 에 들어 있는 값 : 0x7fff894c8b3c 
// int 변수 a 가 저장된 주소 : 0x7fff894c8b3c
```

## *연산자

- 주소값에 대응하는 데이터를 가져오는 단항 연산자
- `*p;` : 포인터 p에 저장된 주소값에 위치한 데이터

```c
#include <stdio.h>

int main() {
    int *p;
    int a;

    p = &a;
    a = 2;
    // *p = 2; // 이 또한, 가능

    printf("a의 값 : %d \n", a);
    printf("*p의 값 : %d \n", *p);

    return 0;
}
// a 의 값 : 2 
// *p 의 값 : 2 
```

## pointer type

- 32비트 운영체제에서 주소값은 4byte, 64비트 운영체제에서 주소값은 8byte가 할당된다.
- 여기서 포인터에 주소값이 할당될 때 모든 주소값이 저장되는 것이 아니라, **시작 주소만 들어가게 됨.**
- type 별로 저장되는 공간크기가 다르기 때문에 pointer에 값을 저장할 때 type을 선언해 주는 것이 중요하다.
    - 예를 들어 4byte인 int 주소값을 pointer에 저장한 경우, 실제 데이터를 불러올 때 4byte크기의 메모리를 읽어서 반환하게 된다.


## 상수 포인터

`const int* pa = &a;`

- 포인터, pa에 int형 변수 a의 주소값을 저장하는데, 그 주소에 해당하는 값을 절대 바꿀 수 없음

```c
#include <stdio.h>

int main(){
    int a;
    int b;
    int* const pa1 = &a;

    *pa1 = 3; // 올바른 문장
    pa1 = &b; // 올바르지 않은 문장, compile 불가


    const int* const pa2 = &b;
    *pa2 = 4; // 올바르지 않은 문장, compile 불가 
    pa2 = &a; // 올바르지 않은 문장, compile 불가

    return 0;
}
```
