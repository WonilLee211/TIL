import sys

sys.stdin = open("input.txt")

'''
n, m = 세로 가로
지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호
(1 ≤ N, M ≤ 8)
CCTV의 최대 개수는 8개를 넘지 않는다.

완전탐색해야할 듯


'''

import sys
import copy

copy = copy.deepcopy
input = sys.stdin.readline


def mark_cctvline(i, j, direction, office_):
    for di, dj in direction:
        ni, nj = i, j
        while True:
            if 0 <= ni + di < n and 0 <= nj + dj < m:
                ni, nj = ni + di, nj + dj
                if office_[ni][nj] == 6:
                    break
                elif office_[ni][nj] == 0:
                    office_[ni][nj] = 7
            else:
                break
    return office_


def count_zero(watched_office):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if watched_office[i][j] == 0:
                cnt += 1
    return cnt


def dfs(depth, office):
    global min_acc

    if depth == num_cctv:
        min_acc = min(count_zero(office), min_acc)
    else:
        copied_office = copy(office)
        r, c, num = info_cctv[depth]
        for direction in cctv[num]:
            dfs(depth + 1,  mark_cctvline(r, c, direction, copied_office))
            copied_office = copy(office)

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

cctv = [[],
        [[(0, 1)], [(-1, 0)], [(0, -1)], [(1, 0)]],
        [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
        [[(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)], [(1, 0), (0, 1)]],
        [[(0, -1), (-1, 0), (1, 0)], [(0, 1), (-1, 0), (1, 0)], [(0, 1), (0, -1), (1, 0)], [(0, 1), (0, -1), (-1, 0)]],
        [[(0, 1), (0, -1), (-1, 0), (1, 0)]]]

info_cctv = []
for i in range(n):
    for j in range(m):
        if office[i][j] not in [0, 6]:
            info_cctv.append((i, j, office[i][j]))

num_cctv = len(info_cctv)
min_acc = 64


dfs(0, office)
print(min_acc)
