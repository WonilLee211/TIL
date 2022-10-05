import sys
sys.stdin = open('input.txt')

# 위상정렬과 우선순위 큐 결합

import heapq as hq

n, m = map(int, input().split())
indegree = list(0 for _ in range(n + 1))
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

res = []
q = []

for i in range(1, n + 1):
    if indegree[i] == 0:
        hq.heappush(q, i)

while q:
    node = hq.heappop(q)
    res.append(node)

    for c in graph[node]:
        indegree[c] -= 1

        if indegree[c] == 0:
            hq.heappush(q, c)

print(*res)