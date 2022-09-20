def solution(board, skill):
    n, m = len(board), len(board[0])

    for i in range(len(skill)):
        sk = skill[i]
        if sk[0] == 1:
            sk[-1] = -sk[-1]

    for effect in skill:
        t, f_r, f_c, t_r, t_c, p = effect
        for r in range(f_r, t_r + 1):
            for c in range(f_c, t_c + 1):
                board[r][c] += p

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                cnt += 1

    return cnt

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board, skill))