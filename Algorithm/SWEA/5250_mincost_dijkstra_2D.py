import sys
sys.stdin = open('input.txt')

INF = int(1e9)
di = [1, -1, 0 ,0]
dj = [0, 0, 1, -1]
from collections import deque

for tc in range(1, int(input()) + 1):
    n = int(input())
    levels = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF] * n for i in range(n)]

    p = (0, 0)

    q = deque()
    q.append((0, p))
    dp[p[0]][p[1]] = 0

    while q:
        w, p = q.popleft()

        if dp[p[0]][p[1]] < w:              # 이미 처리되었다면 pass
            continue
        for i in range(4):
            # 갈 수 있는 범위 밖이면 pass
            if (not 0 <= p[0] + di[i] < n) or (not 0 <= p[1] + dj[i] < n):
                continue

            ni, nj = p[0] + di[i], p[1] + dj[i]
            diff = levels[ni][nj] - levels[p[0]][p[1]]
            if diff < 0:                    # 레벨 차이가 음수이면 0으로 초기화
                diff = 0
            if dp[ni][nj] > dp[p[0]][p[1]] + diff + 1: # 현재까지의 최소값 + 레벨 차이 + 기본 이동 소요
                dp[ni][nj] = dp[p[0]][p[1]] + diff + 1

                q.append((dp[ni][nj], (ni, nj)))

    print(f'#{tc} {dp[n - 1][n - 1]}')
