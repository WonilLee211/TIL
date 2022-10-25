'''
지워진 파이프의 위치와 파이프 종류 알아내기

논리
- M 위치 찾기
- Z에 도착할 때까지 순환
- 빈칸 찾으면
    - 나아갈 수 있는 곳이 한방향뿐이거나
    - 3방향이거나
    - 연결될 수 있는지 확인하고 연결되면 파이프 설치
        - 연결 가능한지

'''

import sys
sys.stdin = open('input.txt')

R, C = list(map(int, input().split()))
land = [list(input().split()) for _ in range(R)]

fr_r, fr_c, to_r, to_c = 0, 0, 0, 0

for r in range(R):
    for c in range(C):
        if land[r][c] == "M":
            fr_c, fr_r = r, c
        elif land[r][c] == "Z":
            to_c, to_r = r, c

blocks = {
    '|' :
}