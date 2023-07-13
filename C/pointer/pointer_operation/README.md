# 상수 포인터와 연산

- 포인터의 덧셈, 뺄셈
- 배열과 포인터와의 관계
- `[]` 연산자

## 포인터의 덧셈

```c
#include <stdio.h>

int main() {
    int a;
    int* pa;
    pa = &a;

    printf("pa의 값 : %p \n", pa);
    printf("(pa + 1)의 값 : %p \n", pa + 1);

    return 0;
}
// pa 의 값 : 0x7ffd6a32fc4c 
// (pa + 1) 의 값 : 0x7ffd6a32fc50
```

- 0x7ffd6a32fc50 - 0x7ffd6a32fc4c = 4
    - `pa + 1` 연산 결과 주소값이 4 증가하게 됨
    - 이는 포인터의 형이 `int*`이기 때문에 형의 크기인 4byte를 더하게 됨

```c
/* 포인터 형에 따른 덧셈 결과 */
#include <stdio.h>

int main(){
    int a;
    char b;
    double c;
    int* pa = &a;
    char* pb = &b;
    double* pc = &c;

    printf("pa의 값 : %p \n", pa);
    printf("(pa + 1)의 값 : %p \n", pa + 1);
    printf("pb의 값 : %p \n", pb);
    printf("(pb + 1)의 값 : %p \n", pb + 1);
    printf("pc의 값 : %p \n", pc);
    printf("(pc + 1)의 값 : %p \n", pc + 1);
}
// pa의 값 : 0x7ffcf64a2e04 
// (pa + 1)의 값 : 0x7ffcf64a2e08 
// pb의 값 : 0x7ffcf64a2e03 
// (pb + 1)의 값 : 0x7ffcf64a2e04 
// pc의 값 : 0x7ffcf64a2e08 
// (pc + 1)의 값 : 0x7ffcf64a2e10 
```

- `char`형 포인터의 + 1 연산은 1byte 증가, `double`형 포인터의 + 1 연산은 8byte가 증가하는 것을 확인할 수 있음

## 포인터 뺄셈

```c
#include <stdio.h>

int main() {
    int a;
    int* pa = &a;

    printf("pa 의 값 : %p \n", pa);
    printf("(pa - 1) 의 값 : %p \n", pa - 1);

    return 0;
}
// pa 의 값 : 0x7ffe4f4fa47c 
// (pa - 1) 의 값 : 0x7ffe4f4fa478
```

- 차이값이 4임을 알 수 있음

## 포인터간 덧셈

```c
#include <stdio.h>

int main(){
    int a;
    int* pa = &a;
    int b;
    int* pb = &b;
    int* pc = pa + pb; // 컴파일 에러코드 : error C2110: '+' : 두 포인터를 더할 수 없습니다.


    return 0;
}
```

- 포인터간 덧셈은 의미가 없기 때문에 C언어에서는 수행할 수 없다.
- 하지만, 포인터간 뺄셈은 가능하다 !

## 포인터간 대입

```c
#include <stdio.h>

int main(){
    int a;
    int* pa = &a;
    int b;
    int* pb = &b;

    *pa = 3;
    pb = pa;

    printf("pa 가 가리키고 있는 것 : %p \n", *pa);
    printf("pb 가 가리키고 있는 것 : %p \n", *pb);

    return 0;
}
// pa 가 가리키고 있는 것 : 3 
// pb 가 가리키고 있는 것 : 3
```
- 포인터 간 주소 공유(대입)가 가능하다.
- 이 때 두 포인터의 형은 같아야 한다.

## 배열과 포인터

`int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};`
<br>

