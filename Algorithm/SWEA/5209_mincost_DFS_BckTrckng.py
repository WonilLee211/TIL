import sys
sys.stdin = open('input.txt')

def dfs(i, s, rs):
    global min_c

    if min_c < sum(rs) + s:
        return
    if i == n:
        if min_c > s:
            min_c = s
    else:
        for j in range(n):
            if j not in case:
                case[i] = j
                dfs(i + 1, s + data[i][j], rs[i+1:])
                case[i] = -1

for tc in range(1, int(input()) + 1):
    n = int(input())
    min_case = [0 for i in range(n)]
    data = [0 for i in range(n)]

    for i in range(n):
        temp = list(map(int, input().split()))
        min_case[i] = min(temp)
        data[i] = temp[:]

    case = [-1] * n
    min_c = 99 * 9
    dfs(0, 0, min_case)
    print(f'#{tc} {min_c}')