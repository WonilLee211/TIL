import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):

    n, m = map(int, input().split())
    arr = [0] * m

    for c in range(m):
        arr[c] = list(map(int, input().split()))

    arr = arr[-1::-1] # pop(0)을 pop()으로 구현하기 위해 역정렬
    # i, j, clr
    # clr 1 = b, clr 2 = w
    # [[1, 2, 1], [1, 1, 2], [4, 3, 1], [4, 4, 2], [2, 1, 1], [4, 2, 2], [3, 4, 1], [1, 3, 2], [2, 4, 1], [1, 4, 2], [4, 1, 2], [3, 1, 2]]

    board = list([0] * n for i in range(n))

    board[n // 2 - 1][n // 2] = board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = board[n // 2 - 1][n // 2 - 1] = 2

    di = [1, -1, 0, 0, -1, 1, -1, 1]
    dj = [0, 0, 1, -1, -1, 1, 1, -1]

    while True:
        if arr:
            i, j, clr = arr.pop()
            i, j = i - 1, j - 1 # 주어진 인풋값을 board의 인덱스와 맞추기
        else:
            break

        if clr == 1: # 인풋값의 컬러가 블랙일 때

            if board[i][j] == 0: # 돌을 놓을 수 있다면
                board[i][j] = 1

                for k in range(8):
                    tmp1 = [] # 방향마다 흰 돌 위치 저장할 곳

                    if 0 <= i + di[k] < n and 0 <= j + dj[k]< n: #나아갈 곳이 범위 내에 있을 때
                        ni, nj = i + di[k], j + dj[k]
                        #
                        while board[ni][nj] == 2 and 0 <= ni < n and 0 <= nj < n:
                            tmp1.append((ni, nj))
                            ni, nj = ni + di[k], nj + dj[k]

                            if not (0 <= ni < n) or not (0 <= nj < n) or board[ni][nj] == 0:
                                tmp1 = []
                                break

                    for p in tmp1:
                        board[p[0]][p[1]] = 1

        else:
            if board[i][j] == 0:
                board[i][j] = 2

                for k in range(8):
                    tmp2 = []

                    if 0 <= i + di[k] < n and 0 <= j + dj[k] < n:
                        ni, nj = i + di[k], j + dj[k]
                        while board[ni][nj] == 1 and 0 <= ni < n and 0 <= nj < n:
                            tmp2.append((ni, nj))
                            ni, nj = ni + di[k], nj + dj[k]
                            if not (0 <= ni < n) or not( 0 <= nj < n) or board[ni][nj] == 0:
                                tmp2 = []
                                break

                    for p in tmp2:
                        board[p[0]][p[1]] = 2

    cnt1 = cnt2 = 0
    for row in board:
        for i in range(n):
            if row[i] == 1:
                cnt1 += 1
            elif row[i] == 2:
                cnt2 += 1

    print(f'#{tc}', cnt1, cnt2)