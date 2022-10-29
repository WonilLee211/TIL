'''
N 개의 집에 C개의 공유기 설치
가장 인접한 두 공유기 사이의 최대 거리 출력

논리
- 인풋이 10억
- 인접한 두 공유기의 거리로 가능한 범위는 1 ~ (max(homes) - min(homes))
- 가운데 값의 거리부터 그 거리 이상으로 공유기를 설치할 수 있다면 저장해두고 큰 범위에 대해서 다시 체크
- 설치할 수 없다면 거리를 줄여서 체크
- 가능한 값 중 최대 거리로 저장

'''

import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
n, c = map(int, input().split())
homes = list(int(input()) for _ in range(n))
homes.sort()

max_distance = homes[-1] - homes[0]
res = 0

def binary_search(fr, to):
    global res

    if fr > to:
        return

    distance = (to + fr) // 2

    cnt = 1
    now = homes[0]

    for i in range(1, n):
        if homes[i] >= now + distance:
            now = homes[i]
            cnt += 1

    if cnt >= c:
        res = distance
        binary_search(distance + 1, to)
    elif cnt < c:
        binary_search(fr, distance - 1)

binary_search(1, max_distance)

print(res)