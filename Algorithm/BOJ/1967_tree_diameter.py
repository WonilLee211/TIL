import sys
sys.stdin = open("input.txt")

'''
어느 임의의 지점에서 가장 먼 지점을 찾으면 지름의 한 끝점임을 의미함.
그 지점에서 가장 먼 곳을 찾으면 트리의 지름을 의미한다.




'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(node, weight):
    global max_value, end_point
    if weight > max_value:
        max_value, end_point = weight, node

    visited[node] = 1

    for next, w in adjList[node]:
        if visited[next]:
           continue

        dfs(next, weight + w)

n = int(input())

adjList = [[] for i in range(n + 1)]

for i in range(n - 1):
    p, c, w = map(int, input().split())
    adjList[p].append((c, w))
    adjList[c].append((p, w))


max_value, end_point = 0, 0
visited = [0] * (n + 1)
dfs(1, 0)

visited = [0] * (n + 1)
dfs(end_point, 0)


print(max_value)