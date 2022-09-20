import sys
sys.stdin = open('input.txt')
'''
# 1. 완전 탐색
# queue를 통한 구현

graph = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]
N = len(graph) # 마지막 정점


def bfs(root, N): # 시작 정점, 마지막 정점번호
    visited = [0] * (N + 1)
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        
        for next in graph[node]:
            if visited[next] == 0:
                visited[next] = visited[node] + 1 # 경로의 길이 저장
                queue.append(next)

bfs(0, len(graph))
# 0 1 2 3 4 5 6 [1, 2, 2, 3, 3, 4, 5, 0]
'''

'''
# 1219 길찾기 문제 시작점 0, 목적지 99 찾기

def bfs(v, N, t): # 시작정점, 마지막 정점, 찾는 정점
    visited = [0 for _ in range(100)]
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.pop(0)

        if v == t: # 목표 정점 발견 시 경로의 총 길이 반환(본 문제는 1 출력)
            return visited[t] # 1

        for next_v in range(v):
            if visited[next_v] == 0:
                queue.append(next_v)
                visited[next_v] = visited[v] + 1

    return 0

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjlist = [[] for _ in range(100)]

    for i in range(E):
        a, b = arr[i*2], arr[i * 2 + 1]
        adjlist[a].append(b) # 단방향

    bfs(0, 99, 99)
'''

'''
# 4875 미로 출발지에서 목적지에 도착하는 경로 존재하는지 확인하는 문제

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j] # 최단 거리

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return -1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = stj = -1

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    print(f'#{tc} {bfs(sti, stj, N)}')
'''
'''
# 4875 미로 출발지에서 목적지에 도착하는 경로 존재하는지 확인하는 문제
# dfs로 경로의 수 세기

def dfs(i, j, N):
    global cnt
    if maze[i][j] == 3:
        cnt += 1
        return # 의미가 있나?

    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni, nj, N)
        visited[i][j] = 0
        return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = stj = -1

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    cnt = 0
    visited = [[0]*N for i in range(N)]
    dfs(sti, stj, N)

    print(f'#{tc} {cnt}')
'''
'''
# 4875 미로 출발지에서 목적지에 도착하는 경로 존재하는지 확인하는 문제
# dfs로 최단거리 찾기.

def dfs(i, j, s, N):
    global minV

    if maze[i][j] == 3:
        if minV > s + 1:
            minV = s + 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni, nj, s+1, N)
        visited[i][j] = 0 # 다른 경로로 현 위치로 왔을 땐 탐색할 수 있도록 함. 가능한 모든 경로를 볼 수 있도록 함
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    minV = N**2
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    dfs(sti, stj, 0, N)
    if minV == N**2:
        minV = -1
    print(f'#{tc} {minV}')
'''
'''
여러 출발지점에서 퍼져나가서 모든 공간을 채우는 데 걸리는 시간 세기

'''
def bfs(N):
    global max_cnt
    visited = [[0] * N for _ in range(N)]

    q = []

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1

    while q:
        i, j = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if max_cnt < visited[ni][nj]:
                    max_cnt = visited[ni][nj]
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    max_cnt = 0
    bfs(N)
    print(f'#{tc} {max_cnt}')