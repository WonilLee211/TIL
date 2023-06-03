# NonBlocking I/O

## 1. I/O의 종류

1. network(socket)
2. file
3. pipe : 프로세스간 통신
4. device


### socket

- 소켓은 장치 파일을 추상화한 인터페이스로, 네트워크(컴퓨터 to 컴퓨터)에서 데이터 통신에 사용된다.
- 백엔드 서버는 네트워크 상의 요청자들과 각각 소켓을 열고 통신을 한다.

## OS 레벨에서의 Block I/O와 non-block I/O

<h3>block I/O</h3>

I/O 작업을 요청한 프로세스, 스레드는 요청이 완료될 때까지 블락되는 방식 


![threadKenel](../image/threadKenel.PNG)

1. 스레드에서 작업 코드 실행
2. read blocking system call 호출/ thread blocked
3. kernel 모드 전환
4. kernel에서 initiate read I/O 실행. 관련 디바이스 실행
5. 해당 디바이스에서 읽을 준비 알림
6. read response를 가지고 kernel에서 thread로 데이터 이동



<hr>

<h3>non-block I/O</h3>

프로세스, 스레드를 블락시키지 않고 요청에 대한 현재 상태를 즉시 리턴하며, 프로세스나 스레드는 다른 작업을 진행할 수 있음

![sockerIO](../image/nonblockingIo.PNG)

1. 스레드에서 read nonblock system call 실행 - 커널모드 전환
2. 커널에서 read I/O 작업 실행 / 리눅스 기준 -1(with error code, EAGAIN or EWOULDBLOCK) 반환
3. 스레드는 다른 코드 실행
4. 커널에서 read response 수신하면 데이터 준비
5. 스레드에서 read nonblocking I/O system call 다시 실행
6. data 수신

<hr>


![sockerIO](../image/socketIO.PNG)

## socket에서 block I/O, non block I/O

<h3>block I/O</h3>

1. socket에는 send buffer와 recieve buffer가 있음
2. socket S에서 socket A로 데이터 전송 시도
3. socket A에서 recieve buffer가 비어있을 경우 read() 함수 실행한 스레드 블록 당함
4. socket S에서 send buffer가 가득 찼을 경우 write 시스템 콜은 블락 상태

<h3>non-block I/O</h3>

1. socket에는 send buffer와 recieve buffer가 있음
2. socket S에서 socket A로 데이터 전송 시도
3. socket A에서 read() 함수 실행한 스레드는 다른 작업 수행 가능
4. socket S에서 send buffer가 가득 찼을 경우 write 시스템 콜은 다른 작업 실행 가능


## non block I/O 결과 처리 방식

`non block I/O 이슈` : 작업 완료를 어떻게 확인할 것인가?

<h3>1. 완료됐는지 반복적으로 확인</h3>

- 내가 읽으려는 데이터가 준비됐을 때까지 반복 확인

### 단점 

1. 완료된 시간과 완료를 확인한 시간 사이의 갭으로 인해 처리 속도가 느려질 수 있음
2. 반복 확인에 의한 `cpu 낭비 발생`

<br>

<h3>2. I/O multiplexing(다중 입출력) 사용</h3>

하나의 스레드에서 여러 개의 I/O 작업을 동시에 처리하기 위한 기법

하나의 스레드가 여러 개의 파일 디스크립터를 동시에 관찰하고, 그 중에서 I/O 이벤트가 발생한 파일 디스크립터를 식별하여 처리하는 방식

멀티 프로세스의 단점을 보완하여 프로세스간 통신과 동기화 오버헤드을 피하고 작은 리소스 소모할 수 있음

<br>

![multiplexingIO](../image/multiplexingIO.PNG)

1. IO multiplexing system call 실행.
    -  예를 들어 두개의 소켓에 대해서 blocking  or non blocking read하려고 하는데 데이터가 준비되면 알려달라는 방식
