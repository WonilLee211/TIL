import sys
sys.stdin = open('input.txt')


'''
3차원 배열
두 지점간의 거리
min(abs(x1-x2),abs(y1-y2),abs(z1-z2))
터널을 n-1개 건설해서 최소 비용으로 구하는 프로그램

n : 행성의 수 1 <= n <= 100,000
x, y, z : n개의 줄 행성별 위치 

논리
- 최소신장트리
- 각 지점에서 최소값
- 시간복잡도가 문제
- x, y, z 기준으로 정렬한 리스트 3개
- x, y, z 별로 리스트 순서대로 비용 개산 후 
- 그 행렬과 사이클을 형성하지 않으면 union

'''

import sys, heapq
input = sys.stdin.readline
hq = heapq

n = int(input())
planets = [[i] + list(map(int, input().split())) for i in range(n)] # 행성번호, x, y, z

sortByX = sorted(planets, key=lambda x : x[1]) # x 기준 정렬
sortByY = sorted(planets, key=lambda x : x[2]) # y 기준 정렬
sortByZ = sorted(planets, key=lambda x : x[3]) # z 기준 정렬

# 정렬 결과
# [[2, -1, -1, -5], [3, 10, -4, -1], [0, 11, -15, -15], [1, 14, -5, -15], [4, 19, -4, 19]]
# [[0, 11, -15, -15], [1, 14, -5, -15], [3, 10, -4, -1], [4, 19, -4, 19], [2, -1, -1, -5]]
# [[0, 11, -15, -15], [1, 14, -5, -15], [2, -1, -1, -5], [3, 10, -4, -1], [4, 19, -4, 19]]

parent = list(range(n))                 # 자기자신을 루트 값으로 갖는 리스트

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    parent[find_parent(y)] = parent[find_parent(x)]


tunnels = []
for i in range(n - 1):  # x, y, z 계산 결과 저장
    hq.heappush(tunnels, [abs(sortByX[i][1] - sortByX[i + 1][1]), sortByX[i][0], sortByX[i + 1][0]])
    hq.heappush(tunnels, [abs(sortByY[i][2] - sortByY[i + 1][2]), sortByY[i][0], sortByY[i + 1][0]])
    hq.heappush(tunnels, [abs(sortByZ[i][3] - sortByZ[i + 1][3]), sortByZ[i][0], sortByZ[i + 1][0]])

cost = 0
while tunnels:
    w, a, b = hq.heappop(tunnels)

    if find_parent(a) != find_parent(b):
        union(a, b)
        cost += w

print(cost)