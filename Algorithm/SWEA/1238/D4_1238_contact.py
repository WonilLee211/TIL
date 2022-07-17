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