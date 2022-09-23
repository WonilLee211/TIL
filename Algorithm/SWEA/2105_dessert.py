import sys
sys.stdin = open('input.txt')

def dfs(i, j, cafes, d):
    global max_cnt

    if d >= 2 and (i, j) == (initI + 1, initJ - 1):
        if max_cnt < len(cafes):
            max_cnt = len(cafes)
    else:
        for k in range(2):
            if k + d == 4:
                continue
            ni, nj = i + di[d + k], j + dj[d + k]
            if [ni, nj] not in visited and 0 <= ni < n and 0 <= nj < n and data[ni][nj] not in cafes:
                visited.append([ni, nj])
                cafes.append(data[ni][nj])
                dfs(ni, nj, cafes, d + k)
                visited.pop()
                cafes.pop()

for tc in range(1, int(input()) + 1):
    n = int(input())
    data = list(input().split() for i in range(n))

    # 0 ~ n - 3 :  검사할 범위

    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]
    max_cnt = 0
    for r in range(n-2):
        for c in range(n-1):
            initI, initJ = r, c
            visited = []
            cafes = []
            cafes.append(data[r][c])
            visited.append([r, c])
            dfs(r, c, cafes, 0)

    print(f'#{tc} {max_cnt or -1}')
