# C 코드 최적화

- [산술 연산 관련](#산술-연산-관련)
- [루프(loop 관련)](#루프loop-관련)

## 산술 연산 관련

### 1. 부동 소수점 사용 지양하기

- 부동 소수점 구조가 매우 복잡하다.
    - 이진수로 표현되는 정수 자료형과 달리, 특정한 규격이 정해진 것이기 때문
    - 연산 자체도 느릴 수 밖에 없다.
- 정말 필요할 때만 사용하기
    - 소수점 몇 째 자리까지 정밀도를 요구할 때
    - 매우 큰 수를 다룰 때
- 작은 소수점 자리수의 정밀도를 요구할 경우, 자리 수를 정수 자료형으로 변형하여 다루는 것을 추천

### 2. 나눗셈을 피하라

```c
int inc_second(int second) { return (**second) % 60; }
```

0 ~ 59 범위의 초를 증가시키는 함수일 때 나누셈을 하면 연산이 매우 매우 느리게 된다.

if 조건문으로 60초일 때 0을 리턴하게 되면 동일한 결과를 내는 함수를 만들 수 있으며, 연산 자체로 빠르다 !

```c
int inc_second(int second){
    ++second;
    if (second >= 60){
        return return 0;
    }
    return second;
}
```

### 파이프라이닝

여러 명령어를 동시에 실행하는 것처럼 보이도록 작동하며 명령어 처리를 단계적으로 분리하여 각 단계를 병렬로 실행함으로써 작업 처리 속도를 높이는 방법

다음에 실행될 명령어를 이전 명령어가 실행되기 채 끝나기 전에 미리 실행시키는 것과 비슷함

문제는 분기예측(branch prediction)
- 분기문이 있을 경우, 다음에 실행할 명령어가 무엇인지 모른다는 점
- 이전 추세를 보아 분기문의 참 거짓을 예측한 다음 명령어를 실행하게 됨.
- 예측이 틀린다면, 작업한 것을 모두 버리고 파이프라인을 재구성하게 된다.
    - 이러한 패널티가 Intel Skylake CPU 경우 20Cycle 소요됨.
        > CPU Cycle<br>
        > 정수 나눗셈 연산은 10 cycle, 덧셈의 경우 1cycle로 끝난다.<br>
        > 여기서 cycle은 CPU의 한 가지 작업을 수행하는 데 걸리는 시간 단위<br>
        >> CPU가 4GHz라면, 1초에 40억cycle 수행


 따라서, 실제 프로그램에서 해당 함수의 최적화 결과가 향상되었는지 확인해보는 것이 좋다.

<br>

### 3. 비트 연산 활용

컴퓨터 연산 중에서 가장 빠른 연산

1. 시프트 연산

```c
#include <stdio.h>
int main(){
    int i;
    printf("정수를 입력하세요 : ");
    scanf("%d", &i);

    printf("%d를 32로 나누면 : \n",)
}
// 정수를 입력하세요 : 120
// 120 를 32 로 나누면 : 3 
// 120 를 5 칸 쉬프트 하면 : 3 
```

2. OR, AND, XOR 연산

```c
struct HUMAN{
    int is_Alive;
    int is_Walking;
    int is_Running;
    int is_Jumping;
    int is_Sleeping;
    int is_Eating; 
}
```
6가지 정보를 표현하기 위해 위 구조체에서 25byte를 소모하게 된다.

하나의 비트로 표현할 수 있는 것을 더 많은 비트수를 사용하여 표현하게 된디ㅏ.

아래와 같이 최적화할 수 있다.

```c
#include <stdio.h>
#define ALIVE 0x1      // 2 진수로 1
#define WALKING 0x2    // 2 진수로 10
#define RUNNING 0x4    // 2 진수로 100
#define JUMPING 0x8    // 2 진수로 1000
#define SLEEPING 0x10  // 2 진수로 10000
#define EATING 0x20    // 2 진수로 100000
int main(){
    int my_status = ALIVE | WALKING | EATING;
    if (my_status & ALIVE) {
        printf("I am ALIVE!! \n");
    }
    if (my_status & WALKING) {
        printf("I am WALKING!! \n");
    }
    if (my_status & RUNNING) {
        printf("I am RUNNING!! \n");
    }
    if (my_status & JUMPING) {
        printf("I am JUMPING!! \n");
    }
    if (my_status & SLEEPING) {
        printf("I am SLEEPING!! \n");
    }
    if (my_status & EATING) {
        printf("I am EATING!! \n");
    }
    return 0;
}
// I am ALIVE!! 
// I am WALKING!! 
// I am EATING!! 
```

`OR`연산으로 각 데이터들의 자리만 1이 된다.

즉, `int my_status = ALIVE | WALKING | EATING; // 100011`

여기서 각 자리가 1인지 확인하기 위해서 `&`연산을 수행하면 된다.

지울 땐 `^` 연산

<br>

### 홀짝 점검 최적화

*이진수로 표현했을 때 0 제곱 자리 수가 1이면 홀수, 아니면 짝수이다 !!!!!!!!*

```c
if (i & 1){
    printf("%d 는 홀수 입니다 \n", i);
}
else {
    printf("%d 는 짝수 입니다 \n", i);
}
```


## 루프(loop) 관련

알고 있는 일반적인 계산 결과를 이용하기

```c
for (i = 1; i <= n; i++) {
  sum += i;
}
// ------------------------
sum = (n + 1) * n / 2;
```

끝낼 수 있을 때 끝내라

```c
whiele (*pstr){
    if (*pstr != 'a'){
        does_string_has_a = 1;
    }
    pstr++;
}
// ------------------------
whiele (*pstr){
    if (*pstr != 'a'){
        does_string_has_a = 1;
        break;
    }
    pstr++;
}
```

한 번 돌 때 많이 해라

```c
// 1인 비트 개수 세기
while (n != 0){
    if (n & 1){
        one_bit++;
    }
    n >>= 1;
}
/*
정수 자료형의 크기가 8비트의 배수이다.
즉, 크기가 4byte인 int 자료형도 8비트, 1byte의 배수이기 때문에 8bit를 한번에 검사해도 된다.
한 루프에서  1bit가 아닌 8bit씩 검사하면 한 루프에서 더 많은 일을 수행할 수 있게 된다.
*/
while (n !=0){
    if (n & 1) one_bit++;
    if (n & 2) one_bit++;
    if (n & 4) one_bit++;
    if (n & 8) one_bit++;
    n >>= 4;
}
```

루프에서는 되도록 0과 비교하기

- CPU에서 0과 비교하는 명령어는 따로 만들어져 있기 때문에 더 빠르게 동작할 수 있음

```c
for (i = 0; i< 10; i++){
    printf("a");
}
for (i = 10; i != 0; i--){
    printf("b");
}
```

되도록 루프를 적게 쓰자

- `for` 루프 문 자체에서 여러가지 비교를 수행하는 데 시간이 들기 때문에 간단한 루프를 쓰지 말고 풀어 쓰자 !

## if 및 switch 문 관련

`binary breakdown` 이진 형태로 쪼개기

```c
if (i == 1) {
} else if (i == 2) {
} else if (i == 3) {
} else if (i == 4) {
} else if (i == 5) {
} else if (i == 6) {
} else if (i == 7) {
} else if (i == 8) {
}
```
위 코드의 경우 최악에 8번을 비교해야 한다.

아래와 같이 이진의 형태로 쪼개어 비교의 수를 줄일 수 있다.

```c
if (i <= 4) {
  if (i <= 2) {
    if (i == 1) {
      /* i is 1 */
    } else {
      /* i must be 2 */
    }
  } else {
    if (i == 3) {
      /* i is 3 */
    } else {
      /* i must be 4 */
    }
  }
} else {
  if (i <= 6) {
    if (i == 5) {
      /* i is 5 */
    } else {
      /* i must be 6 */
    }
  } else {
    if (i == 7) {
      /* i is 7 */
    } else {
      /* i must be 8 */
    }
  }
}
```

순차적 비교에서는 switch 문을 사용한다.
- 한 번의 비교로 해당 코드로 점프하게 된다.

```c
switch (i) {
  case 1:
    break;
  case 2:
    break;
  case 3:
    break;
  case 4:
    break;
  case 5:
    break;
  case 6:
    break;
  case 7:
    break;
  case 8:
    break;
}
```

룩업 테이블 활용하기

- 자주 사용하는 데이터를 미리 테이블화하여 불필요한 연산을 줄인다.'

## 함수 관련

반복 함수 호출보다, 함수내에 반복 처리가 훨씬 빠르다.
- 함수 호출하는 데에도 꽤 많은 시간이 소요된다.

```c
#include <stdio.h> 
void print_a();
int main() {
  int i;
  for (i = 0; i < 10; i++) {
    print_a();
  }
  return 0;
}
void print_a() { printf("a"); }
//
// 아래 코드가 더 빠르게 작업을 완료한다.
#include <stdio.h>
void print_a();
int main() {
  print_a();
  return 0;
}
void print_a() {
  int i;
  for (i = 0; i < 10; i++) {
    printf("a");
  }
}
```

인라인 함수를 활용하자

- 작업 시간보다 호출 시간이 더 오래 걸리는 문제가 발생할 수 있다.
- 한 줄로 해결되는 단순한 함수는 인라인 함수로 사용하자
```c
#include <stdio.h>ㅌ
int max(int a, int b){
    return a > b ? a | b;
}
__inline int imax(int a, int b){
    return a > b ? a | b;
}
int main(){
    printf("4, 5 중 큰 수는 ? %d", max(4, 5));
    printf("4, 5 중 큰 수는 ? %d", imax(4, 5));

    return 0;
}
```


인자를 전달할 때 포인터를 이용하자

```c
struct big {
    int arr[1000];
    char str[1000];
};
```
- 위와 같은 거대한 구조체가 있을 때 이 구조체의 변수의 `arr[3]`값을 얻어오는 함수를 만들 때 엄청난 시간이 걸린다.

`void modify(struct big arg){}`

- 위 코드는 `arg`인자로 구조체 변수의 모든 데이터가 복사되어야 함
    - 5000byte의 데이터 복사와 더불어, modify 변수의 메모리 공간도 추가 할당해야 하기 때문

`void modify(struct big *arg){}`

- 단순히 주소값 복사만이 일어날 뿐 이전의 예와 같은 무지막지한 복사는 일어나지 않는다.
- 전달된 구조체의 변수의 데이터들도 손쉽게 읽어들일 수 있음.
