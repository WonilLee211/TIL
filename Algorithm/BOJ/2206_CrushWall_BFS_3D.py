import sys
sys.stdin = open('input.txt')

from collections import deque
n, m = map(int, input().split())
_map = list(input() for i in range(n))

visited = list([[0] * 2 for _ in range(m)] for _ in range(n))
start = 0, 0,

visited[start[0]][start[1]][0] = 1
c = 0
q = deque()
q.append((start, c))

while q:
    now, c = q.popleft()
    if now[0] == n-1 and now[1] == m-1:
        break

    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next = (now[0] + d[0], now[1] + d[1])

        if not (0 <= next[0] < n and 0 <= next[1] < m) or visited[next[0]][next[1]][c]:
            continue
        # 범위 내에 있고

        if _map[next[0]][next[1]] == '0':
            visited[next[0]][next[1]][c] = visited[now[0]][now[1]][c] + 1
            q.append(((next[0], next[1]), c))

        elif _map[next[0]][next[1]] == '1' and c == 0:
            visited[next[0]][next[1]][1] = visited[now[0]][now[1]][0] + 1
            q.append(((next[0], next[1]), 1))

if visited[n-1][m-1][c] == 0:
    print(-1)
else:
    print(visited[n-1][m-1][c])