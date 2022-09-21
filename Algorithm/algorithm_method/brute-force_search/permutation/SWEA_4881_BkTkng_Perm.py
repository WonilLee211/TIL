
def perm(i):
    global minV
    if i == n:
        temp = 0
        for k in range(n):
            temp += arr[k][p[k]]
        if minV > temp:
            minV = temp
        elif temp > minV:
            return
    else:
        for j in range(i, n):
            p[j], p[i] = p[i], p[j]
            perm(i + 1, k)
            p[j], p[i] = p[i], p[j]            


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n) ]
    p = [i for i in range(n)]         # p[i] i행에서 선택한 열 번호
    minV = n * 10

    perm(0)
    print(f'#{tc} {minV}')