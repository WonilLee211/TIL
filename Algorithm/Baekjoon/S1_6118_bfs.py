import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited = {i:0 for i in range(1, n + 1)}
    visited[start] = 1

    while q:
        next = q.popleft()

        for node in farms[next]:
            if not visited[node]:
                q.append(node)
                visited[node] = visited[next] + 1

    max_v = max(visited.values())
    min_k = n
    cnt = 0
    for k, v in visited.items():
        if v == max_v:
            cnt += 1
            if k < min_k:
                min_k = k
        
    return [min_k, max_v-1, cnt]

n, m = map(int, input().split())

farms = {i:[] for i in range(1, n + 1)}

for _ in range(m):
    f1, f2 = map(int, input().split())
    farms[f1].append(f2)
    farms[f2].append(f1)

print(*bfs(1))