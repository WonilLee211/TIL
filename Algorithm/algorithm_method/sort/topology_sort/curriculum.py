'''
동빈이는 온라인으로 컴퓨터공학 강의를 듣고 있다.
이때 각 온라인 강의는 선수 강의가 있을 수 있는데,
선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
예를 들어 '알고리즘' 강의의 선수 강의로 '자료구조'와 '컴퓨터 기초'가 존재한다면,
'자료구조'와 '컴퓨터 기초'를 모두 들은 이후에 '알고리즘' 강의를 들을 수 있다.
동빈이는 총 N개의 강의를 듣고자 한다.
모든 강의는 1번부터 N번까지의 번호를 가진다.
또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
예를 들어 N = 3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고,
1번과 2번 강의는 선수 강의가 없다고 가정하자.
그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자.
1번 강의 : 30시간
2번 강의 : 20 시간
3번 강의 : 40시간

동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때,
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.
'''
'''
첫째줄에 듣고자하는 강의의 수 1<= N <= 500
다음 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야하는 강의들의 번호가 자연수로 주어지며,
각 자연수는 공백으로 주어진다. 이때 강의 시간은 100,000 이하의 자연수
각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
import sys
sys.stdin = open('../../input.txt')
from collections import deque

# 노드 개수 입력
v = int(input())
# 모든 노드에 대한 집입차수는 0으로 초기화
indegree = [0 for i in range(v + 1)]
# 각 노드에 연결된 간선 정보 담기 위한 연결리스트
graph = [[] for i in range(v + 1)]
# 각 강의 시간 0으로 초기화
times = [0 for i in range(v + 1)]
# dp 저장
dp = [0 for i in range(v + 1)]

# 방향그래프 정보 받기
for i in range(1, v + 1):
    temp = list(map(int, input().split()))
    times[i] = temp[0]
    for j in temp[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

# 시작점 찾기
for i in range(1, v + 1):
    if indegree[i] == 0:
        start = i

# 위상정렬
q = deque()
q.append(start)
dp[start] = times[start]

while q:
    node = q.popleft()

    for c in graph[node]:
        indegree[c] -= 1

        if indegree[c] == 0:
            # 기존 위치의 시간값과 현재 구한 값 + 추가 시간 중 큰 값으로 저장
            dp[c] = max(dp[c], times[c] + dp[node])
            q.append(c)

print(*dp[1:])