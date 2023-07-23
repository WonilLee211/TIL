# 열거형(Enum)

```c
#include <stdio.h>
enum { RED, BLUE, WHITE, BLACK };
int main(){
    int palette = RED;
    switch (palette){
        case RED:
            printf("palette : RED \n");
            break;
        case BLUE:
            printf("palette : BLUE \n");
            break;
        case WHITE:
            printf("palette : WHITE \n");
            break;
        case BLACK:
            printf("palette : BLACK \n");
            break;
    }
    return 0;
}
// palette : RED 
```

- compiler는 각 원소에 차례로 정수값을 매겨줌
- 컴파일할 때 열거형 내에 모든 단어는 매칭되는 정수로 등변환된다.
- 아래 두 조건이 모두 가능하다.
    - `if (palette == 0)  // 현재 파레트의 색이 빨강인지 확인한다.`
    - `if (palette == RED)  // 현재 파레트의 색이 빨강인지 확인한다.`


## 열거형 시작값 변경

`enum { RED = 3, BLUE, WHITE, BLACK };`

RED = 3 부터 해서 BLUE = 4, WHITE = 5, BLACK = 6 이 된다.

`enum { RED = 3, BLUE, WHITE = 3, BLACK };`

수를 지정한 부분 부터 다시 시작 되는 방식으로 BLUE = 4, BLACK = 4 가 된다.

참고로 열거형 에서는 언제나 '정수값' 이여야 한다.
