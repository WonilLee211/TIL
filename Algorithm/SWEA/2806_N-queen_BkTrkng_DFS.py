import sys
sys.stdin = open('input.txt')

def dfs(d):
    global cnt
    if d == n:
        cnt += 1
        return
    else:
        for i in range(n):
            flag = True
            case[d] = i
            for j in range(d):
                if case[j] == case[d] or abs(case[d] - case[j]) == abs(d - j):
                    flag = False
                    break

            if flag:
                dfs(d + 1)


for tc in range(1, int(input()) + 1):
    n = int(input())
    case = [0 for i in range(n)]
    cnt = 0
    dfs(0)
    print(f'{tc} {cnt}')