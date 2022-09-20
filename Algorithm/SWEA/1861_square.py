import sys
sys.stdin = open('input.txt')

from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    arr = [[0] * n] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    num, cnt = n ** 2, 0

    for i in range(n):
        for j in range(n):
            visited = [0] * (n**2+1)
            m = 1
            q = deque()
            q.append((i, j))

            while q:
                ni, nj = q.popleft()

                for k in range(4):
                    if 0 <= ni + di[k] < n and 0 <= nj + dj[k] < n:
                        if not visited[arr[ni + di[k]][nj + dj[k]]] and arr[ni + di[k]][nj + dj[k]] == arr[ni][nj] + 1:
                            ni, nj = ni + di[k], nj + dj[k]
                            q.append((ni, nj))
                            visited[arr[ni][nj]] = 1
                            m += 1

            if cnt <= m:
                if cnt == m and num < arr[i][j]:
                    continue
                cnt = m
                num = arr[i][j]

    print(f'#{tc} {num} {cnt}')