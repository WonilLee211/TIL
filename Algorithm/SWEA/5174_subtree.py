import sys
sys.stdin = open('input.txt')

def BT_search(node):
    global cnt

    if node:
        cnt += 1
        BT_search(c1[node])
        BT_search(c2[node])

T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    v = e + 1

    c1 = [0] * (v + 1)
    c2 = [0] * (v + 1)
    arr = list(map(int, input().split()))

    for i in range(0, e*2, 2):
        if not c1[arr[i]]:
            c1[arr[i]] = arr[i + 1]
        else:
            c2[arr[i]] = arr[i + 1]

    cnt = 0
    BT_search(n)
    print(f'#{tc} {cnt}')