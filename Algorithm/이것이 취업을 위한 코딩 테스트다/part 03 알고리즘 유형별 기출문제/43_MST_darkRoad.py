import sys
sys.stdin = open('input.txt')

'''
최소거리로 연결하기

일부 가로등을 비활성화해서 절약할 수 있는 최대 금액을 출력하는 프로그램 작성

n, m : 집의 개수, 도로 개수
x, y, z : x번 집과 y번 집사이 양방향 거리 z
마을을 구성하는 모든 도로의 길이 합은 2^31

논리
- 최소신장거리
- 사이클이 발생하지 않는 길만 추가
- 최소 거리부터 점검

'''

import sys, heapq
input = sys.stdin.readline
hq = heapq


n, m = list(map(int, input().split()))

road_info = []
total_cost = opt_cost = 0

for _ in range(m):
    x, y, z = list(map(int, input().split()))
    total_cost += z
    hq.heappush(road_info, [z, x, y])

parent = list(range(n))

def find_parent(x):

    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

while road_info:

    w, a, b = hq.heappop(road_info)

    if find_parent(a) != find_parent(b):
        union(a, b)
        opt_cost += w

print(total_cost - opt_cost)
