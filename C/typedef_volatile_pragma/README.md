# `typedef, volatile, #pragma`

## `typedef`

기존의 데이터 타입에 새로운 이름을 부여하는 데 사용

이를 통해 코드의 가독성을 높이거나 코드를 더 모듈화할 수 있음

`typedef 기존_데이터_타입 새로운_이름;`

```c
#include <stdio.h>
struct HUMAN {
    int age;
    int height;
    int weight;
    int gender;
};
typedef struct HUMAN Human;
int main(){
    Human Adam = {31, 182, 75, 0};
    Human Eve = {27, 166, 48, 1};

    // ...
    
    return 0;
}
```

<br>

### `typedef` 여러가지 활용

```c
#include <stdio.h>
int add(int a, int b) { return a + b; }
typedef int CAL_TYPE;
typedef int (*Padd)(int, int);
typedef int Arrays[10];
int main(){
    CAL_TYPE a = 10;
    Arrays arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    Padd ptr = add;
    printf("a : %d \n", a);
    printf("arr[3] : %d \n", arr[3]);
    printf("add(3, 5) : %d \n", ptr(3, 5));
    return 0;
}
```

### `typedef int (*Padd)(int, int);`

- 함수 포인터 명령을 Padd 이름에 붙임
- `int (*ptr)(int, int) = arr;` = `Padd ptr = add;`

### `typedef int Arrays[10];`

- 원소가 10 개인 `int`형 배열을 선언해라
- `int arr[10];` = `Arrays arr;`




## `volatile` 키워드

외부 하드웨어와 통신할 때 사용

특정한 외부 센서와 소통하는 프로그램을 만들 경우
- 센서의 값이 감지되면 할당된 메모리에 0을, 감지되지 않으면 할당된 메모리에 값을 1로 저장

```c
#include <stdio.h>
typedef struct SENSOR {
    int sensor_flag;
    int data;
} Sensor;
int main(){
    Sensor *sensor;
    while(!sensor->sensor_flag){
    }
    printf("Data : %d \n", sensor->data);
}
```

- 위 코드를 컼파일하게 되면 컴파일러는 과한 최적화를 진행하여 아래와 같이 코드를 변경한다.

```c
#include <stdio.h>
typedef struct SENSOR {
    int sensor_flag;
    int data;
} Sensor;
int main(){
    Sensor *sensor;
    if (!(sensor->sensor_flag)) {
        while (1) {
        }
    }
    printf("Data : %d \n", sensor->data);
}
```

- 컴파일 과정에서 최적화를 생략하는 명령어를 줄 수 있지만, 전체 코드 입장에서 불리하다.
- 이 때 사용하는 키워드가 `volatile`!!!!

```c
#include <stdio.h>
typedef struct SENSOR {
  /* 감지 안되면 0, 감지되면 1 이다.*/
  int sensor_flag;
  int data;
} Sensor;
int main(){
    volatile Sensor *sensor;
    while (!(sensor->sensor_flag)){
    }
    printf("Data : %d \n", sensor->data);
    
    return 0;
}
```

- 위와 같이 구조체 Sensor에 대해 volatile키워드를 붙임
    - `sensor->sensor_flag`키워드가 변덕스럽게 변경될 수 있기 때문에 이에 대한 최적화 작업을 하지말라는 의미
    - **변수의 값을 항상 실제 메모리에서 읽거나 쓰도록 보장**

## `#pragma` 키워드

컴파일러에게 명령하는 전처리 명령

다른 전처리기처럼 컴파일 이전에 실행되지만 명령은 컴파일러에게 전달됨

컴파일러의 종속적인 키워드라고 할 수 있음
- 컴파일러마다 사용 문법이 상이하고 통일된 것이 없음


다양한 키워드들이 있다.

```c
#include <stdio.h>
#pragma pack(1)
// Weird 구조체는 6byte이지만 sizeof 출력 시 8로 출력된다.
typedef struct Weird {
    char arr[2];
    int i;
};
int main(){
    Weird a;
    printf("size of a : %d", sizeof(a));
    return 0;
}
// 6
```
### `#pragma pack(n)`
- *더블 워드 경계에 놓인 문제*를 해결할 때 주로 사용함
    - 컴퓨터는 데이털르 보관할 때 4의 배수로 저장하는 것이 처리에 용이하기 때문에 데이터를 불필요한 공간까지 추가하여 할당하게 된다.
- 마이크로소프트 계열의 컴파일러에게 유요한 명령어
- 구조체를 1바이트 단위로 정렬하라는 뜻
- 즉, 구조체의 크기가 1의 배수가 되게 하라는 뜻
- `n` : 1, 2, 4, 8, 16


<br>

### `#pragma once`

헤더 파일의 중복 선언을 방지하는 전처리 명령

기존 상용코드에서는 `#ifndef` 전처리기를 통해 중복 선언을 방지하고 있음

```c
/* 수정된 weird.h*/
#ifndef WEIRD_H
#define WEIRD_H
struct Weird {
  char arr[2];
  int i;
};
#endif

// ------------
#include <stdio.h>
#include "weird.h"
int main() {
  struct Weird a;
  a.i = 3;
  printf("Weird 구조체의 a.i : %d \n", a.i);
  return 0;
}
// Weird 구조체의 a.i : 3
```

- `#include "weird.h"` 를 만났을 때 WEIRD_H 가 정의되어 있지 않으므로 `#ifndef` 가 참이 되어 아래 `#define WEIRD_H` 가 수행되어 `WEIRD_H`라는 것이 정의됨
- 그 후에 실수로 `weird.h` 를 다시 한 번 include 하였을 때 에는 이미 `WEIRD_H` 가 정의되어 있는 상태이므로 `#ifndef` `WEIRD_H` 가 거짓이 되어 `#endif` 로 넘어가버려 `test.c` 에 그 내용이 복사가 안됨.
- 이는 이미 수많은 헤더파일에서 사용되고 있는 방법

위 방법을 단순화한 `#pragma once`

```c
/* #pragma 의 위엄 – weird.h */
#pragma once
struct Weird {
  char arr[2];
  int i;
};
```

- 컴파일러가 지원하는지 확인 후 사용해야 한다.

<br>

### `stdio.h` 열어보기

```c
#if _MSC_VER > 1000
#pragma once
#endif

#ifndef _INC_STDIO
#define _INC_STDIO

/* 내용 (생략) */

#endif /* _INC_STDIO */

```
- 컴파일러마다 알맞는 중복 에러 예외 구문을 작성했음
- `_MSC_VER` : 마이크로소프트 사의 전처리기에 의해 기본적으로 정의되어 있는 상수로 컴파일러의 버전을 의미함

