import sys
sys.stdin = open('input.txt')

def inorder(node):
    global cnt
    if node and node <= n:
        inorder(c1[node])

        tree[node] = cnt
        cnt += 1

        inorder(c2[node])

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    e = n - 1

    cnt = 1

    tree = [0] * (n + 1)
    c1 = [0] * (n + 1)
    c2 = [0] * (n + 1)

    i = 1

    while i <= n:
        c1[i] = i * 2
        c2[i] = i * 2 + 1

        i += 1

    inorder(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')