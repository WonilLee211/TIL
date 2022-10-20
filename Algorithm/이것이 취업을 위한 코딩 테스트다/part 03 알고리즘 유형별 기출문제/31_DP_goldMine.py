'''
n * m : 금광의 크기

0번째 열에서 어느 행에서도 출발 가능
오른쪽과 오른쪽 대각선 방향으로 3방향 이동
m번에 걸쳐 채굴자가 얻을 수 있는 금의 최대 크기


논리
- 제한 시간 1초
- m번째 위치에서 계산한 값이 m + 1번째 dp 값보다 클 때 다음 단계로 넘어감
- 최종값이 얻을 수 있는 최댓값

'''

import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(int(input())):

    n, m = map(int, input().split())
    mines = [0 for _ in range(n)]
    tmp = list(map(int, input().split()))
    for i in range(n):
        mines[i] = tmp[i * m: i * m + 4]
    # [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]

    max_v = 0
    for i in range(n): # 행별로 시작점 정해서 검사

        dp = [0 for i in range(n + 1)]
        dp[0] = mines[i][0]
        q = deque([(i, 0)])

        while q:
            r, c = q.popleft()
            if c == m:
                if dp[-1] > max_v:
                    max_v = dp[-1]
            else:
                for nr, nc in [(r + 1, c + 1), (r, c + 1), (r - 1, c + 1)]:

                    if 0 <= nr < n and 0 <= nc <= m and dp[nc] < dp[c] + mines[nr][nc]:
                        print(nr, nc)
                        dp[nc] = dp[c] + mines[nr][nc]
                        q.append((nc, nr))
            print(dp)
    print(max_v)




