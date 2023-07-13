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

## 배열을 가리키는 포인터 2



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
