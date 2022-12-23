import sys
sys.stdin = open('input.txt')

'''
단방향 도로
최단거리가 k인 도시 번호 출력



논리
-  bfs
'''

import sys, collections
deque = collections.deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
adjList = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adjList[a].append(b)

ans = []
q = deque()

q.append(x)
visited = [0] * (n + 1)
distance = [0] * (n + 1)
visited[x] = 1

while q:
    now = q.popleft()



    for city in adjList[now]:

        if visited[city] != 0:
            continue

        visited[city] = 1
        distance[city] = distance[now] + 1
        q.append(city)

        if distance[city] == k:
            ans.append(city)

if len(ans) == 0:
    print(-1)
else:
    for x in sorted(ans):
        print(x)

