import sys
sys.stdin = open('input.txt')

'''
G : 탑승구 수 1 <= g < 100,000
P : 비행기 수 1 <= p < 100,000
도킹할 수 있는 탐승구 번호 : p개 줄
 - i번째 비행기가 1번부터 gi번째 탑승구 중 하나에 도킹할 수 있다는 의미

출력
- 도킹할 수 있는 비행기 최대 개수

논리
- 서로소 집합 연산 이용
- 도킹가능한 탑승구 번호에서부터 -1 작은 번호의 탑승구에 대해서 도킹 가능한지 확인
- 루트가 0이 아니라면 1 ~ 자기 번호까지 도킹할 수 있는 탑승구가 하나는 있다는 뜻
- 루트가 0이 아니라면 union 
- 0 이라면 stop

'''


import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

parent = list(range(g + 1))

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])

    return parent[x]

def union(x, y):
    parent[find_parent(y)] = parent[find_parent(x)]

root = 0
cnt = p
ans = 0

while cnt != 0:

    cnt -= 1
    info = int(input())

    root = find_parent(info)

    if root == 0:
        break

    union(parent[info]-1, info)
    ans += 1

print(ans)

