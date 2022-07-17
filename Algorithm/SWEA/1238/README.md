# SWEA D4 1238 contact

## 문제
비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때, 가장 나중에 연락받게 되는 사람 중 번호가 가장 큰 사람 구하기
---
## 입력
- 첫번째 줄 : 데이터의 길이와 시작점
- 두번째 줄 : from, to, from, to 형태의 숫자열
    - from to 조합이 중복될 수 있다.
---
## 출력
- #testcase 답 형태
---
## 제약
- 한번 연락한 사람한테 또 연락하지 않음
---
## 알고리즘
1. 첫번째 줄 정보 저장
2. 두번째 줄 리스트에 저장
3. 딕셔너리(key:set) 형태로 저장
4. BFS와 재귀함수 활용
    1. 연락해야할 대상 시퀀스에서 하나씩 pop()
    2. 각각의 대상과 연결된 대상에 아직 연락하지 않았다면, next_queue로 저장
    3. next_queue가 남아있다면 MaxNum함수 다시호출
    4. answer를 함수에서 전역변수로 선언해서 전역에서 정보받도록 설정

```
from collections import deque

def MaxNum(start_q):
    global answer   # answer 전역변수 선언
    answer = max(start_q)

    next_queue = deque()    # 다음 연락해야 할 대상 저장

    while start_q: # 현재 연락할 사람없어질 때까지
        node = start_q.popleft()
        
        for ContactTo in phonebook[node]: # 연락할 대상에 대해서
            if not visited[ContactTo]:  # 방문한 적 없다면
                next_queue.append(ContactTo)
                visited[ContactTo] = 1

    if next_queue: # 연락할 관계가 남아있다면 함수 재호출
        MaxNum(next_queue)


for testcase in range(1,11):
    datalength, startkey = map(int, input().split())   # 입력값 저장
    data = list(map(int, input().split()))

    visited = list( 0 for _ in range(101) ) # 전화번호와 같은 인덱스에 방문 이력 저장할 리스트
    visited[startkey] = 1

    phonebook = {i:[] for i in range(1, 101)}   # 딕셔너리 형태로 연락관계 저장
    for i in range(0, datalength, 2):
        phonebook[data[i]].append(data[i+1])
    
    answer = 0
    q = deque()
    q.append(startkey)

    MaxNum(q)
    
    print(f"#{testcase} {answer}")
```