def dfs(i, N, c):
    if c==3:
        return
    else:
        visited[i] = 1
        friend[i] = 1
        for j in range(1, N + 1):
            if adjM[i][j] and visited[j] == 0:
                dfs(j, N, c + 1)
        visited[i] = 0

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adjM = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1

    visited = [0] * (N + 1)
    friend = [0] * (N + 1)
    dfs(1, N, 0)
    print(f'#{tc} {sum(friend) -1}')