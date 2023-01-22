import sys
sys.stdin = open("input.txt")

'''
어느 임의의 지점에서 가장 먼 지점을 찾으면 지름의 한 끝점임을 의미함.
그 지점에서 가장 먼 곳을 찾으면 트리의 지름을 의미한다.




'''



import sys
input = sys.stdin.readline
def dfs(node, weight):
    for next, w in adjList[node]:
        if visited[next] != -1:
            continue
            
        visited[next] = weight + w
        dfs(next, weight + w)

n = int(input())

adjList = [[] for i in range(n + 1)]

for i in range(n - 1):
    p, c, w = map(int, input().split())
    adjList[p].append((c, w))
    adjList[c].append((p, w))

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

end_point = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[end_point] = 0
dfs(end_point, 0)

print(max(visited))
