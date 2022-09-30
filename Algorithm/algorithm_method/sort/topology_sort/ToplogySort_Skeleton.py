import sys
sys.stdin = open('../../input.txt')
'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''

from collections import deque

# 노드의 개수와 간선의 개수 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0 for i in range(v + 1)]
# 모든 노드에 연결된 간선 정보를 담기 위한 연결리스트(그래프) 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1                    # 연결된 간선에 따라 진입차수 계산

# 위상 정렬 함수
def topology_sort():
    res = []                            # 수행 결과 저장 리스트
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 원소 꺼내기
        node = q.popleft()
        res.append(node)

        for c in graph[node]:
           indegree[c] -= 1             # 해당원소와 연결된 노드들의 진입차수에서 1 빼기

           if indegree[c] == 0:
               q.append(c)              # 진입차수가 0이 되는 노드를 큐에 삽입
    return res

res = topology_sort()

print(res)
# [1, 2, 5, 3, 6, 4, 7]