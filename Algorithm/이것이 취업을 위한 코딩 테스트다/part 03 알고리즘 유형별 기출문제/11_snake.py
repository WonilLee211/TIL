'''
규칙
1. 몸 길이를 늘려 머리를 다음 칸에 위치시킴
2. 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
3. 이동한 칸에 사과가 없다면, 몸의 길이를 줄여서 꼬리가 위치한 칸을 비움
4. 처음 오른 쪽 방향

n : 보드의 크기 0 ~ 100
k 개: 사과의 위치 개수 0 ~ 100
(r, c) k개
L : 뱀의 방향 변환 횟수
x, c : 게임시작으로부터 x초 뒤에 (L왼쪽, D오른쪽) 회전


사과 위치와 뱀 이동 경로가 주어질 떄 게임이 몇 초에 끝나는지 계산
'''
import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for i in range(n)]

for i in range(k):
    apple_r, apple_c = map(int, input().split())
    board[apple_r-1][apple_c-1] = 1

L = int(input())

change_time = [0] * 10001
for i in range(L):
    info = input().split()
    change_time[int(info[0])] = info[1]

r, c = 0, 0

t = 0
d = 0
direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]
change_d = {
    (0, 1): {'D': 1, 'L': 2},
    (1, 0): {'D': 3, 'L': 0},
    (-1, 0): {'D': 0, 'L': 3},
    (0, -1): {'D': 2, 'L': 1},
}

q = deque()
q.append((r, c))

while True:
    t += 1

    r, c = r + direct[d][0], c + direct[d][1]

    if not (0 <= r < n) or not (0 <= c < n) or (r, c) in q:
        break

    q.append((r, c))

    if board[r][c] == 0:
        q.popleft()
    else:
        board[r][c] = 0

    if change_time[t] != 0:
        d = change_d[direct[d]][change_time[t]]

print(t)
