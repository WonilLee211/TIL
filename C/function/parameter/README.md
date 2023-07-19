# 함수 인자와 포인터

- 더블 포인터 인자
- 2 차원 배열 인자
- 인자 상수화
- 함수 포인터



## 더블 포인터 인자

![image](https://github.com/WonilLee211/TIL/assets/109330610/330bc236-2918-4582-beec-0d1c21978a9b)

- 포인터가 가리키는 변수 변경

```c
#include <stdio.h>

int pswap(int **ppa, int **ppb);
int main() {
    int a, b;
    int *pa, *pb;

    pa = &a;
    pb = &b;

    printf("pa 가 가리키는 변수의 주소값 : %p \n", pa);
    printf("pa 의 주소값 : %p \n \n", &pa);
    printf("pb 가 가리키는 변수의 주소값 : %p \n", pb);
    printf("pb 의 주소값 : %p \n", &pb);

    printf(" ------------- 호출 -------------- \n");
    pswap(&pa, &pb);
    printf(" ------------- 호출끝 -------------- \n");

    printf("pa 가 가리키는 변수의 주소값 : %p \n", pa);
    printf("pa 의 주소값 : %p \n \n", &pa);
    printf("pb 가 가리키는 변수의 주소값 : %p \n", pb);
    printf("pb 의 주소값 : %p \n", &pb);

    return 0;
}

int pswap(int **ppa, int **ppb){
    int *temp = *ppa;

    printf("ppa가 가리키는 변수의 주소값 : %p \n", ppa);
    printf("ppb가 가리키는 변수의 주소값 : %p \n", ppb);

    *ppa = *ppb;
    *ppb = temp;

    return 0;
}
// pa 가 가리키는 변수의 주소값 : 0x7ffc5ffd7520 
// pa 의 주소값 : 0x7ffc5ffd7528 
 
// pb 가 가리키는 변수의 주소값 : 0x7ffc5ffd7524 
// pb 의 주소값 : 0x7ffc5ffd7530 
//  ------------- 호출 -------------- 
// ppa 가 가리키는 변수의 주소값 : 0x7ffc5ffd7528 
// ppb 가 가리키는 변수의 주소값 : 0x7ffc5ffd7530 
//  ------------- 호출끝 -------------- 
// pa 가 가리키는 변수의 주소값 : 0x7ffc5ffd7524 
// pa 의 주소값 : 0x7ffc5ffd7528 
 
// pb 가 가리키는 변수의 주소값 : 0x7ffc5ffd7520 
// pb 의 주소값 : 0x7ffc5ffd7530
```

- 두 포인터가 가리키는 변수를 서로 바꿔버린 것
- 포인터를 가리키는 형인 `int**`로 인자를 받아서 함수에서 포인터 swap을 진행해야 한다.


## 2 차원 배열 인자

```c
#include <stdio.h>

int add_element(int (*arr)[2], int row);
int main(){
    int arr[3][2];
    int i, j;

    for (i = 0; i < 3; i++){
        for (j = 0; j < 2; j++){
            scanf("%d", &arr[i][j]);
        }
    }

    add_element(arr, 3);

    for (i = 0; i < 3; i++){
        for (j = 0; j < 2; j++){
            printf("arr[%d][%d] : %d \n", i, j, arr[i][j]);
        }
    }
    return 0;
}

int add_element(int (*arr)[2], int row) {
    int i, j;

    for (i = 0; i < row; i++){
        for (j = 0; j < 2; j++){
            arr[i][j]++;
        }
    }
    return 0;
}
```

### 함수의 인자에서만 가능한 배열 인자의 다른 표현

```c
int add_element1(int arr[][3], int row);
```

- 다차원 인자

```c
int multi(int (*arr)[3][2][5]){
    arr[1][1][1][1] = 1;
    return 0;
}

int multi1(int ar[][3][2][5]){
    arr[1][1][1][1] = 1;
    return 0;
}
```

## 인자 상수화

```c
#include <stdio.h>
int read_val(const int val);
int main(){
    int a = 4;
    read_val(a);
    return 0;
}
int read_val(const int val){
    val = 5; // 컴파일 오류 :  error C2166: l-value가 const 개체를 지정합니다.
    return 0;
}
```

## 함수 포인터

- 프로그램의 코드 자체가 메모리 상에 존재함
- 함수의 포인터는 메모리 상에 올라간 함수의 시작 주소를 가리키는 역할

```c
#include <stdio.h>

int max(int a, int b);
int main(){
    int a, b;
    int (*pmax)(int, int);

    a = 10;
    b = 15;
    pmax = max;

    printf("max(a, b) : %d \n", max(a, b));
    printf("pmax(a, b) : %d \n", pmax(a, b));

    return 0;
}
int max(int a, int b){
    if (a > b){
        return a;
    }
    else {
        return b;
    }
    return 0;
}
// max(a,b) : 15 
// pmax(a,b) : 15 
```

<br>

### 함수 포인터의 정의

`(함수 리턴형) (*포인터 이름)(첫 번째 인자 타입, 두 번째 인자 타입, ...);`

`포인터_이름 = 함수_이름;`

- 특정 함수의 주소값은 함수 이름으로 알 수 있음
- `포인터 이름 = &함수_이름;`은 틀린 표현

<br>

### 포인터 인자를 갖는 함수의 포인터

```c
int increase(int (*arr)[3], int row);
int main(){
    int (*pfunc)(int (*)[3], int);
    
    ...
    
    return 0;
}

```
