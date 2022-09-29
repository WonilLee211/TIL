import sys
sys.stdin = open('input.txt')

import heapq

for tc in range(1, int(input()) + 1):
    n, e = map(int, input().split())            # 노드번호, 간선 수
    LkL = [[] for i in range(n + 1)]            # 몇 개가 연결되어있는지 모르니까 연결리스트

    total = 0
    for i in range(e):                          # 간선 정보 저장
        s, e, w = map(int, input().split())
        total += w
        LkL[s].append((e, w))
    # [[(1, 1), (2, 6)], [(2, 1)], []]

    h = []
    heapq.heappush(h, (0, 0))
    visited = [0 for i in range(n + 1)]
    dp = [10 * (n**2) for i in range(n + 1)]
    dp[0] = 0
    while h:

        MinD, idx = heapq.heappop(h)
        if visited[idx] == 0:
            visited[idx] = 1                # 가중치가 가장 작은 값을 먼저 봤기 때문에 한번 거친 노드는 고정

            for node in LkL[idx]:           # 갈 수 있는 노드에 대해서
                if dp[node[0]] > MinD + node[1]: # DP
                    dp[node[0]] = MinD + node[1]
                    heapq.heappush(h, (dp[node[0]], node[0]))

    print(f'#{tc} {dp[-1]}')
