# void

- `void` 형 함수, `void` 형 포인터에 대한 이해
- `main` 함수의 인자에 대한 이해(`argc`, `argv`)
- 포인트 배열

## void 형 포인터

```c
#include <stdio.h>
int main(){
    void* a;
    return 0;
}
```

a 포인터에 메모리 상에 8byte만큼 지정하게 됨.

순전히 주소값의 보관 역할을 수행할 수 있다.

어떤 타입의 포인터의 주소값도 편리하게 담을 수 있다.

출력 시 아래와 같이 형변환을 맞춰줘야 한다.

```c
#include <stdio.h>
int main(){
    void *a;
    double b = 123.3;

    a = &b;
    printf("%lf", *(double *)a);
    return 0;
}

```
<br>

### 활용법

특정 주소값으로부터 1바이트 씩 읽어오는 함수

```c
#include <stdio.h>
int read_char(void *p, int byte);
int main(){
    int arr[1] = {0x12345678};

    printf("%x \n", arr[0]);
    read_char(arr, 4);

    return 0;
}
int read_char(void *p, int byte){
    do {
        printf("%x \n", *(char *)p);
        byte--;

        p = (char *)p + 1;
    } while (p && byte);

    return 0;
}
// 12345678 
// 78 
// 56 
// 34 
// 12 
```

## 메인 함수의 인자

```c
#include <stdio.h>
int main(int argc, char **argv){
    printf("받은 인자의 개수 : %d \n", argc);
    printf("이 프로그램의 경로 : %s \n", argv[0]);

    return 0;
}
```

- 운영체제가 넣어주는 인자

<br>

### 인자를 가지는 메인 함수

```c
#include <stdio.h>
int main(int argc, char **argv){
    int i;
    printf("받은 인자의 개수 : %d \n", argc);

    for (i = 0; i < argc; i++)
        printf("이 프로그램이 받은 인자 : %s \n", argv[i]);

    return 0;
}
```
avgv는 `(char *)형 배열을 가리키는 포인터`이자 포인터 배열이다.

즉, `char *arr[];`를 가리키는 포인터이다.

포인터들의 배열을 가리키고 있고, 그 포인터들은 인자로 전달된 문자열을 가리키고 있다.

따라서, `argv[i]`를 통해 인자의 문자열이 저장된 주소값을 찾을 수 있다.
