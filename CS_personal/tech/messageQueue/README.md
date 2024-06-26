# 생성과 조회를 책임지는 알림 서버

- 목적 : 안정적이고 빠른 서비스 제공

<h3> 알림 생성에 부하가 걸린다면?</h3>

1. CPU 사용률이 100%를 유지될 경우
2. 시스템 스레드가 고갈됐을 경우

> 전체 기능에 장애 전파됨
> 알림 생성과 조회기능 전반에 장애가 전파되게 됩니다.



<h3>대책 1. 생성 / 조회 서버 분리</h3>

<h4>장점</h4> 

-  조회서버에 대한 장애 전파 방지

<h4>단점</h4> 

- 관리포인트가 증가하여 유지보수성 악화
- **생성 서버의 부하를 막지 못함. 근본대책이 아니다.**
    - 알림 서버의 쓰레드 고갈 발생 가능성
    - 수십밀리세컨드의 응답 시간이 몇 초로 증가할 수 있음
    - 이체 알림일 경우 부수적 기능인 알림 때문에 이체가 안되는 상황이 발생할 수 있음


<h4>그러면 비정상적인 지연 응답에 대해서 대책이 뭘까?</h4>

- 짧은 Timeout 설정 : 비정상적인 지연응답에 대해서 끊어 내어 자신의 자원을 지켜내야 함
- 비동기 호출 : 가용한 공간 내에서 알림 생성을 `비동기로 호춯`하여 주요 비지니스로부터 분리시켜야 함

> 하지만 연계시스템이 늘어남에 따라 모든 연계시스템이 이러한 대비책을 세워야하기 때문에 서버를 신뢰할 수 없는 상황

<h3>대책 2. 생성 서버 내부 비동기 알림 생성</h3>

1. 요청을 수신
2. 비동기 쓰레드 풀에서 알림 생성
3. 응답

<h4>비동기 알림 생성을 통해 알림 요청과 생성에 경계층 생성</h4>

> 알림 생성의 장애가 알림 요청에 전파되지 않는, 신뢰성있는 서버의 역할을 할 수 있는 것임 !
> 비동기를 통해 빠른 응답시간과 장애 격리에 대한 이점을 얻을 수 있는 것임 !

<h4>여전한 단점 1 : 알림 생성 여부에 대해 알 수 없음</h4>

<h4>여전한 단점 2 : 실시간 알림 생성이 아닌, 지연 발생 가능성</h4>

 - 알림의 특성상 어느정도의 지연은 감안할 수 있음

<h4>여전한 단점 3 : 생성 서버의 다운에 의해 요청 데이터 유실</h4>

- 운영 신뢰성을 높이려는 비동기 방식이 역으로 데이터 신뢰성을 보장할 수 없는 상황
- 이에 따라 알림이 생성됐는지 지속 감시하거나 유실 시 재 요청하는 과정이 필요해짐


<h3>대책 3. Message Queue 도입</h3>

<h4>Message Queue</h4>

1. 프로듀서가 q에 알림 생성 요청을 날림
2. q는 요청을 수신하여 consumer에게 전달함

<h4>Message Queue 도입한 알림 생성</h4>

1. 연계시스템이 생성 서버에 요청을 보냄
2. 서버는 Queue에 요청을 담음
3. Queue는 Consumer에게 전송
4. 서버는 알림 생성 서비스 로직을 거친 후 DB에 저장
5. consumer는 작업 완료를 의미하는 ack를 Queue에 전송


<h4>Consumer에 장애가 발생하면?</h4>

- 설정에 따라 재처리 가능

<h4>장점</h4>

- 메세지 큐는 메모리외에도 디스크에도 저장하기 때문에 안전함

<br>
