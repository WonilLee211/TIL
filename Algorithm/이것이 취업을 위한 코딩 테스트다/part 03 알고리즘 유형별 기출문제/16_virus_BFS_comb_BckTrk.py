import sys
sys.stdin = open('input.txt')

from itertools import combinations as comb
from collections import deque
from copy import deepcopy

def bfs(data):
    global max_cnt

    cnt = len(svZn_idx)

    queue = deque()
    queue.extend(virus_idx)
    visited = [['0']*c for _ in range(r)]
    
    for i, j in virus_idx:
        visited[i][j] = '2'

    while queue:
        sr, sc = queue.popleft()
        
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if 0 <= sr + dr < r and 0 <= sc + dc < c and data[sr + dr][sc + dc] == '0' and visited[sr + dr][sc + dc] == '0':
                nr, nc = sr + dr, sc + dc
                queue.append((nr, nc))
                visited[nr][nc] = '2'
                cnt -= 1

        if cnt < max_cnt:
            break

        if not queue:
            if cnt > max_cnt:
                max_cnt = cnt

r, c = map(int, input().split())

maze =[[0] * c for _ in range(r)]

virus_idx = []
svZn_idx = []

for i in range(r):
    row = input().split()
    for j in range(c):
        if row[j] == '2':
            virus_idx.append((i,j)) # 바이러스 위치
        elif row[j] == '0':         # 빈칸 위치
            svZn_idx.append((i, j))
        maze[i][j] = row[j]

add_walls = list(comb(svZn_idx, 3)) # 빈칸들 중에 3개 조합
#  [((4, 3), (5, 6), (6, 2)), ((4, 3), (5, 6), (6, 3)), ...]

max_cnt = 0

for info in add_walls:
    data = deepcopy(maze)
    for i in range(3):
        data[info[i][0]][info[i][1]] = '1'
    
    bfs(data)

print(max_cnt - 3)