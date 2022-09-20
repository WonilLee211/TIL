import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m, r, c, L = map(int, input().split())
    visited = [[0] * m for i in range(n)]
    arr = [0] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    moves = [0] * 8
    moves = [
        [],
        [(1, 0), (-1, 0), (0, 1), (0, -1)],
        [(1, 0), (-1, 0)],
        [(0, 1), (0, -1)],
        [(-1, 0), (0, 1)],
        [(1, 0), (0, 1)],
        [(1, 0), (0, -1)],
        [(-1, 0), (0, -1)],
    ]

    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        ni, nj = q.popleft()

        for mv in moves[arr[ni][nj]]:
            if 0 <= ni + mv[0] < n and 0 <= nj + mv[1] < m:
                if not visited[ni + mv[0]][nj + mv[1]] and arr[ni + mv[0]][nj + mv[1]]:
                    temp = arr[ni + mv[0]][nj + mv[1]]
                    for mv_ in moves[temp]:
                        if mv[0] == -mv_[0] and mv[1] == -mv_[1]:
                            visited[ni + mv[0]][nj + mv[1]] = visited[ni][nj] + 1
                            q.append((ni + mv[0], nj + mv[1]))

    cnt = 0
    for arr in visited:
        for i in range(m):
            if 0 < arr[i] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')