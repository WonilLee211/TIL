import sys
sys.stdin = open('input.txt')

'''
주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 
주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램
주사위를 놓은 칸에 쓰여 있는 수는 항상 0

만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

지도 세로 가로 : n ,m, 주사위 위치 x, y, 명령 개수 : k
지도 n 줄 , 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.
마지막 줄, 이동하는 명령/ 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

논리
- 돌았을때 주사위 바닥 면의 마주보는 값을 출력
    - 범위가 벗어나는 움직일 때는 출력 안함
- 각 면의 동서남북을 미리 정할 수 있나?
- 못함
- 동서남북으로 이동할 때마다 현재의 주사위 면들이 어느 방향의 면을 바라보는지 정해야 함
- 북쪽으로 굴릴 때
    - 현재의 동서는 그대로 동서
    - 현재의 바닥면이 남쪽
    - 마주보는 면을 제외한 값이 북쪽
- 남쪽으로 굴릴 때
    - 현재의 동서는 그대로 동서
    - 현재의 바닥면이 북쪽
    - 마주보는 면을 제외한 값이 남쪽
- 동쪽으로 굴릴 때
    - 현재의 북남은 그대로
    - 서쪽2은 현재의 바닥면1
    - 동쪽
    
    - 마주보는 면을 제외한 값이 동쪽
- 서쪽으로 굴릴 때
    - 현재의 북남은 그대로
    - 현재의 바닥면이 동쪽
    - 마주보는 면 을 제외한 값이 서쪽   
'''

import sys
input = sys.stdin.readline

n, m, x, y, k = list(map(int, input().split()))

board = list(list(map(int, input().split())) for _ in range(n))
moves = list(map(int, input().split()))
d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남
acrossSide = [5, 4, 3, 2, 1, 0] # 마주보는 면
crtDice = [0, 2, 3, 1, 4, 5] # 현재의 바닥, 동, 서 북, 남, 위
dice_values = [0] * 6 # 해당 위치에 값 저장

cntBtm = 0

for move in moves:
    nx, ny = x + d[move][0], y + d[move][1]
    if not (0 <= nx < n) or not (0 <= ny < m):
        continue

    # m 방향으로 굴림
    # m 방향으로 굴릴 때 crtDice 갱신
    if move == 1: # 동쪽으로 굴릴 때
        crtDice[0], crtDice[1], crtDice[2], crtDice[5] = crtDice[move], crtDice[5], crtDice[0], crtDice[2]
    elif move == 2: # 서쪽으로 굴릴 때
        crtDice[0], crtDice[1], crtDice[2], crtDice[5] = crtDice[move], crtDice[0], crtDice[5], crtDice[1]
    elif move == 3: # 북쪽으로 굴릴 때
        crtDice[0], crtDice[3], crtDice[4], crtDice[5] = crtDice[move], crtDice[5], crtDice[0], crtDice[4]
    elif move == 4: # 남쪽으로 굴릴 때
        crtDice[0], crtDice[3], crtDice[4], crtDice[5] = crtDice[move], crtDice[0], crtDice[5], crtDice[3]

    # 해당 위치의 board값에 따른 갱신
    if board[nx][ny] != 0:
        dice_values[crtDice[0]] = board[nx][ny]
        board[nx][ny] = 0
    else:
        board[nx][ny] = dice_values[crtDice[0]]
    x, y = nx, ny

    print(dice_values[crtDice[5]]) # top 출력
