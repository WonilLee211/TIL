import sys
sys.stdin = open('input.txt')

import heapq

for tc in range(1, int(input()) + 1):
    n, e = map(int, input().split())
    LkL = [[] for i in range(n + 1)]
    total = 0
    for i in range(e):
        s, e, w = map(int, input().split())
        total += w
        LkL[s].append((e, w))
    # [[(1, 1), (2, 6)], [(2, 1)], []]

    h = []
    heapq.heappush(h, (0, 0))
    visited = [0 for i in range(n + 1)]
    dp = [10 * (n**2) for i in range(n + 1)]
    dp[0] = 0
    print(LkL)
    while h:
        print('h', h)

        p = heapq.heappop(h)
        print('p', p)

        if visited[p[0]] == 0:
            visited[p[0]] = 1
            for node in LkL[p[0]]:
                if dp[node[0]] > p[1] + node[1]:
                    dp[node[0]] = p[1] + node[1]
                    heapq.heappush(h, (node[0], dp[node[0]]))

    print(f'#{tc} {dp[-1]}')
