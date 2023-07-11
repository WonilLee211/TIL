# 입출력함수 포맷

## 문자열 형식 (String Format):

- `%s` : 문자열을 입력 또는 출력하는 데 사용됩니다.

## 정수 형식 (Integer Format):

- `%hd`: 부호있는 짧은 정수를 입력 또는 출력하는 데 사용됩니다.
- `%d` : 부호 있는 10진수 정수를 입력 또는 출력하는 데 사용됩니다.
- `%ld` : 부호 있는 긴 10진수 정수를 입력 또는 출력하는 데 사용합니다.
- `%u` : 부호 없는 10진수 정수를 입력 또는 출력하는 데 사용됩니다.
- `%x` 또는 `%X` : 부호 없는 16진수 정수를 입력 또는 출력하는 데 사용됩니다.

## 실수 형식 (Floating-point Format):

- `%f` : float 부동 소수점 수를 입력 또는 출력하는 데 사용됩니다.
- `%lf` : double 부동 소수점 수를 입력 또는 출력하는 데 사용됩니다.
- `%e` 또는 `%E` : 지수 형식의 부동 소수점 수를 입력 또는 출력하는 데 사용됩니다.

## 문자 형식 (Character Format):

- `%c` : 단일 문자를 입력 또는 출력하는 데 사용됩니다.

## 아스키코드

![asciicode](https://github.com/WonilLee211/TIL/assets/109330610/b93e31fd-73b9-40f7-8da0-5974f2ac6c0f)


## 입출력함수 예시

- scanf

```c
#include <stdio.h>

int main() {
    char ch; // 문자

    short sh; // 정수
    int i;
    long lo;

    float fl; // 실수
    double du;

    printf("char 형 변수 입력 : ");
    scanf("%c", &ch);

    printf("short 형 변수 입력 : ");
    scanf("%hd", &sh);
    printf("int 형 변수 입력 : ");
    scanf("%d", &i);
    printf("long 형 변수 입력 : ");
    scanf("%ld", &lo);
    
    printf("float 형 변수 입력 : ");
    scanf("%f", &fl);
    printf("double 형 변수 입력 : ");
    scanf("%lf", &du);

    printf("char : %c, short : %d, int : %d ", ch, sh, i);
    printf("long : %ld, float : %f, double : %f \n", lo, fl, du);

    return 0;
}

```

