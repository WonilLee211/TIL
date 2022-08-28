import sys
sys.stdin = open('input.txt')
# 완전 탐색을 통한 최소 거리 구하기
def dfs(arr, starts, cores, length):
    global max_core
    global min_length

    if len(starts) == 0: # 모든 시작점을 돌았을 때
        if cores > max_core: # 연결된 코어가 더 많을 때 최신화
            max_core = cores
            min_length = length
        elif cores == max_core: # 코어 수가 같으면 길이가 짧은 것으로 저장
            if length < min_length:
                min_length = length
        return

    start = starts[0]
    # 벽에 붙어있는 core에 대해 처리
    if start[0] in [0, n-1] or start[1] in [0, n-1]:
        dfs(arr, starts[1:], cores + 1, length)
    else: # 모든 방향에 대해 탐색
        for d in [[0,1], [1, 0], [0, -1], [-1, 0]]:
            next = start[:]
            while  0 <= next[0] + d[0] < n and 0 <= next[1] + d[1] < n and maxinos[next[0] + d[0]][next[1] + d[1]] == 0:
                next = [next[0] + d[0], next[1] + d[1]]
                # 끝까지 갓을 때 거리 계산
                if next[0] in [0, n-1] or next[1] in [0, n-1]:
                    diff = abs(next[0] - start[0]) + abs(next[1] - start[1])
                    # 지나온 거리 표시
                    while 0 <= next[0] - d[0] < n and 0 <= next[1] - d[1] < n and arr[next[0]][next[1]] != 1:
                        arr[next[0]][next[1]] = 2
                        next[0], next[1] = next[0] - d[0], next[1] - d[1]
                    # 다음 길로 가기
                    dfs(arr, starts[1:], cores + 1, length + diff)
                    # 표시한 거리 지우기
                    while 0 <= next[0] + d[0] < n and 0 <= next[1] + d[1] < n:
                        next[0], next[1] = next[0] + d[0], next[1] + d[1]
                        arr[next[0]][next[1]] = 0

        else: # 모든 방향에 대해 연결할 곳이 없을 때 다음 위치로 이동
            dfs(arr, starts[1:], cores, length)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maxinos = list(list(map(int, input().split())) for i in range(n))

    core_idx = []
    for i in range(n):
        for j in range(n):
            if maxinos[i][j] == 1:
                core_idx.append([i,j])

    max_core = 0
    min_length = 0

    dfs(maxinos, core_idx, 0, 0)

    print(f'#{tc} {min_length}')
