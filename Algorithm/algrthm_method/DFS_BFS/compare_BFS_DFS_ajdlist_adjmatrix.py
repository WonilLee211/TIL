
#인접행렬+stack
def dfs_matrix_with_stack(matrix, i, visited):
    stack=[i]                                               #탐색 시작할 정점 넣기

    while stack:
        value = stack.pop()                                 #방문하는 노드

        if not visited[value]:                              #아직 방문을 안했다면
            print(value, end=' ')
            visited[value] = True                           #방문했음을 표시

        for c in range(len(matrix[value])-1, -1, -1):       #문제에서 작은 숫자부터 입력하기를 요구하기 때문에 반대로 순회
            if matrix[value][c] == 1 and not visited[c]:    #연결되어있고 아직 가지 않은 노드라면
                stack.append(c)                             #후에 방문할 예정임을 스택에 추가

n, m, v = map(int, input().split())                         #정점의 개수, 간선의 개수, 탐색을 시작할 정점
                                                            #노드의 인덱스가 1부터 시작하기 때문에 n+1을 해줌
matrix = [[0]*(n+1) for _ in range(n+1)]                    #인접행렬리스트
visited = [False]*(n+1)                                     #각 노드에 방문한 적 있는지 확인

for _ in range(m):                                          #인접행렬리스트에 각 노드 표시
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

dfs_matrix_with_stack(matrix, v, visited)


'''
#인접행렬+재귀함수
#재귀함수를 사용하면 앞선 프로세스가 스택으로 쌓이는 형태가 되기 때문에 스택을 직접 사용하지 않아도 됩니다
def dfs_matrix_with_recursive(matrix, i, visited):
    visited[i] = True                                           #갔다온 노드 표시
    print(i, end=' ')

    for c in range(len(matrix[i])):
        if matrix[i][c]==1 and not visited[c]:                  #연결되어 있고 아직 방문하지 않은 노드라면
            dfs_matrix_with_recursive(matrix, c, visited)       #갔다오도록 합시다

n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]                        #인접행렬
visited = [False]*(n+1)                                         #갔다옴을 표시할 배열

for _ in range(m):                                              #인접행렬에 값 표시
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

dfs_matrix_with_recursive(matrix, v, visited)
'''

'''
#인접리스트+stack
def dfs_list_with_stack(graph, i, visited):
    stack = [i]
    visited[i] == True

    while stack:
        value = stack.pop()

        if not visited[value]:
            print(value, end=' ')
            visited[value] = True

        for j in graph[value]:
            if not visited[j]:
                stack.append(j)

n, m, v = map(int, input().split())
graph = [[]]*(n+1)
visited = [False]*(n+1)

for _ in range(m):                      #인접리스트 형성
    f, t = map(int, input().split())
    if graph[f] == [] : graph[f] = [t]
    else : graph[f].append(t)

    if graph[t] == [] : graph[t] = [f]
    else : graph[t].append(f)

for i in graph : i.reverse()            #문제에서 작은 숫자부터 입력하기를 요구하기 때문

dfs_list_with_stack(graph, v, visited)
'''

'''
#인접리스트+재귀함수
def dfs_list_with_recursive(graph, i, visited):
  visited[i] = True
  print(i, end=' ')
  for j in graph[i]:                                #노드 리스트 받아오기
    if not visited[j]:                              #아직 방문하지 않았다면
      dfs_list_with_recursive(graph, j, visited)    #돌아봅시다

n, m, v = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  if graph[f] == []:
    graph[f] = [t]
  else:
    graph[f].append(t)
  if graph[t] == []:
    graph[t] = [f]
  else:
    graph[t].append(f)

dfs_list_with_recursive(graph, v, visited)
'''

'''
#인접행렬+queue
from collections import deque                                   #BFS니까 queue 써주기

def bfs_matrix(matrix, i, visited):
    queue = deque()
    queue.append(i)                                             #갈 곳 추가

    while queue:
        value = queue.popleft()                                 #방문하는 노드

        if not visited[value]:                                  #아직 방문 전이라고 한다면
            print(value, end=' ')                               #이제 방문할 예정이기 때문에 출력해주고
            visited[value] = True                               #방문했다고 표시해줍시다

            for c in range(len(matrix[value])):                 #방문하는 노드의 리스트를 가져와서 연결된 리스트 둘러보기
                if matrix[value][c] == 1 and not visited[c]:    #아직 방문 전 노드가 리스트에 있다면
                    queue.append(c)                             #곧 방문하기 위해 큐에 추가해줍시다

                                                                #이렇게 들어온 큐 값은 선입선출 구조이니 2부터 출력
                                                                #DFS와 들어가는 값은 똑같지만, stack과 queue의 특성이 달라 서로 방문하는 노드 순서가 달라짐

n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

bfs_matrix(matrix, v, visited)
'''

'''
from collections import deque

def bfs_list(graph, i, visited):
    queue = deque()
    queue.append(i)                                     #방문할 첫번째 노드

    while queue:
        value = queue.popleft()                         #방문할 노드 꺼내기

        if not visited[value]:                          #아직 방문하지 않은 상황이면
            print(value, end=' ')

            visited[value] = True                       #방문했다고 해주기

            for j in graph[value]: queue.append(j)      #차례대로 인접 노드 추가해주기

n, m, v = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  if not graph[f]: graph[f] = [t]
  else: graph[f].append(t)
  if not graph[t]: graph[t] = [f]
  else: graph[t].append(f)

bfs_list(graph,v, visited)
'''