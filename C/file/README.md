# 파일 입출력에 대한 기본적인 이해

- 파일 입출력이란?
- 스트림이란 무엇인가
- `fopen, fputs, fgets, fgetchar`함수에 대한 이해
- 파일 위치 지정자와 `fseek`함수에 대한 이해

## 파일 입출력이란?

파일에 출력하기
```c
#include <stdio.h>
int main(){
    FILE *fp;
    fp = fopen("a.txt", "w");

    if (fp == NULL){
        printf("Write Error! \n");
        return 0;
    }

    fputs("Hello World!!! \n", fp);

    fclose(fp);x
    return 0;
}
```

위와 같이 `fopen`함수는 운영체제가 우리가 지정한 파일과 소통할 수 있도록 스트림을 만들어준다.
<br>

### 스트림

![image](https://github.com/WonilLee211/TIL/assets/109330610/2ffc511e-fdba-44b7-ab16-a46a9a2ee0ae)

- 두 개의 완전히 다른 장치들을 이어주는 추상화된 장치(abstract devices) 또는 파이프
- 하드웨어 장치마다 명령을 내리는 방식이 다르다. 하지만, 운영체제가 하드웨어에 해당 명령을 쉽게 전달할 수 있도롯 스트림을 제공한다.
- 예로, 모니터와 잇는  스트림을 이용해야 한다면 운영체제가 모니터에 맞는 명령어를 내림
- 다양한 스트림이 존재함
    1. `stdout` : 모니터에 대한 스트림
    2. `stdin` : 키보드에 대한 스트림
    3. `stderr` : 오류 메세지를 출력하는 스트림

<br>

### `FILE`

```c
typedef struct _iobuf
{
    char* _ptr // 파일포인터로, 파일의 현재 위치를 나타낸다.
    int _cnt; // 입력버퍼에서 사용할 수 있는 문자의 개수
    char* _base; // 메모리 상에 있는 파일 원형의 주소를 가리킨다.
    int _flag; // 파일 포인터가 파일의 끝에 오면 제 5bit가 1이 됨.
    int _file; // 파일 식별자
    int _charbuf; // 문자열 버퍼
    int _bufsiz; // 버퍼 크기
    char* _tmpfname; // 임시 파일 이름의 위치?
} FILE;

```

- `printf("%s\n"fp->_base);` 명령어를 실행시키면 파일에 출력되는 모든 내용을 볼 수 있음
- `_files`
    - 파일 식별자
    - stdin : 0, 입력버퍼
    - stdout : 1, 출력버퍼
    - stderr : 2, 에러버퍼
    - 나머지부터는 파일이 열어진 순서대로 3, 4, 5...가 할당된다.


## `fopen`

생성한 스트림을 가리키는 포인터를 리턴함

인자로 파일의 이름, 옵션을 전달함
- 그냥 파일이름을 전달하면 소스파일이 존재하는 동일 경로에서 해당 파일 이름을 탐색
    - 특정 폴더의 파일을 찾고 싶을 경우 해당 파일 경로를 전달하면 됨
- `"w"`
    - 파일 쓰기만 가능
    - 첫 번째 인자인 파일 이름이 존재하지 않는다면 아무 내용이 없는 파일을 새로 만듦
    - 동일한 이름의 파일이 존재한다면 그 내용을 전무 지워버림

어떤 이유로 인해 파일을 열지 못한 경우, `NULL`리턴
- 따라서 `NULL` 검사를 해야 한다.

## `fput`

파일에 기록하는 함수


인자
1. 파일에 기록할 문자열을 전달
2. 문자열을 전달할 스르림 포인터
    - 두 번째 문자열로 모니터 표준 출력 스트림인, `stdout`을 전달하면 모니터에 해당 문자열이 출력됨

## `fclose`

연결되었던 스트림을 닫아주는 함수

닫지 않는다면 계속 살아있게 되어, 프로그램 종료되기 전까지 해당 파일이 쓰기 살태로 남게 됨

> `stdout` 표준 출력 스트림을 닫게 되면 `printf`함수가 동작하지 않는다.


## `fgets`


```c
#include <stdio.h>
int main() {
  FILE *fp = fopen("a.txt", "r");
  char buf[20];  // 내용을 입력받을 곳
  if (fp == NULL) {
    printf("READ ERROR !! \n");
    return 0;
  }
  fgets(buf, 20, fp);
  printf("입력받는 내용 : %s \n", buf);
  fclose(fp);
  return 0;
}
```
첫번째 인자로 어디에 입력받을 지, 두번째 인자로 입력받을 바이트 수, 세번째 인자로 어떤 스트림을 통해 입력받을지 명시해 주면 됨

`scanf` 함수와 달리 입력받을 바이트를 제한할 수 있어서 오버플로우를 예방할 수 있는 안정성이 있다.


## `fgetc`

```c
#include <stdio.h>

int main() {
  FILE *fp = fopen("a.txt", "r");
  char c;

  while ((c = fgetc(fp)) != EOF) {
    printf("%c", c);
  }

  fclose(fp);
  return 0;
}
```

fp 에서 한 문자씩 읽어들어 옴

문자열 맨 마지막이 NULL 문자로 종료를 나타내는 것 처럼,파일의 맨 마지막에는 EOF(End Of File)을 나타내는 값인 -1 이 들어가 있음

## 파일 위치 지정자(Position indicator)

파일에서 입력을 받을 때 언제나 파일의 시작 부분에서 끝 부분으로 입력을 쭉 받아 나갔음

즉, 이전에 입력 받았던 데이터는 다시 입력 받지 않았다는 것

파일을 맨 처음 열었을 때 에는 파일 위치 지정자는 파일의 맨 첫부분을 가리키고 있음

`fgetc`로 한 문자씩 입력받으면 위치지정자는 한 칸씩 옮기며 다음 위치를 가리키고 있음

<br>

### `fseek`, 파일 위치 지정자 옮기기

```c
#include <stdio.h>
int main() {
  /* 현재 fp 에 abcdef 가 들어있는 상태*/
  FILE *fp = fopen("a.txt", "r");
  fgetc(fp);
  fgetc(fp);
  fgetc(fp);
  fgetc(fp);
  /* d 까지 입력받았으니 파일 위치지정자는 이제 e 를 가리키고 있다 */
  fseek(fp, 0, SEEK_SET);
  printf("다시 파일 처음에서 입력 받는다면 : %c \n", fgetc(fp));
  fclose(fp);
  return 0;
}
```

`fseek(fp, 0, SEEK_SET);`

- fp를 세 번째 인자로부터 두 번째 인자만큼 떨어진 곳으로 되돌림
- `SEEK_SET` : 파일의 맨 처음을 일컫는 매크로 상수
- `SEEK_CUR` : 현재의 위치를 표시하는 매크로 상수
- `SEEK_END` : 파일의 맨 끝을 표시하는 매크로 상수

<br>

### 파일 수정

```c
#include <stdio.h>
int main(){
    FILE *fp = fopen("a.txt", "w");
    fputs("Psi is an excellent C programmer", fp);
    fseek(fp, 0, SEEK_SET);
    fputs("is Psi", fp);
    fclose(fp);
    return 0;
}
// is Psi an excellent C programmer
```

- 파일 앞에 내용이 끼워져 들어가는 것이 아니라 이전의 내용에 덮어쓰기 하면서 기록
