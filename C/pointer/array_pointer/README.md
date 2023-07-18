# 배열 포인터

- 1 차원 배열을 가리키는 포인터
- 2 차원 배열을 가리키는 포인터(배열 포인터)
- 포인터 배열
- 더블 포인터(`**`)

## 1 차원 배열 가리키기

```c
#include <stdio.h>
int main(){
    int arr[3] = {1, 2, 3};
    int *arrP;
    arrP =  arr; // arrP = &arr[0];

    printf("arr[1] : %d \n", arr[1]);
    printf("arrP[1] 값 : &d \n", arrP[1]);

    return 0;
}

// arr[1] : 2 
// parr[1] : 2 
```

- `arr`는 배열의 첫 번째 원소를 가리키는 포인터로 변환이 된다.
- 그 원소의 타입은 `int`이며, 포인터의 타입은 `int*`가 된다.

```c
#include <stdio.h>
int main(){
  int arr[10] = {100, 98, 97, 95, 89, 76, 92, 96, 100, 99};
  int *arrP;
  
  arrP = arr;
  int sum = 0;
  while (arrP - arr < 10){
    sum += *arrP;
    arrP++;
  }

  printf("점수 평균 : %d \n", sum / 10);

  return 0;
}
// 점수 평균 : 94 
```

- 포인터와 배열의 이름의 차이는 연산자의 동작에서 발생한다.
    - `arrP++` : 주소값의 증가를 의미한다. int 형 크기에 따라 4바이트가 증가한다.
    - `arr++` : arr이름은 커파일러가 첫 번째 원소의 주소로 인식하지만, ++연산자가 동작하지 않아, 컴파일 에러가 발생한다.

## 포인터의 포인터

