import sys
sys.stdin = open('input.txt')

def dfs(i, c):
    global min_cnt
    if c > min_cnt:
        return

    if i >= n:
        c -= 1
        if c < min_cnt:
            min_cnt = c
    else:
        for j in range(i + 1, i + stops[i] + 1):
            dfs(j, c + 1)

for tc in range(1, int(input()) + 1):
    stops = list(map(int, input().split()))
    n = stops[0]
    min_cnt = n
    dfs(1, 0)
    print(f'#{tc} {min_cnt}')
