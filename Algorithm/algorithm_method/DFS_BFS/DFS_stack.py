# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# [1,2,1,3...]

adj_arr = list([] for _ in range(V + 1)) # [[], [2], [1]
for i in range(0, len(arr), 2):
    adj_arr[arr[i]].append(arr[i + 1])
    adj_arr[arr[i + 1]].append(arr[i])
# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

visited = [0 for _ in range(V + 1)]

def recursive_dfs(v):
    visited[v] = 1

    for node in adj_arr[v]:
        if not visited[node]:
            recursive_dfs(node)

'''
stack = []

def dfs(v):
    visited[v] = 1

    while True:
        for node in adj_arr[v]:
            if not visited[node]:

                stack.append(v)

                v = node # 다음 노드로 최신화

                visited[v] = 1 #
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
'''


