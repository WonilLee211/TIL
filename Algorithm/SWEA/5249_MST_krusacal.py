import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

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

for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())

    p = [i for i in range(0, v + 1)]

    edges= []
    for i in range(e):
        a, b, w = map(int, input().split())
        edges.append([w, a, b])
    edges.sort()

    cnt = 0
    for edge in edges:
        w, a, b = edge
        if find_p(a) != find_p(b):
            union(a, b)
            cnt += w

    print(f'#{tc} {cnt}')