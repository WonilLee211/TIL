# 메모리 동적 할당

- `malloc` 함수의 이해
- 1 차원 배열 동적 할당
- 2 차원 배열 동적 할당

## `malloc()`

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int SizeOfArray;
  int *arr;

  printf("만들고 싶은 배열의 원소의 수 : ");
  scanf("%d", &SizeOfArray);

  arr = (int *)malloc(sizeof(int) * SizeOfArray);
  // int arr[SizeOfArray] 와 동일한 작업을 한 크기의 배열 생성

  free(arr);

  return 0;
}
```

`<stdlib.h>`에 정의되어 있는 메모리 동적 할당 함수

인자로 원하는 메모리의 크기를 전달한다.

자신이 할당한 메모리의 시작주소를 반환한다.

이 때, (void *) 형이므로 사용자가 원하는 형으로 변환시켜야 한다.

할당받은 메모리를 쓰고 난 후, 다시 컴퓨터에게 반납해야 한다.

사용하지 않는 메모리에 대해서 반납하지 않을 경우, **메모리 누수**가 발생할 수 있다.

## 힙(Heap), `malloc` 함수가 사용하는 메모리 영역

힙은 사용자가 자유롭게 할당하거나 해제할 수 있다.

`malloc` 함수도 힙을 사용한다.

인간이 직접 다루는 영역이기 때문에 철저한 관리가 요구된다.

## 동적 할당의 활용


```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
    int student;    // 입력 받고자 하는 학생의 수
    int i, input;
    int *score;     // 학생들의 수학 점수 변수
    int sum = 0;    // 총점

    printf("학생의 수는? : ");
    scanf("%d", &student);
    
    score = (int *)malloc(sizeof(int) * student);

    for (i = 0; i < student; i++){
        printf("학생 %d 의 점수 : ", i);
        scanf("%d", &input);

        arr[i] = input;
    }

    for (i = 0; i < student; i++)
        sum += arr[i];

    printf("전체 학생 평균 점수 : %d \n", sum / student);
    free(arr);

    return 0;
}
// 학생의 수는? : 3
// 학생 0 의 점수 : 100
// 학생 1 의 점수 : 90
// 학생 2 의 점수 : 95
// 전체 학생 평균 점수 : 95 
```


## 2 차원 배열의 동적 할당

할당 방법은 크게 두 가지가 있다.

1. 포인터 배열을 사용해서 2 차원 배열처럼 동작하는 배열을 만드는 방법
2. 실제로 2 차원 배열 크기의 메모리를 할당한 뒤 2 차원 배열 포인터로 참조하는 방법

<br>

## 방법 1. 포인터 배열을 이용하여 2 차원 배열 할당하기

각 포인터 원소들이 다른 1 차원 배열을 가리키도록 한다.

먼저, 포인터 배열을 동적 할당한다.
다시 포인터 배열의 각각의 원소(포인터)들이 가리키는 1 차원 배열을 다시 동적으로 할당한다.

*위 방법은 2 차원 배열처럼 모든 원소들이 메모리 공간에 연달아 존재한다고 보장할 수 없다.*

```c
#include <stdio.h>
include <stdlib.h>

int main(int argc, char **argv){
    int i;
    int x, y;
    int **arr; // 우리는 arr[x][y]를 만들 것이다.

    printf("arr[x][y] 를 만들 것입니다. \n");
    scanf("%d %d", &x, &y);
    // int* 형의 원소를 x 개 가지는 1 차원 배열 생성
    arr = (int **)malloc(sizeof(int *) * x);

    for (i = 0; i < x; i++)
        arr[i] = (int *)malloc(sizeof(int) * y);

    printf("생성 완료! \n");

    for (i = 0; i < x; i++){
        free(arr[i]);
    }
    free(arr);

    return 0;
}
// arr[x][y] 를 만들 것입니다.
// 3
// 5
// 생성 완료! 
```


1. 포인터 배열, `int **arr`를 선언한다.
2. `(int *)` 형 배열을 가리킬 포인터를 저장할 공간을 동적으로 할당한다.
    - `arr = (int **)malloc(sizeof(int *) * x);`
3. `(int)`형 배열을 가리킬 포인터를 저장할 공간을 동적으로 할당한다.
    - `arr[i] = (int *)malloc(sizeof(int) * y);`
4. 힙에 할당한 해당 배열을 사용한 후 반환한다
    - `for (i = 0; i < x; i++) free(arr[i]);`
    - `free(arr);`
    - 여기서 반환 순서를 지켜야 한다.


## 방법 2. 진짜 2 차원 배열 할당하기

메모리에 연속적으로 존재하는 진짜 2 차원 배열을 만들기 위해 반드시 `malloc` 함수를 통해 해당 크기의 공간을 할당해야 한다.

`int arr[height][width];`와 같은 배열을 할당하고자 한다.

`int (*arr)[width] = (int *[width])malloc(width * height * sizeof(int));`

- 컴파일러에 열의 크기가 `width`인 2 차원 배열을 가리키는 `arr`라고 선언하는 것을 의미한다.
- 위 방법은 컴파일러에 따라 오류가 발생할 수 있다.
    - 비주얼 스튜디오의 경우 파일 확장자를 .c 로 지정해야하고, GCC 를 사용하시는 분들은 g++ 이 아니라 gcc 로 컴파일 해야 합니다.

```c
#include <stdio.h>
#include <stdlib.h>
int main(){
    int width, height, data;
    printf("배열 행 크기 : ");
    scanf("%d", &width);
    printf("배열 열 크기 : ");
    scanf("%d", &height);

    int (*arr)[width] = (int *[width])malloc(height * width * sizeof(int));
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            scanf("%d", &data);
            arr[i][j] = data;
        }
    }
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++)
            printf("%d ", arr[i][j]);
        printf("\n");
    }
    free(arr);
    
    return 0;
}
// 배열 행 크기 : 3
// 배열 열 크기 : 2
// 1 2 3 4 5 6
// 1 2 3 
// 4 5 6 
```
<br>

### 메모리 동적 할당한 2 차원 배열을 함수 인자로 전달하기

`void print_arr(int (*arr)[width], int width, int height);`와 같은 함수 원형을 사용해야 하는데 포인터의 width 값을 모르기에 컴파일 에러가 발생한다.

인자의 순서를 변경함으로써 컴파일 에러를 방지할 수 있다.


```c
void print_arr(int width, int height, int (*arr)[width]){
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}
```