2. thread는 블락이 될 수도, 다른 작업이 실행되도록 하도록 할 수 있음
3. 데이터가 있다는 걸 커널에서 스레드로 알려줌
4. 순차적으로 소켓별로 읽어나가도록 처리

<br>

### I/O multiplexing 종류

1. select : 저성능으로 잘 사용하지 않음. 블록킹 함수
2. poll : 저성능으로 잘 사용하지 않음. select와 달리 파일디스크립터 집합의 크기 제한이 없음
3. epoll : 리눅스에서 사용
4. kqueue : 맥OS 사용
5. IOCP(I/O completion port) : 윈도우, 솔라리스에서 사용

<br>

<h3>Linux epoll</h3>

- 이벤트 기반 (event-driven)으로 동작합니다.
- 사용자 공간 (user space)에서 이벤트를 처리합니다.
- 대상 파일 디스크립터의 수에 따라서 성능이 좋습니다.
- select나 poll과 달리 대상 파일 디스크립터의 수에 따라서 성능이 크게 차이가 나며, 이벤트 기반으로 동작하기 때문에 불필요한 파일 디스크립터를 모니터링하지 않습니다.
- 그래서 네트워크 통신에 많이 사용합니다.


### 동작원리

1. epoll_create 시스템 콜을 사용하여 epoll 인스턴스를 생성합니다. 이 인스턴스는 epoll에서 관찰할 파일 디스크립터들을 저장합니다.
2. epoll_ctl 시스템 콜을 사용하여 epoll 인스턴스에 파일 디스크립터를 등록하고, 관찰할 이벤트를 설정합니다. 이때, 등록된 파일 디스크립터와 관련된 이벤트가 발생하면 커널은 epoll 인스턴스에서 이벤트를 저장합니다.
3. epoll_wait 시스템 콜을 사용하여 epoll 인스턴스에서 발생한 이벤트를 읽어들입니다. 이때, 이벤트가 발생한 파일 디스크립터와 해당 이벤트를 구분할 수 있는 사용자 지정 데이터가 함께 반환됩니다.
4. 사용자 공간에서 epoll_wait 시스템 콜의 반환값을 처리합니다. 이때, 발생한 이벤트와 관련된 작업을 수행합니다.

<h3>3. callback/signal 사용</h3>

- 많이 사용하지 않음

![callback](../image/callbackSignal.PNG)

1. aio_read non block system call 호출/ 스레드 비동기 작업
2. 커널 모드에서 read IO 실행
3. read 데이터 준비 완료
4. 콜백 및 시그널 형태로 반환됨


<h3>3.1 callback/signal 종류</h3>

1. POSIX AIO
2.  LINUX AIO


<h3>4. io_uring</h3>

- 파일 IO에 효율적


<h3>핵심</h3>

non block IO를 통해 IO 요청 완료 전에도 다른 일을 할 수 있다는 것

## Blocking, Non-blocking, Sync, Async

![asyncNonblock](../image/asyncnonblock.png)

<h3>블로킹 Blocking</h3>

A 함수가 B 함수를 호출 할 때, B 함수가 자신의 작업이 종료되기 전까지 A 함수에게 제어권을 돌려주지 않는 것

<h3>논블로킹 Non-blocking</h3>

A 함수가 B 함수를 호출 할 때, B 함수가 제어권을 바로 A 함수에게 넘겨주면서, A 함수가 다른 일을 할 수 있도록 하는 것.

<h3>동기 Synchronous</h3>
A 함수가 B 함수를 호출 할 때, B 함수의 결과를 A 함수가 처리하는 것.

<h3>비동기 Asynchronous</h3>

A 함수가 B 함수를 호출 할 때, B 함수의 결과를 B 함수가 처리하는 것. (callback)

<br>

![2](../image/2.PNG)

- 여기서 I/O multiplexing을 non blocking으로 생각하는 것이 더 옳다