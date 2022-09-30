import sys
sys.stdin = open('input.txt')


def dfs(opnums, d, s):
    global min_v, max_v

    if d == m:
        if min_v > s:
            min_v = s
        if max_v < s:
            max_v = s
    else:
        for i in range(4):
            if opnums[i]:
                opnums[i] -= 1

                if i == 0:
                    s_ = s + arr[d + 1]
                elif i == 1:
                    s_ = s - arr[d + 1]
                elif i == 2:
                    s_ = s * arr[d + 1]
                else:
                    s_ = int(s / arr[d + 1])
                dfs(opnums, d + 1, s_)
                opnums[i] += 1

for tc in range(1, int(input()) + 1):

    n = int(input())
    opnums = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    max_v = -100000001
    min_v = 100000001
    m = sum(opnums)
    dfs(opnums, 0, arr[0])

    print(f'#{tc} {(max_v-min_v)}')