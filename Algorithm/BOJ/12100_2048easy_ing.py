import sys
sys.stdin = open('input.txt')

'''
2048게임
4 x 4 보드 게임
한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것
같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다
한번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.


이 문제에서 다루는 2048 게임은 보드의 크기가 n×n 이다. 
보드의 크기와 보드판의 블록 상태가 주어졌을 때, 
최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

논리
- 5번의 이동 경우의 수 조합 모두구하기
    - 324 가지
- 각 조합의 이동 후 최대 최대값 갱신
- 각 조합 이동 방법
    1. 이동 후 이동 방향의 젤 끝 값부터 출발방향으로 비교
    2. 같으면 합치기
    3. 다르면 쌓기
    4. 이동 다하면 최대 값 찾기
    
에러
- max_value 비교 위치가 잘못되어 있었다.
- 0이 아닌 값을 찾는 함수에 idx out of range 에러가 발생했다.
'''


import sys, copy

input = sys.stdin.readline

n = int(input())
board1 = list(list(map(int, input().split())) for _ in range(n))


start_point = [(0, n-1), (0, 0), (n-1, 0), (0, 0)] # 비교 시작점
next = [(1, 0), (1, 0), (0, 1), (0, 1)]
d = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 동서남북 쪽으로 이동할 때 시작점과 다음 비교 위치와의 인덱스 차이

def find_value(r, c, dir, board):
    is_exist = True
    while board[r][c] == 0:
        r, c = r + dir[0], c + dir[1]
        if not (0 <= r < n) or not (0 <= c < n):
            is_exist = False
            break

    if is_exist:
        idx = (r, c)
        return idx
    else:
        return False

# 이동 조합 만들기
def play(case, _board):
    global max_value
    board = copy.deepcopy(_board)

    for move in case:
        for t in range(n):
            r, c = start_point[move][0] + next[move][0] * t, start_point[move][1] + next[move][1] * t

            while 0 <= r < n and 0 <= c < n: # 각 줄의 끝까지 도달할 때까지 반복
                # 현재 위치가 0일 때
                if board[r][c] == 0: # 다음 위치에 가장 가까운 0이 아닌 값 가져오기
                    idx = find_value(r, c, d[move], board)

                    if idx is not False:
                        board[r][c], board[idx[0]][idx[1]] = board[idx[0]][idx[1]], 0
                    else:
                        break

                # 현재 위치가 0이 아닐 때
                # 0이 아닌 다음 값 찾기
                if 0 <= r + d[move][0] < n and 0 <= c + d[move][1] < n:
                    idx1 = find_value(r + d[move][0], c + d[move][1], d[move], board)
                    if idx1 is False:
                        break

                if board[r][c] == board[idx1[0]][idx1[1]]:
                    board[r][c], board[idx1[0]][idx1[1]] = board[r][c] * 2, 0
                r, c = r + d[move][0], c + d[move][1]

    for row in range(n):
        max_value = max(max_value, max(board[row]))


def dfs(depth, board):
    if depth == 5: # 이동 조합 만들어지면 play 2048
        play(case, board)
        # print(case)
    else:
        for i in range(4):
            case.append(i)
            dfs(depth + 1, board)
            case.pop()


max_value = 0
case = []
if n == 1:
    print(board1[0][0])
else:
    dfs(0, board1)
    print(max_value)
