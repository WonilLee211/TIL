import sys
sys.stdin = open('input.txt')

def dfs(i, m, rm):
    global max_v

    if max_v > rm * m:
        return

    if i == n:
        if max_v < m:
            max_v = m
    else:
        for j in range(n):
            if j not in case and data[i][j] != 0:
                case[i] = j
                dfs(i + 1, m * data[i][j], rm/max_case[i])
                case[i] = -1


for tc in range(1, int(input()) + 1):
    n = int(input())
    max_case = [0 for i in range(n)]
    data = [0 for i in range(n)]

    for i in range(n):
        temp = list(map(int, input().split()))
        max_case[i] = max(temp)
        data[i] = temp[:]
    case = [-1] * n
    max_v = 0
    rm = 1
    for x in max_case:
        rm *= x

    dfs(0, 1, rm)
    max_v = round(max_v /100**(n-1), 6)

    print(f'#{tc} {max_v:2.6f}')