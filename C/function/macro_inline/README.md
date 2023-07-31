# 매크로 함수와 인라인 함수

`#define 함수_이름(인자...) 치환할_대상`

- `#define` 전처리 지시문을 사용하여 정의
- 미리 정의된 텍스트 블록을 코드로 대채하는 기능을 재공하는 함수
- 예시 : `#define square(x) x*x`
    - `square(x)`를 `x * x`로 치환하게 됨

## `#` in `#define`

인자 앞에 `#`을 붙일 경우 해당 인자를 문자열로 바꿔 버린다.

```c
#include <stdio.h>
#define PrintVariableName(var) printf(#var "\n");

int main(int argc, char **argv) {
  int a;

  PrintVariableName(a);
  //printf("a" "\n"); = printf("a\n");


  return 0;
}
// a
```

- C언어에서 연속한 두 개의 문자열은 그냥 하나로 합쳐진다.


## `##` in `#define`

```c
#include <stdio.h>
#define AddName(x, y) x##y

int main(int argc, char **argv) {
  int AddName(a, b); // int ab;

  ab = 3;

  printf("%d \n", ab);

  return 0;
}
// 3
```

입력된 것을 하나로 합치는 역할

## 인라인 함수

```c
__inline int square(int a){ return a * a; }
int main(int argc, int **argv){
  printf("%d", square(3));
  
  return 0;
}
```

인라인 함수는 `__inline`만 빼면 일반 함수 선언과 동일하다.

하지만, 동작은 전혀 다르다. 일반함수는 프로그램의 흐름이 함수로 넘어가게 된다. 즉, 함수를 호출하는 과정이 추가된다.

이는 간단한 수행을 하는 함수가 시간이 비교적 소모적이게 된다.

인라인 함수는 매크로 함수와 같이 치환되지만, 매크로 함수와도 차이가 있다.

매크로 함수의 단점인 무식한 치환이 아닌, 컴파일러가 문장 내부에서 함수와 같이 연산 우선순위를 지켜준다.

아래와 같이 연산 우선순위를 지켜준다.

```c
__inline int square(int a){ return a * a; }
int main(int argc, int **argv){
  printf("%d", square(3 + 1));
  /*
  printf("%d", (3 + 1) * (3 + 1));
  */
  return 0;
}
```

