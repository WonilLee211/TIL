# lldb 사용법

작성한 코드가 어떻게 돌아가는지, 어디에서 문제가 발생하는지, 알 수 있는 방법

## lldb

Low-Level Debugger의 약자로,

LLVM의 디버거 컴포넌트를 개발하는 애플의 서브프로젝트

Xcode의 기본 디버거로 내장되어 있음

로우레벨 컨트롤이 가능한 모듈로 이루어져 있으며,

기계어에 가까운 영역까지 사용자가 볼 수 있도록 지원함


## 사용법

### 컴파일 시, 옵션 주기 (`-g`)

```shell
gcc [파일 이름] -g
```

- 디버거를 사용할 수 있도록 디버깅 정보를 생성하는 옵션

### lldb 디버거 실행하기

```shell
lldb [executable file name]
```

### 프로그램 실행하기 `run, r`

- breakpoint없이 바로 실행됨

### breakpoint걸기 `b [breakpoint]`

- `b main` : main함수에 들어가자마자 break
- `b 10` : 열 번째 줄에서 멈추게 됨
- 프로세스 아이디와 thread, stop reason이 표시됨
- 현재 실행된 지점을 화살표로 보여줌

### 다음 줄 실행하기 `next, n`

- return key 를 입력하면 이전에 입력한 명령어를 그대로 실행함
- 한 번 n을 입력 후 enter를 치면 된다.


### 함수 안으로 들어가기 `step, s`

- 함수 내에 들어감

### 변수 값 보기 `print [variable name], p [variable name]`

- 보고 싶은 변수 이름을 프린트함

### 변수 값 띄워놓기 `display [variable name]`

- 다음 코드를 실행할 때마다 설정한 변수값이 프린트된다.


### breakpoint설정하고 건너뛰어가기 `c`

- breakpoint를 설정해주고 설정해준 breakpoint로 건너뛰어가는 명령

### reference

[LLDB Tutorial](https://lldb.llvm.org/use/tutorial.html)


