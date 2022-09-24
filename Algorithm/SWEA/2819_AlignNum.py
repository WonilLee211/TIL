import sys
sys.stdin = open('input.txt')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
def dfs(i, j, temp):
    if len(temp) == 7:
        case.append(temp)
    else:
        for k in range(4):
            if 0 <= i + di[k] < 4 and 0 <= j + dj[k] < 4:
                dfs(i + di[k], j + dj[k], temp + data[i + di[k]][j + dj[k]])

for tc in range(1, int(input()) + 1):
    data = list(input().split() for i in range(4))
    case = []
    for i in range(4):
        for j in range(4):
            temp = data[i][j]
            dfs(i, j, temp)

    print(f'#{tc} {len(set(case))}')