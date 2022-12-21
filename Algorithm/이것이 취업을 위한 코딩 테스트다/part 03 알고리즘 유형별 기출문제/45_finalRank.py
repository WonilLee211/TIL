import sys
sys.stdin = open('input.txt')

'''
작년순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어질 때
올해 순위

T : 테스트 케이스 수, t <= 100
n : 팀 수, 2 <= n <= 500
작년 등수 별 팀 번호 : n개 정수
m : 상대적인 등수가 바뀐 쌍 수
a, b : 상대 등수가 바뀐 두 팀 번호 m개 줄. 같은 쌍이 여러번 발표된느 경우는 없음

출력
한줄에 올해의 등수 1등팀부터 순서대로 출력
확실한 순위를 찾을 수 없다면 ? 출력
데이터에 일관성이 없어서 순위를 정할 수 없는 경우 IMPOSSIBLE

논리
1. 정해진 우선순위에 맞게 전체 팀의 순서를 나열해야 한다. : 위상 정렬
2. 팀간의 순위정보를 그래프 정보로 표현한 뒤 위상정렬을 이용해 해결
3. 작년 순위 정보 ->  자기보다 낮은 등수를 가진 팀을 가리키도록 방향 그래프를 만듬
    - 진입차수의 크기가 크면 자기보다 순위가 낮아짐
4. 특이사항
    1. 사이클이 발생하는 경우 : n번 돌기 전에 q가 비면 사이클이 발생했다는 의미
    2. 위상 정렬의 결과가 1개가 아닌 경우 : q의 원소가 2개 이상인 경우
    >> 알고리즘 interation 과정마다 q 원소 개수를 확인하는 코드 추가
5. 위상 정렬을 통한 결과 출력

'''

import sys
from collections import deque

input = sys.stdin.readline


for tc in range(int(input())):

    n = int(input())            # 노드의 개수 입력 받기
    indegree = [0] * (n + 1)    # 모든 노드에 대한 진입차수 초기화
    graph = [[False] * (n + 1) for i in range(n + 1)] # 각 노드에 연결된 간선 정보를 담을 인접 행렬 초기화

    data = list(map(int, input().split())) # 작년 순위 정보

    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음시작할때 진입차수가 0인 노드를 q에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    isOne = True # 위상 정렬 결과가 오직 하나 인지 여부
    cycle = False # 그래프 내 사이클이 존재하는 지 여부

    # 정확히 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break

        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            isOne = False
            break

        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now) # 결과 저장

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 q에 담기
                if indegree[j] == 0:
                    q.append(j)


    if cycle:                   # 사이클이 발생하는 경우(일관성이 없는 경우)
        print("IMPOSSIBLE")
    elif not isOne:             # 결과가 여러 개인 경우
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()