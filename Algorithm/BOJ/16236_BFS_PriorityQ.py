'''
작은 물고기만 먹는 아기상어
크기가 같거나 작은 물고기가 있는 칸을 지날 수 있음
상하좌우 가는 조건
- 먹을 수 있는 물고기가 공간에 없다면 엄마 상어한테 도움 요청(끝)
- 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러감
- 먹을 수 있는 물고기가 1마리보다 많다면 거리가 가장 가까운 물고기
    - 거리 : 지나야하는 칸수의 최소값
    - 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기.
    - 그러한 물고기가 여러 마리라면 가장 왼쪽에 있는 물고기(우선순위 큐 3차원)

- 자기의 크기와 같은 수의 물고기를 먹었을 때 마다 1씩 증가
먹어야 하는 양이 2, 3, 4, 5, 6, ...

먹을  수 있을 만큼 먹는데 걸리는 시간구하기
2초 : 40만번 연산 가능
물고기 : 1,2,3,4,5,6
아기상어 위치 : 9

논리
- 물고기 크기별 위치 저장하기.
- 처음에 크기가 2니까 1의 물고기만 먹으러 다녀야 함.
- 일단 우선순위큐 bfs로 목표 물고기 탐색. q = visited, i, j
- 가장 먼저 작은 물고기 찾으면 먹고 visited 초기화
- 먹은 물고기 양 체크. 자기 크기 만큼 먹었으면 크기  + 1. 먹은 물고기양 초기화
- 먹을 물고기가 있는지 확인

'''
import sys
sys.stdin = open('input.txt')

import sys
import heapq
input = sys.stdin.readline
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def is_inner(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

def bfs(start):
    global shark_size, time
    eat = 0
    board[start[0]][start[1]] = 0

    visited = list([0] * n for _ in range(n))
    visited[start[0]][start[1]] = 1

    q = []
    heapq.heappush(q, (visited[start[0]][start[1]], start[0], start[1]))

    while q:
        t, ni, nj = heapq.heappop(q)

        if 0 < board[ni][nj] < shark_size:
            board[ni][nj] = 0
            eat += 1
            fishes[board[ni][nj]] -= 1
            time += t - 1
            visited = list([0] * n for _ in range(n))
            visited[ni][nj] = 1
            q = []
            heapq.heappush(q, (0, ni, nj))

            if eat == shark_size:
                shark_size += 1
                eat = 0

                if set([0]) == set(fishes[:shark_size]):
                    return
                continue

            if set([0]) == set(fishes[:shark_size]):
                return


        for i in range(4):
            t_i, t_j = ni + di[i], nj + dj[i]
            if  is_inner(t_i, t_j) and not visited[t_i][t_j] and board[t_i][t_j] <= shark_size:
                visited[t_i][t_j] = visited[ni][nj] + 1
                heapq.heappush(q, (visited[t_i][t_j], t_i, t_j))


n = int(input())
time = 0

fishes = [0 for i in range(7)]
shark_idx = [0, 0]
shark_size = 2

board = [0 for i in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 9:
            shark_idx[0], shark_idx[1] = i, j
        if temp[j] in list(range(1, 7)):
            fishes[temp[j]] += 1
    board[i] = temp

bfs(shark_idx)

print(time)