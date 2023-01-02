import sys
sys.stdin = open('input.txt')

'''
5 <= len(board) <= 100 


0 : 빈칸
1 : 벽

회전 조건
- 로봇은 90도씩 회전할 수 있습니다.
- 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 
- 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다.

"0"과 "1"로 이루어진 지도인 board가 주어질 때,
로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간을 return 

논리

'''

import sys, collections

input = sys.stdin.readline
deque = collections.deque
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_movable(robot, board):
    n = len(board)
    if 0 <= robot[0][0] < n and 0 <= robot[0][1] < n and 0 <= robot[1][0] < n and 0 <= robot[1][1] < n:
        if board[robot[0][0]][robot[0][1]] == 0 and board[robot[1][0]][robot[1][1]] == 0:
            return True
    return False


def get_next_robot(robot, board):
    next_robots = []
    # 상하좌우 이동 가능한 로봇
    for dr, dc in move:
        move_robot = [(robot[0][0] + dr, robot[0][1] + dc), (robot[1][0] + dr, robot[1][1] + dc)]
        if is_movable(move_robot, board):
            next_robots.append(set(move_robot))

    # 회전한 로봇
    if robot[0][0] == robot[1][0]:  # 가로 방향 로봇
        for i in [1, -1]:
            rotate_robot1 = [(robot[0][0], robot[0][1]), (robot[0][0] + i, robot[0][1])]
            rotate_robot2 = [(robot[1][0], robot[1][1]), (robot[1][0] + i, robot[1][1])]
            if is_movable(rotate_robot1, board) and is_movable(rotate_robot2, board):
                next_robots.append(set(rotate_robot1))
                next_robots.append(set(rotate_robot2))

    else:  # 세로 방향 로봇
        for i in [1, -1]:
            rotate_robot1 = [(robot[0][0], robot[0][1]), (robot[0][0], robot[0][1] + i)]
            rotate_robot2 = [(robot[1][0], robot[1][1]), (robot[1][0], robot[1][1] + i)]
            if is_movable(rotate_robot1, board) and is_movable(rotate_robot2, board):
                next_robots.append(set(rotate_robot1))
                next_robots.append(set(rotate_robot2))

    return next_robots


def solution(board):
    n = len(board)
    robot = {(0, 0), (0, 1)}

    visited = []

    q = deque()
    q.append((robot, 0))
    ans = 0

    while q:
        now, time = q.popleft()

        if (n - 1, n - 1) in now:
            return time

        for next_robot in get_next_robot(list(now), board):

            if next_robot not in visited:
                q.append((next_robot, time + 1))
                visited.append(next_robot)

    return ans



