import sys
sys.stdin = open('input.txt')
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

from collections import deque

def bfs(i, j):
    global cnt
    for k in range(n + 2, 0, -1):
        visited = [[0] * n for i in range(n)]
        q = deque()
        q.append((i, j))
        visited[i][j] = 1

        k_cnt = 0
        while q:
            ni, nj = q.popleft()
            if data[ni][nj]:
                k_cnt += 1

            if visited[ni][nj] == k:
                continue

            for e in range(4):
                if 0 <= ni + di[e] < n and 0 <= nj + dj[e] < n and not visited[ni + di[e]][nj + dj[e]]:
                    q.append((ni + di[e], nj + dj[e]))
                    visited[ni + di[e]][nj + dj[e]] = visited[ni][nj] + 1

        if k_cnt*m >= k**2 + (k-1)**2:
            if k_cnt > cnt:
                cnt = k_cnt

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())  # 범위, 주택당 지불 가격
    data = list(list(map(int, input().split())) for i in range(n))
    cnt = 0
    for i in range(n):
        for j in range(n):
            bfs(i, j)
    print(f'#{tc} {cnt}')
