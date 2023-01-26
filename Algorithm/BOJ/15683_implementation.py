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
input = sys.stdin.readline

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

cctv = [[],
        [[(0, 1)], [(-1, 0)], [(0, -1)], [(1, 0)]],
        [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
        [[(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)], [(1, 0), (0, 1)]],
        [[(0, -1), (-1, 0), (1, 0)], [(0, 1), (-1, 0), (1, 0)], [(0, 1), (0, -1), (1, 0)], [(0, 1), (0, -1), (-1, 0)]],
        [[(0, 1), (0, -1), (-1, 0), (1, 0)]]]


idx_cctv = []
for i in range(n):
    for j in range(m):