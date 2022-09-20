import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, 11):
    length, start = map(int, input().split())

    temp = list(map(int, input().split()))
    graph = list([0] for i in range(101))

    for i in range(0, length, 2):
        graph[temp[i]].append(temp[i + 1])

    q = deque()
    visited = [0] * 101
    q.append(start)
    visited[start] = 1
    ans = 0
    while q:
        next = q.popleft()

        if graph[next]:
            for node in graph[next]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = visited[next] + 1
                    flag = visited[node]

    for i in range(100, -1, -1):
        if visited[i] == flag:
            print(f'#{tc} {i}')
            break