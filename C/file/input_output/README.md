# 파일 입출력

- 파일 위치 지정자(File Position Indicator)에 대한 이해
- `fseek` 다루기
- `fopen`에서 `"r", "w+", "a", "a+"` 형태 에 대해 배우고, 쓰기/ 읽기 전환 시 문제점에 대해 알기
- `fprintf`함수와 `fscanf`함수를 사용하기
- 도서 관리 프로그램에 입출력 처리 적용하기

## 파일 위치 지정자(File Position Indicator)

스트림의 기본 모토가 *순차적으로 입력받는다*이다.

이를 가능하게 해주는 것이 **파일 위치 지정자**이다.

```c
// 텍스트파일에서 문자를 하나씩 입력받는다.
#include <stdio.h>
int main(){
    FILE *fp = fopen("some_data.txt", "r");
    char c;

    if (fp == NULL){
        printf("file open error ! \n");
        return 0;
    }

    while ((c = fgetc(fp)) != EOF) {
        printf("%c", c);
    }
    return 0;
}
// There is some data in this FILE!!!!
```

- 위 코드처럼 `fgetc` 함수를 실행시킬 때마다 파일 위치지정자가 다음 글자를 가리키며 모든 데이터가 출력됨을 볼 수 있다.

## `fseek`

`int fseek(FILE* stream, long int offset, int origin);`

- `stream` : 우리가 파일 위치 지시자를 옮기고 싶은 스트림의 포인터
- `offset` : 얼마만큼 옮길지에 대한 정보
    - `+n` : 오른쪽으로 n만큼 이동
    - `+n` : 왼쪽으로 n만큼 이동
- `origin`: 어디서 부터 옮길지에 대한 정보
    - `SEEK_SET` : 파일의 맨 처음을 일컫는 매크로 상수
    - `SEEK_CUR` : 현재의 위치를 표시하는 매크로 상수
    - `SEEK_END` : 파일의 맨 끝을 표시하는 매크로 상수

```c
#include <stdio.h>
int main(){
    FILE *fp = fopen("some_data.txt", "r");
    char data[10];
    char c;

    if (fp == NULL){
        printf("file open error ! \n");
        return 0;
    }
    fgets(data, 5, fp);
    printf("입력 받은 데이터 : %s \n", data);

    c = fgetc(fp);
    printf("그 다음에 입력 받은 문자 : %c \n", c);

    fseek(fp, -1, SEEK_END);
    printf("그렇다면 무슨 문자가? : %c \n", c);

    return 0;
}
// 입력 받은 데이터 : Ther
// 그 다음에 입력 받은 문자 : e
// 그렇다면 무슨 문자가? : !
```
- `fgets`에서 5을 줬지만 4자리만 읽은 이유는 문자열을 구성할 때 마지막에 `\n`을 구성하기 때문임

## 파일 동시에 쓰기 

`r+`

- 읽기 및 쓰기형식으로 열기
- 파일이 존재하지 않는다면 열지를 않겠다는 의미
- 파일이 존재한다면 파일 내용을 지우지 않음

`w+`

- 읽기 및 쓰기형식으로 열기
- 파일이 존재하지 않는다면 새로 생성해서 열기
- 파일이 존재한다면 파일 내용을 지우고 열기



<br>

> ### 주의사항
> 스트림 작업에서 읽기/쓰기를 전환할 때, `fflush`, `fseek`, or `rewind`와 같은 함수를 호출하여 파일 위치 지정자를 다시 설정해줘야 한다.

```c
#include <stdio.h>
int main(){
    FILE *fp = fopen("some_data.txt", "r+");
    char c;

    if (fp == NULL) {
        printf("파일 열기를 실패하였습니다! \n");
        return 0;
    }


    while ((c = fgetc(fp)) != EOF) {
        /* c 가 대문자일 경우 */
        if (65 <= c && c <= 90) {
            /* 한 칸 뒤로 가서*/
            fseek(fp, -1, SEEK_CUR);
            /* 소문자로 바뀐 c 를 출력한다*/
            fputc(c + 32, fp);
            /*
            쓰기 - 읽기 모드 전환을 위해서는 무조건
            fseek 함수와 같은 파일 위치 지정자 설정 함수들을
            호출해야 한다.
            */
            fseek(fp, 0, SEEK_CUR);
        }
        /* c 가 소문자일 경우*/
        else if (97 <= c && c <= 122) {
        fseek(fp, -1, SEEK_CUR);
        fputc(c - 32, fp);
        fseek(fp, 0, SEEK_CUR);
        }
    }
    fclose(fp);

    return 0;
}
```


## `fopen`함수의 기타 인자 사용

`"a"`

- 덧붙이기 형식
- 파일의 맨 끝부분부터 내용이 쓰여지고 기존 데이터를 전혀 건들지 않음
- 기존 데이터를 보호
- 파일 위치 지정자를 이동시켜 봐도 기존 파일의 끝 부분 위치에서 쓸 수 있음

```c
/* fopen 의 'append' 기능 사용*/
#include <stdio.h>
int main() {
  FILE *fp = fopen("some_data.txt", "a");
  char c;
  if (fp == NULL) {
    printf("파일 열기를 실패하였습니다! \n");
    return 0;
  }
  /* 아래 내용이 파일 뒤에 덧붙여진다.*/
  fputs("IS ADDED HAHAHAHA", fp);
  fclose(fp);
}
// There is some data in this FILE!!!!IS ADDED HAHAHAHA
```
## `fscanf` 사용하기

`int fcanf(FILE *stream, const char *format, target);`

- 파일에서 데이터를 읽어와서 형식화된 입력을 처리하는 함수
- stream : 데이터를 읽어올 파일 스트림
- format : 입력 데이터의 형식을 지정하는 문자열
- target : 읽어온 데이터를 형식에 따라 변수에 저장
- return : 더 이상 받아올 문자열이 없는 경우 EOF 리턴
```c
#include <stdio.h>
int main(){
    FILE *fp = fopen("some_data.txt", "r");
    char data[100];
    if (fp == NULL) {
        printf("파일 열기 오류! \n");
        return 0;
    }

    printf("---- 입력 받은 단어들 ---- \n");
    while (fscanf(fp, "%s", data) != EOF) {
        printf("%s \n", data);
    }
    fclose(fp);

    return 0;
}
```
- `scanf` 가 `stdin` 에서만 입력을 받고 `fscanf` 는 임의의 스트림에서도 입력을 받을 수 있는 좀더 일반화 된 함수
-  띄어쓰기나 탭 문자들도 모두 string terminator로 인식
- 더이상 새로운 데이터를 입력을 받을 수 없을 경우에는 EOF 를 리턴

<br>

### prac. 파일에서 'this' 를 'that' 으로 바꾸기

```c
#include <stdio.h>
#include <string.h>

int main(){
    FILE *fp = fopen("some_data.txt", "r+");
    char data[100];

    if (fp == NULL) return 0;

    while ((fscanf(fp, "%s", data)) != EOF){
        if (strcmp(data, "this") == 0){
            fseek(fp, -(long)strlen(data), SEEK_CUR);
            fputs("data", fp);

            fflush(fp);
        }
    }
    fclose(fp);

    return 0;
}
// this is a man and this is a woman, and that is a boy
// that is a man and that is a woman, and that is a boy
```
