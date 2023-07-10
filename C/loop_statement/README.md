# 반복문

## 무한 루프

1. for-loop

```c

#include <stdio.h>

void main() {

    int usrAnswer;

    printf("컴퓨터가 생각한 숫자를 맞춰보세요! \n");

    for (;;) {
        scanf("%d", &usrAnswer);
        if (usrAnswer == 3){
            printf("맞추셨군요! \n");
            break;
        }
        else {
            printf("틀렸어요! \n");
        }
    }
    return;
}
```

<br>

2. while-loop

```c
#include <stdio.h>


void main() {

    int usrAnswer;

    printf("컴퓨터가 생각한 숫자를 맞춰보세요! \n");

    while (true) {
        scanf("%d", &usrAnswer);
        if (usrAnswer == 3){
            printf("맞추셨군요! \n");
            break;
        }
        else {
            printf("틀렸어요! \n");
        }
    }
    return;
}
```

