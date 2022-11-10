'''

2 : 치킨
1 : 집
0 : 빈칸
치킨 거리 : 집과 가장 가까운 치킨 집 사이 거리

M개의 치킨집을 골라 치킨거리가 가장 작게 되는 구하는 프로그램
M개의 치킨집의 치킨 거리 최소값

논리
-
'''
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

chickens = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chickens.append((i, j))
dist_list = []
for chicken in chickens:
    min_dist = 2 * n
    for i in range(n):

        if min_dist < abs(chicken[0] - i):
            break

        for j in range(n):
            if board[i][j] in [0, 2]:
                continue

            min_dist = min(min_dist, abs(chicken[0] - i) + abs(chicken[1] - j))

    dist_list.append(min_dist)

print(sum(sorted(dist_list)[:m]))