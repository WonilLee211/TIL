import sys
sys.stdin = open('input.txt')

def find_p(x):
    while x != p[x]:
        x = find_p(p[x])
    return x

def union(x, y):
    a = find_p(x)
    b = find_p(y)
    if b > a:
        p[b] = a
    else:
        p[a] = b

for tc in range(1, int(input())  + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    p = [i for i in range(n + 1)]
    for i in range(m):
        union(a[i * 2], a[i * 2 + 1])

    res = []
    for i in range(1, n + 1):
        repre = find_p(i)
        if repre not in res:
            res.append(repre)

    print(f'#{tc} {len(res)}')
