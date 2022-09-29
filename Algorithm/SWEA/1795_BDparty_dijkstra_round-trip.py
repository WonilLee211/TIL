import sys
sys.stdin = open('input.txt')


import heapq as hq
INF = int(1e9)

def dijkstra(st):

    dp = [INF for _ in range(n + 1)]
    q = []
    hq.heappush(q, (0, st))
    dp[st] = 0
    while q:
        w, node = hq.heappop(q)
        if dp[node] < w:
            continue

        for adj in LKL[node]:
            if dp[adj[0]] > w + adj[1]:
                dp[adj[0]] = w + adj[1]
                hq.heappush(q, (dp[adj[0]], adj[0]))

    return dp

for tc in range(1, int(input()) + 1):
    n, m, start = map(int, input().split())

    cnt = 0

    LKL = [[] for i in range(n + 1)]

    for i in range(m):
        x, y, c = map(int, input().split())
        LKL[x].append((y, c))
    # [[], [(2, 4), (3, 2), (4, 7)], [(1, 1), (3, 5)], [(1, 2), (4, 4)], [(2, 3)], [], [], [], []]
    dp = dijkstra(start)
    nodes = [i for i in range(1, n + 1)]
    temp = [0]
    for node in nodes:
        if node == start:
            continue
        dp1 = dijkstra(node)[:]
        dp[node] += dp1[start]
    max_v = 0
    for i, v in enumerate(dp[1:]):
        if v > max_v:
            max_v = v

    print(f'#{tc} {max_v}')
