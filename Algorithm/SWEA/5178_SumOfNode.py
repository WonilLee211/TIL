import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    n, m, target = map(int, input().split())

    tree = [0] * (n + 1)

    for i in range(m):
        num, val = map(int, input().split())
        tree[num] = val

    for num in range(n, 0, -1):
        if num//2:
            tree[num//2] += tree[num]

    print(f'#{tc} {tree[target]}')