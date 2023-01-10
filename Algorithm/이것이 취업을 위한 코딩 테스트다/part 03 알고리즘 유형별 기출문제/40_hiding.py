import sys, heapq
sys.stdin = open('input.txt')
INF = 1e10
n, m = map(int, input().split())
path = [[] for i in range(n + 1)]

for i in range(m):
    fr, to = map(int, input().split())
    path[fr].append(to)
    path[to].append(fr)

dp = [INF] * (n + 1)
dp[1] = 0
q = []
heapq.heappush(q, (0, 1)) # distance, start

while q:
    distance, fr = heapq.heappop(q)

    for to in path[fr]:

        if dp[to] > distance + 1:
            dp[to] = distance + 1
            heapq.heappush(q, (dp[to], to))

max_v = max(dp[1:])
ans = [dp.index(max_v), max_v, dp.count(max_v)]
print(*ans)