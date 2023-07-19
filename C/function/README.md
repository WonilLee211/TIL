# 함수

- 함수의 정의
- `main` 함수
- 포인터로 받는 인자
- 함수의 원형
- 배열을 인자로 받기


## 함수의 정의

```c
int print_hello() {
    // ...
}

```

## 메인(main) 함수

- 프로그램을 실행할 때 컴퓨터가 `main`함수부터 찾아 호출함
- `main`함수의 return 값은 운영체제가 받아들임
- 통상적으로 정상적으로 종료되므로 마지막에 0을 리턴함

## 포인터로 받은 인자

```c
#include <stdio.h>
int change_val(int *pi) {
    printf("---- change_val 함수 안에서 ---- \n");
    printf("pi의 값 : %p \n", pi);
    printf("pi가 가리키는 값 : %d \n", *pi);

    *pi = 3;

    printf("------ change_val 함수 종료 ------\n");
    return 0;
}

int main() {
    int i = 0;

    printf("i 변수의 주소값 : %p \n", &i);
    printf("호출 이전 i의 값 : %d \n", i);
    change_val(&i);
    printf("호출 이후 i의 값 : %d \n", i);

    return 0;
}

// i 변수의 주소값 : 0x7ffd3928afc4 
// 호출 이전 i 의 값 : 0 
// ----- change_val 함수 안에서 -----
// pi 의 값 : 0x7ffd3928afc4 
// pi 가 가리키는 것의 값 : 0 
// ----- change_val 함수 끝~~ -----
// 호출 이후 i 의 값 : 3 
```

- `*pi`를 통해 `i`에 간접적으로 접근 가능
    - `*` : 해당 주소값에 해당하는 변수를 의미하도록 하는 명령어
    - `i`의 주소값이 `pi`에 전달된다. 즉, `pi`는 `i를 가리키게 된다.


## 포인터를 이용한 swap 함수

- 어떠한 함수가 특정한 타입의 변수/배열의 값을 바꾸려면 함수의 인자는 반드시 타입을 가리키는 포인터 형을 이용해야 한다.

```c
#include <stdio.h>

int swap(int *pi, int *pj){
    int temp = *pi;

    *pi = *pj;
    *pj = temp;

    return 0;
}

int main(){
    int i, j;
    i = 3;
    j = 5;

    printf("SWAP 이전 :i = %d, j = %d \n", i, j);
    swap(&i, &j);
    printf("SWAP 이후 : ㅑ = %d, j = %d \n", i, j);

    return 0;    
}
// SWAP 이전 : i : 3, j : 5 
// SWAP 이후 : i : 5, j : 3
```

## 함수의 원형(prototype)

- 함수의 인자 누락, 타입 오류, 선언 위치 등 다양한 문제로 발생 가능한 프로그램 오류에서 디버깅을 방지하기 위한 방법

```c
#include <stdio.h>

int swap(int *a, int *b); // 함수의 원형

int main(){
  int i, j;
  i = 3;
  j = 5;
  printf("SWAP 이전 : i : %d, j : %d \n", i, j);
  swap(&i, &j);
  printf("SWAP 이후 : i : %d, j : %d \n", i, j);

  return 0;
}
int swap(int *a, int *b) {
  int temp = *a;

  *a = *b;
  *b = temp;

  return 0;
}
// SWAP 이전 : i : 3, j : 5 
// SWAP 이후 : i : 5, j : 3 
```

- `main`함수의 위에 함수의 정의를 작성함으로써, 컴파일러에서 함수 사용 과정에서 오류를 잡아낼 수 있도록 함
- 통상적으로 함수의 원형언 `main` 함수 앞에, 구현체는 뒤에 작성한다.

## 배열을 인자로 받기

```c
#include <stdio.h>

int add_number(int *parr);

int main() {
    int arr[3];
    int i;

    // 3개의 정수 입력
    for (i = 0; i < 3; i++){
        scanf("%d", &arr[i]);
    }

    add_number(arr); // 배열의 첫 번째 원소를 가리키는 포인터로 형변환

    printf("배열의 각 원소 : %d, %d, %d", arr[0], arr[1], arr[2]);
    
    return 0;
}

int add_number(int *parr){
    int i;
    for (i = 0; i < 3; i++){
        parr[i]++;
    }
    return 0;
}
// 10
// 11
// 15
// 배열의 각 원소 : 11, 12, 16
```
