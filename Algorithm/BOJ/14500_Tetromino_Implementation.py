import sys
sys.stdin = open('input.txt')

'''
조건
- 정사각형은 서로 겹치면 안 된다.
- 도형은 모두 연결되어 있어야 한다.
- 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.

NxM 종이
각 칸에 정수가 입력되어있음
도형이 높인 칸 수에 쓰여있는 수들의 합을 최대로하는 프로그램 작성
회전이나 대칭 가능

입력
n, m
n개의 줄에 종이에 쓰여 있는 수

논리
- 모든 정점에 대해서 dfs
- 그 중 가장 큰 값을 저장하고 다음 점으로 s
- dfs는 한붓그리기가 가능할 때만 된다.
    - ㅗ 모양은 따로 처리해야 함.

'''
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

board = []
maxV = 0
for i in range(n):
    temp = list(map(int, input().split()))
    maxV = max(maxV, max(temp))
    board.append(temp)

direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j, depth, acc):
    global cnt

    if depth == 3 and cnt < acc:
        cnt = acc
    if acc + maxV * (3 - depth) <= cnt:
        return
    else:
        for d in direc:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                visited.append((ni, nj))
                dfs(ni, nj, depth + 1, acc + board[ni][nj])
                # visited.pop()

ans = 0

for i in range(n):
    for j in range(m):

        cnt = 0
        visited = [(i, j)]
        cnt += board[i][j]
        dfs(i, j, 0, cnt)
        ans = max(ans, cnt)

print(ans)