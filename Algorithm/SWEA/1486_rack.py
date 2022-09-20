import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))

    diff = sum(arr)

    for i in range(1, 1 << n+1):
        cnt = 0
        for j in range(n):
            if i & (1 << j):
                cnt += arr[j]

            if cnt > diff + b:
                break

        if cnt >= b and diff > cnt - b:
            diff = cnt - b

    print(f'#{tc} {diff}')
