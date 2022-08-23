T = int(input())

def dfs(start):
    global result

    for i in range(4):  # 4 방향에 대해서
        if result == 0 and 0 <= start[0] + dr[i] < N and 0 <= start[1] + dc[i] < N:
            # 다음 방향 찾기
            if maze[start[0] + dr[i]][start[1] + dc[i]] == 0:
                start[0], start[1] = start[0] + dr[i], start[1] + dc[i]
                maze[start[0]][start[1]] = 1  # 지나간 길 흔적남기기
                dfs(start)
                start[0], start[1] = start[0] - dr[i], start[1] - dc[i]

            # 3인 곳 찾으면 탐색 끝
            elif maze[start[0] + dr[i]][start[1] + dc[i]] == 3:
                result = 1
                return

for tc in range(1, T + 1):
    N = int(input())
    maze = list(list(map(int, input())) for _ in range(N))

    # 델타 이동
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 2 자리찾기
    start = [0, 0]
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start[0], start[1] = r, c
                break

    result = 0
    dfs(start)

    print(f'#{tc} {result}')