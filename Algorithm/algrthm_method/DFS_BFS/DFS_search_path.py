# 정점의 수와 간선의 수
V, E = map(int, input().split())
# 이차원 배열형태로 (from , to) 받기
arr = list(map(int, input().split()))

# 인접리스트 만들기
adj_arr = list([] for _ in range(V + 1)) # 인덱스와 정점 숫자 맞추기 위해 V+1

for i in range(0, len(arr), 2):
    adj_arr[arr[i]].append(arr[i + 1])
    adj_arr[arr[i + 1]].append(arr[i])
# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

visited = [0 for _ in range(V + 1)]
stack = []

# 탐색하기
def dfs(start):

    print(start, end = ' ')
    visited[start] = 1

    while True:
        for node in adj_arr[start]:
            if not visited[node]:
                stack.append(start)

                start = node
                visited[start] = 1
                print(node,  end=' ')
                break
        else: # 방문하지 않은 곳이 없는 경우
            if len(stack) != 0: # stack이 비어있지 않으면
                start = stack.pop()
            else: # stack이 비어있으면 탐색 종료
                break

dfs(1)