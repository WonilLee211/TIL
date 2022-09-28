import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        num = q.popleft()
        if visited[m] < visited[num]:
            break

        for i in range(4):
            if i == 2:
                next = num * 2
            else:
                next = num + op[i]

            if 0 <= next <= 1000000:
                if not visited[next]:
                    visited[next] = visited[num] + 1
                    q.append(next)
                else:
                    if visited[next] > visited[num] + 1:
                        visited[next] = visited[num] + 1
                        q.append(next)

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    op = [1, -1, 2, -10]
    visited = [0] * 1000001
    visited[m] = 1000000
    bfs()
    print(f'#{tc} {visited[m]}')