import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))

    cnt = 0
    for num in b:
        lo, hi = 0, n - 1
        md = (lo + hi) // 2

        flag = 0

        while lo <= hi:
            md = (lo + hi) // 2

            if a[md] == num:
                cnt += 1
                break
            elif a[md] < num:
                lo = md + 1
                if flag == 1:
                    break
                flag = 1
            else:
                hi = md - 1
                if flag == 2:
                    break
                flag = 2


    print(f'#{tc} {cnt}')