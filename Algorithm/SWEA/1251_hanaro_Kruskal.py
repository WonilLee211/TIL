import sys
sys.stdin = open('input.txt')

def find_p(x):
    while x != parents[x]:
        x = find_p(parents[x])
    return x

def union(x, y):
    a = find_p(x)
    b = find_p(y)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

INF = int(1e9)
for tc in range(1, int(input()) + 1):
    # e*(l**2)

    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    p = tuple(zip(x, y))
    nodes = {i:p[i-1] for i in range(1, n + 1)}
    # [(1, (0, 0)), (2, (0, 100)), (3, (400, 0)), (4, (400, 100))]
    e = float(input())

    dp = [INF for i in range(n + 1)]
    dist = []

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d = ((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2) * e
            if d > 0:
                dist.append((d, i, j))
    '''
    [(10000, 1, 2), (160000, 1, 3), (170000, 1, 4), (10000, 2, 1), 
    (170000, 2, 3), (160000, 2, 4), (160000, 3, 1), (170000, 3, 2), 
    (10000, 3, 4), (170000, 4, 1), (160000, 4, 2), (10000, 4, 3)]
    '''
    dist.sort()
    parents = [i for i in range(0, n + 1)]

    res = 0
    for d in dist:
        w, a, b = d
        if find_p(a) != find_p(b):
            union(a, b)
            res += w

    print(f'#{tc} {round(res)}')


