# 컴파일, 링킹, 헤더파일,Makefile

## 컴파일

실행 파일을 만들기 위해 컴파일을 진행한다.

컴파일러가 소스 코드 전체를 어셈블리어로 변환해준다.

이 때, 목적코드라 불리는 .o 파일이 생성된다.

## 링킹

이 후 각기 다른 파일에 위치한 소스코드들을 한데 엮어서 하나의 실행 파일로 만드는 과정이다.

실행 파일은 목적 파일, .o파일을 통해 만든 바이너리 파일이다.

이 과정을 통해 특정한 소스 파일에 있는 함수들이 어디에 있는지 찾느 과정을 거친다.

## 헤더파일

파일을 여러 개로 나눠야 할 때 전처리기 `#include`를 이용하여 파일별로 연결시켜준다.

전처리기는 컴파일 전에 실행되어, 지칭하는 파일의 내용을 복사하여 붙여넣는다.

보통 해더파일의 이름은 헤더파일이 포함하고 있는 함수의 소스코드 이름을 따른다.


### 파일 내에 헤더파일 선언

`#include <~.h>` : 컴파일러에서 기본으로 지원하는 헤더파일의 경우
`#include "~.h"` : 사용자가 직접 제작한 헤더 파일


## Makefile

반복되는 컴파일 작업을 생략할 수 있다.

수정된 파일만 컴파일할 수 있다.

대규모 프로젝트, 공도 프로젝트에서 반드시 필요하다.


## 실습

![image](https://github.com/WonilLee211/TIL/assets/109330610/010f10fb-3e7c-458f-b1a6-ac5d3100c45f)

```
.
├── headerfile
│   └── str.h
├── resourcefile
└── sourcefile
    ├── app.out
    ├── str.c
    ├── test.c
```

위와 같은 폴더 구조로 파일을 생성했다.


```c
// test.c
#include <stdio.h>
#include "str.h"
int main() {
  char str1[20];
  char str2[20];

  scanf("%s", str1);
  scanf("%s", str2);

  if (compare(str1, str2)) {
    printf("%s 와 %s 는 같은 문장 입니다. \n", str1, str2);
  } else {
    printf("%s 와 %s 는 다른 문장 입니다. \n", str1, str2);
  }
  return 0;
}

//str.c
#include "str.h"
char compare(char *str1, char *str2) {
  while (*str1) {
    if (*str1 != *str2) {
      return 0;
    }

    str1++;
    str2++;
  }

  if (*str2 == '\0') return 1;

  return 0;
}
// str.h
char compare(char *str1, char *str2);
```

위 코드들을 gcc를 이용하여 링킹이 된 실행파일을 만들어 보고자 한다.

1. 목적파일 생성
  - `gcc -c test.c str.c -I ../headerfile`
  - -c 옵션은 소스파일을 목적파일로 생성한다.
2. 링킹을 통한 바이너리 파일을 생성한다.
  - `gcc -o app.out test.o str.o -I ../headerfile`

```shell
.
├── headerfile
│   └── str.h
├── resourcefile
└── sourcefile
    ├── app.out
    ├── str.c
    ├── str.o
    ├── test.c
    └── test.o
```

3. 실행
  - `./app.out`


## Makefile 활용한 컴파일

### Makefile 구조

- Target : 만들려는 파일
- DEPENDENCY : 필요한 재료
- command : shell 커멘드에 명령을 준다(Tab)으로 구분

```shell
// Makefile
app.out : test.o str.o
      gcc -o app.out test.o str.o -I ../headerfile
test.o :
      gcc -c test.c  -I ../headerfile
str.o :
      gcc -c str.c  -I ../headerfile

// shell
make
gcc -c test.c  -I ../headerfile
gcc -c str.c  -I ../headerfile
gcc -o app.out test.o str.o -I ../headerfile
```

- 위 처럼 `app.out` 파일을 생성하는 명령어를 마지막에 실행하기 위해 첫 부분에 작성하거나 all 옵션을 사용한다.

```shell
// Makefile
all : app.out

test.o :
      gcc -c test.c  -I ../headerfile

str.o :
      gcc -c str.c  -I ../headerfile

app.out : test.o str.o
      gcc -o app.out test.o str.o -I ../headerfile
```

- 아래와 같이, 컴파일 명령을 환경변수화 시켜서 컴파일 명령, 바이너리 파일 이름을 변수화할 수 있다.
- 변경사항이 발생하면 환경변수 부분의 값만 변경하면 된다.

```shell
CC = gcc
TARGET = app.out
// 오브젝트 파일, 공통적으로 쓰는 Makefile의 내부 변수
OBJS = test.o str.o

all : $(TARGET)

$(TARGET) : $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)
    
test.o : 
	$(CC) -c test.c 
    
str.o :
	$(CC) -c str.c
```

아래와 같이, shell에서 지원하는 단축 표현을 활용할 수 있다.

- $@ : $(TARGET) 
- $^ : $(OBJS)
- $< : .c 소스파일
- .c.o : Makefile이 위치한 공간에 있는 .c 파일을 .o 오브젝트로 바꿔준다. .o을 Target으로 잡아준다.


```shell
CC = gcc
H = ../headerfile
TARGET = app.out
// 오브젝트 파일, 공통적으로 쓰는 Makefile의 내부 변수
OBJS = test.o str.o

all : $(TARGET)
$(TARGET) : $(OBJS)
        $(CC) -o $@ $^ -I $(H)
.c.o :
        $(CC) -c -o $@ $< -I $(H)
```

아래와 같이, CFLAGS, LDFLAGS라는 Makefile을 활용할 수 있다.

- CFLAGS : 컴파일 시 옵션을 줄 수 있다.
- LDFLAGS : 링크할 때 옵션(라이브러리)를 줄 수 있다

```shell
// Makefile
CC = gcc
H = ../headerfile
TARGET = app.out
OBJS = test.o str.o

CFLAGS = -Wall
LDFLAGS = -lc

all : $(TARGET)
    
$(TARGET) : $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^ -I $(H)
    
.c.o :
	$(CC) $(CFLAGS) -c -o $@ $< -I $(H)
    
clean : 
	rm -f $(OBJS) $@
```


Makefile을 통해 수정된 파일만 컴파일해서 바이너리파일을 다시 만드는 기능도 누릴 수 있다.

```shell
make
>> gcc -Wall -c -o test.o test.c -I ../headerfile
>> gcc -lc -o app.out test.o str.o -I ../headerfile

make clean
>> rm -f test.o str.o clean
```