![image](https://github.com/WonilLee211/TIL/assets/109330610/ce566f4e-d247-4e6a-95e8-3b375ab744e5)

`int **p;`

```c
#include <stdio.h>
int main(){
    int a;
    int *pa;
    int **ppa;

    pa = &a;
    ppa = &pa;
    
    a = 3;

    printf("a : %d // *pa : %d // **ppa : %d \n", a, *pa, **ppa);
    printf("&a : %p // pa : %p // *ppa : %p \n", &a, pa, *ppa);
    printf("&pa : %p // ppa : %p \n", &pa, ppa);

}
// a : 3 // *pa : 3 // **ppa : 3 
// &a : 0x7ffd26a79dd4 // pa : 0x7ffd26a79dd4 // *ppa : 0x7ffd26a79dd4 
// &pa : 0x7ffd26a79dd8 // ppa : 0x7ffd26a79dd8
```

## 배렬 이름의 포인터



```c
#include <stdio.h>

int main() {
  int arr[3] = {1, 2, 3};
  int (*arrP)[3] = &arr;

  printf("arr[1] : %d \n", arr[1]);
  printf("arrP[1] : %d \n", (*arrP)[1]);

  return 0;
}
// arr[1] : 2 
// parr[1] : 2 
```

- `&arr`를 보관할 포인터는 크기가 3인 배열은 가리키는 포인터가 되어야 한다.
- `int (*arrP)[3]` : C 문법 상 크기가 3인 배열을 가리키는 포인터를 선언
- `arrP` : 크기가 3인 배열을 가리키는 포인터
    - `arr[1] = (*arrP)[1]`와 같이 사용해야 한다.
    - 하지만 `arr`와 `arrP`는 다른 타입임을 명심해야 한다.
    - `arr` 자체가 메모리 공간에 존재하지 않기 떄문.

## 2 차원 배열의 [] 연산자

### `int a[2][3];`

-  2 차원 배열은 메모리 상에 1 차원 배열 여러 개가 연속적으로 존재하는 것과 같다.

### `int a[0]` 의 의미

```c
#include <stdio.h>
int main(){
  int arr[2][3];

  printf("arr[0] : %p \n", arr[0]);
  printf("&arr[0][0] : %p \n", &arr[0][0]);
  printf("arr[1] : %p \n", arr[1]);
  printf("&arr[1][0] : %p \n", &arr[1][0]);
  
  return 0;
}
// arr[0] : 0x7ffda354e530 
// &arr[0][0] : 0x7ffda354e530 
// arr[1] : 0x7ffda354e53c 
// &arr[1][0] : 0x7ffda354e53c 
```

- 1차원 배열과 마찬가지로 `[]` 연산자를 사용하지 않을 경우, `arr[n]`은 `arr[n][m]`을 가리키는 포인터로 타입변환된다.

## 포인터의 형(type)을 결정짓는 두 가지 요소

### `int arr[a][b];` 2 차원 배열의 원소 주소값 계산법

`arr + 4bx + 5y`

- `arr[x][y]`원소에 접근할 때 주소값 계산법

### **2 차원 베열을 가리키는 포인터를 통해서 원소들을 정확히 접근하기 위해 필요한 정보**
  1. 가리키는 원소의 크기
  2. b의 값(열의 길이)
- 두 정보가 포인터의 타입에 명시되어야 컴파일러가 원소에 올바르게 접근할 수 있음

## 2 차원 배열을 가리키는 포인터

`(배열의 형) (*포인터이름)[2 차원 배열의 열 개수];`

- 2차원 배열을 가리키는 포인터는 배열의 크기에 관한 정보를 알 수 있도록 선언되어야 함


`int (*arrP)[b];`

- `arrP`는 `int` 형 원소의 열의 개수가 b인 2 차원 배열을 가리키는 포인터
- 다른 말로, 크기가 b인 배열을 가리키는 포인터
- 1 차원 배열에서 배열의 이름이 첫 번째 원소를 가리키는 포인터로 형변환되었듯, 2 차원 배열에서 배열의 이름은 배열의 첫 번째 행을 가리키는 포인터로 형변환되어야 함


```c
#include <stdio.h>
int main() {
  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int (*arrP)[3];

  arrP = arr; // arrP가 arr를 가리키게 됨

  printf("arrP[1][2] : %d, arr[1][2] : %d \n", arrP[1][2], arr[1][2]);

  return 0;
}
// parr[1][2] : 6 , arr[1][2] : 6 
```

### 오류코드

```c
#include <stdio.h>
int main(){
  int arr[2][3];
  int brr[10][3];
  int crr[2][5];

  int (*arrP)[3];

  arrP = arr; // ok
  arrP = brr; // ok
  arrP = crr; // error

  return 0;
}
```

### 2 차원 배열을 가리키는 포인터 에러코드 분석

```c
#include <stdio.h>
int main() {
  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int **arrP;

  arrP = arr;

  printf("arrP[1][1] : %d \n", arrP[1][2]); // bugggggggg

  return 0;
}
```

`arrP[1][1]` 

- `= *(*(arrP + 1) + 1)`
- `arrP + 1`
  - `arrP` : `int*`를 가리키는 포인터
  - 주소값 크기인 8이 더해짐
- `*(arrP + 1)`
  - `= 3`
- `*(arrP + 1) + 1`
  - `*(arrP + 1)`의 타입은 `int` 형
  - `3 + 4 = 7`
- `*(7)` : 주소값 7을 읽어라!고 명령하기에 오류 발생


## 포인터 배열

- 포인터들의 배열

```c
#include <stdio.h>

int main() {
  int *arr[3];
  int a = 1, b =2, c = 3;
  arr[0] = &a;
  arr[1] = &b;
  arr[2] = &c;

  printf("a : %d, *arr[0] : %d \n", a, *arr[0]);
  printf("b : %d, *arr[1] : %d \n", b, *arr[1]);
  printf("c : %d, *arr[2] : %d \n", c, *arr[2]);

  printf("&a : %p, arr[0] : %p \n", &a, arr[0]);
  
  return 0;
}
// a : 1, *arr[0] : 1 
// b : 2, *arr[1] : 2 
// b : 3, *arr[2] : 3 
// &a : 0x7ffe8a2fa4e4, arr[0] : 0x7ffe8a2fa4e4
```