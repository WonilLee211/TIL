'''
# 1. 완전 탐색
# queue를 통한 구현

graph = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]
N = len(graph) # 마지막 정점


def bfs(root, N):
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
def bfs(v, N, t): # 시작정점, 마지막 정점, 찾는 정점
    
