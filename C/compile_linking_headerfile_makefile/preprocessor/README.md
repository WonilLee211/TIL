# 전처리기

- `#include, #define, #infdef, #endif, #else` 전처리기 구문에 대한 이해
- 헤더파일에 대한 설명
- 라이브러리 (string.h) 사용

## 헤더 파일

구성 

- 함수의 원형
- 전역 변수
- 구조체, 공용체, 열거형
- 함수의 원형
- 일부 특정한 함수(인라인 함수 등)
- 매크로


헤더파일에 C코드를 넣을 수 있지만 권장하지 않음

<br>

### `human.h`

```c
enum {MALE, FEMALE};

struct Human {
    char name[20];
    int age;
    int gender;
};

struct Human create_human(char *name, int age, int gender);
int print_human(struct Human *human);
```

### `human.c`

```c
#include <stdio.h>
#include "human.h"
#include "str.h"

struct Human create_human(char *name, int age, int gender){
    struct Human human;
    human.age = age;
    human.gender = gender;
    copy_str(human.name, name);

    return human;
}
int print_human(struct Human *human){
    printf("Name : %s \n", human->name);
    printf("Age : %d \n",human->age);
    if (human->gender == MALE) {
        printf("Gender : Male \n");
    } else if (human->gender == FEMALE) {
        printf("Gender : Female \n");
    }
    return 0;
}
```


### `str.h`

```c
char copy_str(char *dest, char *src);
```

### `str.c`

```c
#include "str.h"

char copy_str(char *dest, char *src) {
  while (*src) {
    *dest = *src;
    src++;
    dest++;
  }

  *dest = '\0';

  return 1;
}
```

### `main.c`

```c
#include <stdio.h>
#include "human.h"
int main(){
    struct Human Lee = create_human("Lee", 30, MALE);

    print_human(&Lee);
    
    return 0;
}
// Name : Lee
// Age : 40
// Gender : Male
```

- 좋은 프로그램일수록 main 함수에서 하는 일이 적어진다.

## 전처리기

### `#define`

- `#define 매크로이름 값`

- 컴파일 전에 소스코드에서 매크로이름에 해당하는 부분을 값으로 대체

```c
#include <stdio.h>
#define VAR 10
int main(){
    char arr[VAR] = {"hi"};
    printf("%s", arr[VAR]);
    return 0;
}
// hi
```

<br>

### `#ifdef, endif`

- 조건에 따라 컴파일되는 코드가 달라야 할 때 사용

```c
#ifdef 매크로이름
/* 매크로이름이 정의되어 있다면 이 부분이 코드에 포함되고, 그렇지 않다면 코드에 포함되지 않음 */
#endif
```

```c
#include <stdio.h>
#define A
int main(){
#ifdef A
printf("AAAAA \n");
#endif
#ifdef B
printf("BBBBB \n");
#endif
    return 0;
}
```
<br>

### 실사용 예시

```c
/* 계산기 모델 별 시스템 리소스 차이로 이난 변수 타입이 다른 경우 */
#define CACULATOR_MODEL_1

#ifdef CALCULATOR_MODEL_1
float var1, var2;
#endif
#ifdef CALCULATOR_MODEL_2
double var1, var2;
#else
ufloat var1,var2;
#endif
```

### `#ifndef`

- 매크로가 정의되어 있지 않을 때 참이 되는 전처리기


