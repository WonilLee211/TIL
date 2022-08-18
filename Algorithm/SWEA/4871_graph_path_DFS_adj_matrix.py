def dfs(start, stop, V):
    visited[start] = 1

    if visited[stop]:
        return

        

def dfs(start, stop, V):
    visited[start] = 1

    if visited[stop]:  # 도중에 찾으면 탐색 중단
        return

    for i in range(V + 1):
        if adj_matrix[start][i] and not visited[i]:
            dfs(i, stop, V)


T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())

    # 인접행렬 사용
    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

    # 단방향 정보 저장
    for _ in range(E):
        frm, to = map(int, input().split())
        adj_matrix[frm][to] = 1

    visited = [0 for i in range(V + 1)]
    start, stop = map(int, input().split())

    result = 0

    dfs(start, stop, V)

    if visited[stop]:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')