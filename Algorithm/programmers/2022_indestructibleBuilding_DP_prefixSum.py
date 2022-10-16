def solution(board, skill):
    n, m, k = len(board), len(board[0]), len(skill)
    '''
    누적합의 형태를 이용
    배열에 모든 공격/회복의 시작점과 (끝점+1)에 각각의 degree를 표시
    누적합 시행
    각 배열과 빌딩의 내구도를 비교하여 1보다 크면 카운트
    '''

    # 누적합 시킬 위치 board 상하좌우로 한 칸씩 여유만들기
    acc = list([0] * (m +2) for i in range(n + 2))
    
    for i in range(k):
        fr_i, fr_j, to_i, to_j = skill[i][1], skill[i][2], skill[i][3], skill[i][4],
        
        if skill[i][0] == 2:
            skill[i][-1] = -skill[i][-1]
        
        acc[fr_i + 1][fr_j + 1] += skill[i][-1]
        acc[to_i + 2][fr_j + 1] -= skill[i][-1]
        acc[fr_i + 1][to_j + 2] -= skill[i][-1]
        acc[to_i + 2][to_j + 2] += skill[i][-1]
        
    cnt = 0
    for r in range(n):
        for c in range(m):
            acc[r + 1][c + 1] += acc[r + 1][c] + acc[r][c + 1] - acc[r][c]
            
            if board[r][c] > acc[r + 1][c + 1]:
                cnt += 1
    
    return cnt