import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    last = 0

    tree = [0] * (n + 1)

    for i in range(n):
        last += 1

        c = last
        p = c // 2

        tree[last] = arr[i]

        while p and tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            c = p
            p = c // 2

    total = 0
    p = n // 2
    while p:
        total += tree[p]
        p //= 2

    print(f'#{tc} {total}')
