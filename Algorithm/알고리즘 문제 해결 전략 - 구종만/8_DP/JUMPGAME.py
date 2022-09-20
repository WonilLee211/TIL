'''
N*N크기의 격자에 1부터 9까지의 정수를 쓴 게임판  2 <= N <= 100
왼쪽 위에서 시작해서 오른쪽 아래 칸에 도착
각 칸에 적혀 있는 숫자만큼 아래, 오른쪽으로 이동 가능

게임판이 주어질 때 끝점에 도달할 수 있는 경로가 있는지 확인하기
'''
import sys
sys.stdin =open('input.txt')
'''
# 재귀 함수 구현
def jump(r, c): # 목적지에 도달할 수 있는지 없는지 반환
    if r >= n or c >= n:
        return False
    if r == n-1 and c == n-1:
        return True
    jumpsize = data[r][c]
    return jump(r + jumpsize, c) or jump(r, c + jumpsize)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = [[]] * n

    for i in range(n):
        data[i] = list(map(int, sys.stdin.readline().split()))

    if jump(0, 0):
        print('YES')
    else:
        print('NO')
'''

# memoization으로 전환
def memo_jump(r, c):

    if r >= n or c >= n: # 기저 상태 처리
        return 0

    # (n-1, n-1)에
    if r == n-1 and c == n-1:
        return 1

    # 아직 (n-1, n -1)에 도착하지 못했을 경우
    if cache[r][c] == -1:
        jumpsize = data[r][c]
        # 열방향으로 기저 사례나 목적지에 도달할 때까지 깊게 탐색하고 행방향으로 가보기

    return cache[r][c]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = [[]] * n

    for i in range(n):
        data[i] = list(map(int, sys.stdin.readline().split()))

    cache = [[-1] * n for i in range(n)]

    if memo_jump(0, 0):
        print('YES')
    else:
        print('NO')