![image](https://github.com/WonilLee211/TIL/assets/109330610/1c438f05-af51-4ab0-906a-4e1f4fac0b5d)

- 배열은 위와 같이 메모리 상에 연속된 형태로 나타난다.
- int 형 변수이기 때문에 4byte를 차지하게 된다.

```c
#include <stdio.h>

int main(){
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int i;

    for (i = 0; i < 10; i++){
        printf("arr[%d] 의 주소값 : \n", i, &arr[i]);
    }
    return 0;
}
// arr[0] 의 주소값 : 0x7ffeb5683890 
// arr[1] 의 주소값 : 0x7ffeb5683894 
// arr[2] 의 주소값 : 0x7ffeb5683898 
// arr[3] 의 주소값 : 0x7ffeb568389c 
// arr[4] 의 주소값 : 0x7ffeb56838a0 
// arr[5] 의 주소값 : 0x7ffeb56838a4 
// arr[6] 의 주소값 : 0x7ffeb56838a8 
// arr[7] 의 주소값 : 0x7ffeb56838ac 
// arr[8] 의 주소값 : 0x7ffeb56838b0 
// arr[9] 의 주소값 : 0x7ffeb56838b4
```

- 이는 포인터로도 배열원 원소에 쉽게 접근할 수 있다는 뜻이 된다.
- 즉 p 라는 포인터가 int a; 를 가리킨다면 p + 1 을 할 때 p 의 주소값에 사실은 1*4 가 더해지고, p + 3 을 하면 p 의 주소값에 3 * 4 인 12 가 더해진다는 것

<br>

### 배열의 원소를 가르키는 포인터

```c
#include <stdio.h>

int main(){
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int* arrP;
    int i;
    arrP = &arr[0];

    for (i = 0; i < 10; i++){
        printf("arr[%d] 의 주소값 : %p ", i, &arr[i]);
        printf("(arrP + %d) 의 값 : %p ",i, arrP + i);

        if (&arr[i] == (arrP + i)){
            // 만일 (arrP + 1) 가 성공적으로 arr[i]를 가르킨다면
            printf("--> 일치 \n");
        }
        else {
            printf("--> 불일치 \n");
        }
    }
    return 0;
}
// arr[0] 의 주소값 : 0x7ffedbe31530 (parr + 0) 의 값 : 0x7ffedbe31530  --> 일치 
// arr[1] 의 주소값 : 0x7ffedbe31534 (parr + 1) 의 값 : 0x7ffedbe31534  --> 일치 
// arr[2] 의 주소값 : 0x7ffedbe31538 (parr + 2) 의 값 : 0x7ffedbe31538  --> 일치 
// arr[3] 의 주소값 : 0x7ffedbe3153c (parr + 3) 의 값 : 0x7ffedbe3153c  --> 일치 
// arr[4] 의 주소값 : 0x7ffedbe31540 (parr + 4) 의 값 : 0x7ffedbe31540  --> 일치 
// arr[5] 의 주소값 : 0x7ffedbe31544 (parr + 5) 의 값 : 0x7ffedbe31544  --> 일치 
// arr[6] 의 주소값 : 0x7ffedbe31548 (parr + 6) 의 값 : 0x7ffedbe31548  --> 일치 
// arr[7] 의 주소값 : 0x7ffedbe3154c (parr + 7) 의 값 : 0x7ffedbe3154c  --> 일치 
// arr[8] 의 주소값 : 0x7ffedbe31550 (parr + 8) 의 값 : 0x7ffedbe31550  --> 일치 
// arr[9] 의 주소값 : 0x7ffedbe31554 (parr + 9) 의 값 : 0x7ffedbe31554  --> 일치

```

- 이제 `*` 연산자를 이용하여 포인터로 배열의 값을 조회할 수 있게 된다.

```c
#include <stdio.h>

int main(){
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int* arrP;

    arrP = &arr[0];
    
    printf("arr[3] = %d, *(arrP + 3) = %d \n", arr[3], *(arrP + 3));

    return 0;
}
// arr[3] = 4 , *(parr + 3) = 4 
```

- 포인터의 덧셈이 형의 크기에 따라 증가하는 이유가 여기서 해결된다.

## 배열의 이름의 비밀

```c
#include <stdio.h>
int main() {
  int arr[3] = {1, 2, 3};

  printf("arr 의 정체 : %p \n", arr);
  printf("arr[0] 의 주소값 : %p \n", &arr[0]);

  return 0;
}
// arr 의 정체 : 0x7fff1e868b1c 
// arr[0] 의 주소값 : 0x7fff1e868b1c 
```

- 배열의 이름을 출력하면 첫번째 원소 주소가 출력된다.
- 하지만 배열의 이름을 배열의 첫 번째 원소를 가르키는 포인터라고 할 수 없다.

## 배열은 배열이고 포인터는 포인터다.

```c
#include <stdio.h>
int main(){
    int arr[6] = {1, 2, 3, 4, 5, 6};
    int* arrP = arr;

    printf("sizeOf(arr) : %d \n", sizeOf(arr));
    printf("sizeOf(arrP) : %d \n", sizeOf(arrP));
}
// Sizeof(arr) : 24 
// Sizeof(parr) : 8
```

- `sizeOf(arr)`는 배열의 실제 크기인, `원소 6 개 * 4byte = 24`
- `sizeOf(arrP)`는 포인터의 크기인, 8byte(64비트 컴퓨터이므로 8byte 주소)
- `sizeOf` 연산자나 주소값 연산자(`&`)가 사용되는 경우를 제외하고 **배열의 이름**을 사용 시 암묵적으로 첫 번재 원소를 가르키는 포인터 타입으로 변환됨

## []연산자

- 배열의 형태를 `*(arr + 3)`과 같이 변환하는 연산자

```c
/* [] 연산자 */
#include <stdio.h>
int main() {
  int arr[5] = {1, 2, 3, 4, 5};

  printf("arr[3] : %d \n", arr[3]);
  printf("*(arr+3) : %d \n", *(arr + 3));
  printf("3[arr] : %d \n", 3[arr]);

  return 0;
}
// a[3] : 4 
// *(a+3) : 4
// 3[arr] : 4 
```

- 세 번째 출력 코드와 같이 `3[arr]`와 같은 코드도 동작하게 된다.

## 포인터의 정의

- 한번에 여러 포인터 선언
    - `ìnt *a, *b, *c;`
- 하나의 포인터와 여러 int 형 변수 선언
    - `int *a, b, c;`
 