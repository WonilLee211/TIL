import sys

sys.stdin = open('input.txt')

'''
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 
익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.

입력 
- m, n : 가로 세로
- 토마토 정보 n 줄
    - 1 : 익은 토마토
    - 0 익지 않은 토마토
    - -1 : 빈 칸
토마토가 하나 이상 있는 경우만 입력
2 ≤ M,N ≤ 1,000

출력
- 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력
- 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
- 모두 익지는 못하는 상황이면 -1을 출력

- 1이 없는 경우 -1 출력
- 0이 없는 경우 0 출력
- 1의 위치 저장
- bfs
- 0이 다 사라질 때까지 돌기
- Cnt 세기

에러
- 마지막에 엣지케이스 외에 모든 토마토가 익지 않을 수도 있는 경우를 고려하지 못했음
- bfs이후에 cnt0이 0이 되지 않은 경우 -1 출력
'''

import sys
from collections import deque

input = sys.stdin.readline

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
m, n = list(map(int, input().split()))
cnt1 = cnt0 = cntB = 0 # 익은, 익지않은, 비어있는
idx1 = []
board = []

for i in range(n):
    temp = list(map(int, input().split()))

    for idx, tomato in enumerate(temp):

        if tomato == 1:

            idx1.append((i, idx))
            cnt1 += 1

        elif tomato == -1:
            cntB += 1

    board.append(temp)

cnt0 = n * m - cnt1 - cntB

if cnt0 == 0: # 0이 없는 경우 0 출력
    print(0)

elif cnt1 == 0: # 1이 없는 경우 -1 출력
    print(-1)

else:
    t = 0

    visited = [[0] * m for _ in range(n)]

    q = deque(idx1)

    while cnt0 != 0 and q:

        node = q.popleft()

        for d in moves:
            ni, nj = node[0] + d[0], node[1] + d[1]

            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 0 and visited[ni][nj] == 0:

                visited[ni][nj] = visited[node[0]][node[1]] + 1
                cnt0 -= 1
                q.append((ni, nj))

            if cnt0 == 0:
                t = visited[ni][nj]
                break

    if cnt0 != 0:
        print(-1)
    else:
        print(t)
