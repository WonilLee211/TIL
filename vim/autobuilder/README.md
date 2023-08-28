# autotools를 이용한 프로젝트 빌드하기

## 폴더 구조

```shell
./rootDir
└── src
    └── main.c

# main.c

#include <stdio.h>

int main(int argc, char *argv[])
{
       printf("Hello autotools\n");

       return 0;
}

```
## autotools 구성하기

root Makefile.am 파일 작성

- 가장 상위 디렉토리의 Makefile.amm을 참조하여 SUBDIRS를 참조하여 진행한다.

```shell
rootDir
├── Makefile.am
└── src
    └── main.c

SUBDIRSS = src
```

subdir 폴더 내에 파일 작성

```shell
rootDir
├── Makefile.am
└── src
    ├── Makefile.am <-- 파일 작성
    └── main.c


bin_PROGRAMS = amhello

amhello_SOURCES = main.c

```

<br>

autoscan - confgure.scan 탬플릿을 생성

- MAC 환경에서 `brew install autoconf`
- `rootDir`에서 `autoscan` 실행
- 생성된 configure.scan -> configure.ac로 수정 후 파일 아래와 같이 수정

```am
#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([rootDir], [1.0], [xxx@gmail.com]) <- 패키지이름, 버전, 메일을 수정
AC_CONFIG_SRCDIR([src/main.c])
AC_CONFIG_HEADERS([config.h])

AM_INIT_AUTOMAKE([foreign -Wall -Werror])        <- automake를 사용할 수 있도록 추가

# Checks for programs.
AC_PROG_CC

# Checks for libraries.

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([Makefile
                 src/Makefile])
AC_OUTPUT
```

<br>

autoconf 실행

- `autoreconf -i`
    - configure.ac파일을 입력으로 사용하여 configure에 필요한 파일들을 생성해줌
    - -i 옵션은 보조적 파일들을 생성

```
rootDir
├── Makefile
├── Makefile.am
├── Makefile.in
├── aclocal.m4
├── autom4te.cache
│   ├── output.0
│   ├── output.1
│   ├── output.2
│   ├── output.3
│   ├── output.4
│   ├── output.5
│   ├── output.6
│   ├── requests
│   ├── traces.0
│   ├── traces.1
│   ├── traces.2
│   ├── traces.3
│   ├── traces.4
│   ├── traces.5
│   └── traces.6
├── autoscan.log
├── compile
├── config.h
├── config.h.in
├── config.log
├── config.status
├── configure
├── configure.ac
├── configure.scan
├── configure~
├── depcomp
├── install-sh
├── missing
├── src
│   ├── Makefile
│   ├── Makefile.am
│   ├── Makefile.in
│   ├── main.c
│   ├── main.o
│   └── rootDir
└── stamp-h1

```

<br>

compile & build & execute

- rootDir에서 `./configure`
- `make`
- `./src/rootDir`


