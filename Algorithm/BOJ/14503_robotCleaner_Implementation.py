import sys
sys.stdin = open('input.txt')

'''
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램
NxM크기
벽 또는 빈칸
청소기는 바라보는 방향이 있음
동서남북 중 하나

동작규칙
1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

입력
n m
(r, c), 바라보는 방향(d = 0 : 북, 1 : 동, 2 : 남, 3 : 서)
n개의 줄 , 빈칸은 0  벽은 1 
첫 행 마지막행 첫열 마지막 열은 벽

논리
- 동작규칙을 코드로 구현
- 청소한다 - visited로 표시
- 청소 후 왼쪽방향부터 방문안했다면 방향 틀기, 그 방향으로 나아가기
'''

import sys, copy
input = sys.stdin.readline

n, m = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))

board = list(list(map(int, input().split())) for i in range(n))
visited = copy.deepcopy(board)
turn = [3, 0, 1, 2]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0
while True:
    flag = False

    # 현재 위치 청소
    if visited[r][c] != -1:
        visited[r][c] = -1
        cnt += 1

    # 다음 청소할 곳 찾기
    nd = turn[d]
    while visited[r + move[nd][0]][c + move[nd][1]] != 0:
        if nd == d:
            flag = True
            break

        nd = turn[nd]


    if not flag:
        d = nd
        r, c = r + move[nd][0], c + move[nd][1]
    else:
        if visited[r - move[d][0]][c - move[d][1]] == -1:
            r, c = r - move[d][0], c - move[d][1]
        else:
            break

print(cnt)