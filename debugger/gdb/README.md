# gdb 사용법

주요 명령어 약어

- `i : info`
- `p : print`
- `b : break`
- `d : delete`
- `s : step`
- `c : continue`
- `n : next`
- `fin : finish`
- `t, thr : thread`
- `bt : backtrace`

실행 중인 프로세스에 붙이기

- > gdb -p <PID>

현재 프로세스의 thread 목록 보기

- > **i**nfo **thr**ead

N번 thread로 switch

- > **thr**ead [N]

모든 thread에 CMD를 수행

- > **thr**ead apply all [CMD]
- ex) 모든 thread의 callstack 동시에 보기 : (gdb) thr app all bt

EXP 값을 출력

- > **p**rint [EXP]

stop할 때마다 자동으로 EXP값을 출력

- > **dis**play [EXP]

display로 설정된 expression을 출력

- > **i**nfo **dis**play

EXP값이 변할 때 break 설정

- > watch [EXP]

break 위치 설정

- > **b**reak [PROBE_MODIFIER][LOCATION][thread THREADNUM][if CONDITION]
- ex) 현재 위치에 thread 10번만 break 설정 : > (gdb) b thread 10
- ex) a.c파일의 100라인에 모든 thread break 설정 : > (gdb) b a.c:10
- ex) 현재 위치에 variable a값이 10일 때만 break 설정 : > (gdb) b if a == 10


설정된 breakpoint 삭제

- > **i**nfo **b**reakpoint

breakpoint 삭제

- > **d**elect [N]
- N 안쓰면 all

N번 breakpoint 잠시 disable

- > disable [N]
- N 안쓰면 all


N번 breakpoint 다시 enable

- > enable [N]
- N 안쓰면 all

현재 function의 argument값 출력

- > **i**nfo args

현재 function의 local variable 출력

- > info variables

n 개의 statement를 수행하고 stop

- > **n**ext [N]
- N 안쓰면 1

breakpoint에 걸리는 (N - 1)개를 skip하고 N번째 breakpoint에서 멈춤

- > **c**ontinue [N]
- N 안쓰면 1


next와 동작이 비슷하나, statement 중 함수가 있으면 해당 함수 안으로 계속 들어감

- > **s**tep [N]
- N 안쓰면 1

화면 레이아웃 설정 및 변경

- > layout [src|asm|split|regs]
- `src` : 디버깅 중인 소스코드와 command 창  표시
- `asm` : 디버깅 중인 프로그램의 어셈블리 코드와 command 창 표시
- `split`: 소스코드와 어셈플리코드 분할하여 command 창 표시
- `regs` : CPU 레지스터의 상태 및 값과 command 창 표시

현재 함수 끝까지 수행 후 멈춤
- > **fin**ish

stop된 위치에서 함수를 호출한 상위/하위 함수로 이동

- > up/down

긴 문자열 출력

1. > set print element 0 (default 200)
2. > p printf("%s\n", str)
3. > x/300sb

16진수 출력

- > print /x 1234

2진수 출력

- > print /t 1234
