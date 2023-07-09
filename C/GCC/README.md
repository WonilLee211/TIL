# 우분투 리눅스에서 C 프로그래밍

1. `vim helloworld.c`
2. c 코드 작성

```c
#include <stdio.h>

int main() {
    printf("Hello, World ! \n");
    return 0;
}

```

3. 컴파일
    - `gcc -O helloworld helloworld.c`
3. 파일 실행
    - `./helloworld`