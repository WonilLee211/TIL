import sys, heapq
sys.stdin = open('input.txt')
INF = 1e9
move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
t = int(input())

for tc in range(t):
    n = int(input())
    target = (n - 1, n - 1)
    area = [list(map(int, input().split())) for i in range(n)]

    dp = [[INF] * n for _ in range(n)]
    q = []

    heapq.heappush(q, (area[0][0], 0, 0))
    ans = 0

    while q:
        acc, r, c = heapq.heappop(q)

        if (r, c) == target:
            ans = acc
            break

        for dr, dc in move:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n) or not (0 <= nc < n):
                continue
            if dp[nr][nc] > acc + area[nr][nc]:
                dp[nr][nc] = acc + area[nr][nc]
                heapq.heappush(q, (dp[nr][nc], nr, nc))

    print(ans)

