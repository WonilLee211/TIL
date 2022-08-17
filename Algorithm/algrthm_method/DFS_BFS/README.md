# 깊이 우선 탐색과 너비 우선 탐색

## 1. 깊이 우선 탐색(DFS)

- 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘

- 예> 미로 길찾기에서 한방향으로 끝까지 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 다른 방향으로 탐색 진행

- ### 1.1 특징

- 후입선출(가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하기 때문)

- 모든 노드를 방문하고자 할 때 사용

- 깊이 우선 탐색이 너비 우선 탐색보다 좀 더 간단함

- 검색 속도 자체는 너비 우선 탐색에 비해 느림

- 시간복잡도 : O(n)
  
  ![Alt text](../../img/DFS.gif)
  
  <h6>출처 : https://devuna.tistory.com/32</h6>

### 1.2 장점 & 단점

- 장점
  - 현 경로상의 노드를 기억하기 때문에 적은 메모리 사용
  - 찾으려는 노드가 깊은 단계에 있는 경우 BFS보다 빠름
- 단점
  - 해가 없는 경로를 탐색할 경우 완전 탐색하게 됨
  - 최단 경로를 구하는 문제에서 찾은 해가 최단 경로라는 보장 없음

### 1.3 구현 방법

- 스택
- 재귀함수

### 1.4 DFS 구현

- 재귀함수
- ```python
  # 재귀 사용
  graph = {
          0:[1, 2], 1:[0, 3, 4], 2:[0, 4],
           3:[1, 5], 4:[1, 2, 5], 5:[3, 4, 6], 6:[5],
      }
  
  visited = [False] * len(graph)
  
  def DFS(v):
      visited[v] = True
      print(v, end = ' ')
  
      for node in graph[v]:
          if not visited[node]:
              DFS(node)
        
  DFS(0) # 0 1 3 5 4 2 6
  ```
  
  
  - 줄기별로 막다른 곳까지 갔을 때 탐색 경로 출력

```python
graph = [[], [2, 3], [4], [4, 5 ,6], [8], [], [9],[], [10, 11], [], [], []]

visited = [0 for _ in range(len(graph))]

def dfs(graph, start, visited):
  # 방문기록 남기기
  visited[start] = start

  if not graph[start]: # 막다른 길일 때
    print(visited)

  for node in graph[start]:
    if not visited[node]: # 방문이력이 없을 때
      dfs(graph, node, visited) # 
      visited[node] = 0

dfs(graph, 1, visited)

#[0, 1, 2, 0, 4, 0, 0, 0, 8, 0, 10, 0]
#[0, 1, 2, 0, 4, 0, 0, 0, 8, 0, 0, 11]
#[0, 1, 0, 3, 4, 0, 0, 0, 8, 0, 10, 0]
#[0, 1, 0, 3, 4, 0, 0, 0, 8, 0, 0, 11]
#[0, 1, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0]
#[0, 1, 0, 3, 0, 0, 6, 0, 0, 9, 0, 0]
```

- 스택을 통한 구현
- ```python
  # 스택 사용
  graph = {
          0:[1, 2], 1:[0, 3, 4], 2:[0, 4],
           3:[1, 5], 4:[1, 2, 5], 5:[3, 4, 6], 6:[5],
      }
  
  def DFS(v):
      visited = [0] * len(graph)
      stack = [0] * len(graph)
      top = -1
      
      top += 1
      visited[v] = 1
      print(v)
  
      while True:
          for w in graph[v]:# v의 인접 정점 중 방문안한 w가 있으면
              if not visited[w]:
                  top += 1
                  stack[top] = v
                  v = w
                  visited[w] = 1
                  print(v)
                  break
          else: # w가 없으면
              if top != -1: # 스택이 비어 있지 않으면
                  v = stack[top]
                  top -= 1
              else: # 스택이 비어있으면
                  break
  
  
  DFS(0) # 0 1 3 5 4 2 6
  ```
- ```python
  
  # 탐색하기
  def dfs(v):
  
      print(v, end = ' ')
      visited[v] = 1
  
      while True:
          for node in adj_arr[v]:
              if not visited[node]:
                  stack.append(v)
  
                  v = node
                  visited[v] = 1
                  print(node,  end=' ')
                  break
          else:
              if stack:
                  v = stack.pop()
              else:
                  break
  
  dfs(1)
  ```

```python
graph = [[], [2, 3], [4], [4, 5 ,6], [8], [], [9],[], [10, 11], [], [], []]

def dfs_stack(graph, node):
  visited = []
  stack = [node]

  while stack:
    n = stack.pop()

    if n not in visited:
      visited.append(n)
      stack.extend(graph[n])

  return visited

print(dfs_stack(graph, 1))

# [1, 3, 6, 9, 5, 4, 8, 11, 10, 2]
```

### 1.4 DFS 활용할만한 문제 유형

1. 모든 정점을 방문하는 것이 주요한 문제
2. 경로의 특징을 저장해둬야 하는 문제
3. 검색 대상 그래프가 정말 큰 문제

---

## 2. 너비 우선 탐색(BFS, breath first search)

- 현재 정점에 연결된 가까운 노드부터 탐색하는 알고리즘
- queue자료 구조로 자연스레 가까운 노드부터 탐색하도록 진행
- 두 노드 사이의 최단 경로를 찾고 싶을 때 사용
- 예> 지구상에 존재하는 모든 친구 관계를 그래프로 표현한 뒤, sam과 eddle 사이에 존재하는 경우
  - sam과 가까운 관계부터 탐색

### 2.1 특징

- 선입선출

- 시간복잡도 : O(n)

- 실제 수행시간은 DFS보다 좋은 편
  
  ![Alt text](../../img/BFS.gif)
  
  <h6>출처 : https://devuna.tistory.com/32</h6>

### 2.2 장점 & 단점

- 장점
  - 답이 되는 경로가 여러 개인 경우에도 최단경로임을 보장
  - 최단 경로가 존재하면 깊이가 무한정 깊어진다고 해도 답을 찾을 수 있음
- 단점
  - 경로가 매우 길 경우 탐색 가지가 급격히 증가>> 기억공간이 증가함
  - 해가 존재하지 않으면 유한 그래프의 경우 모든 그래프를 탐색하고 실패로 끝남
  - 무한 그래프는 해를 못찾고 끝내지도 못함

### 2.3 구현 방법

- 큐와 재귀함수를 이용
- 큐를 이용한 구현
  
  ```python
  graph = [[], [2, 3], [4], [4, 5 ,6], [8], [], [9],[], [10, 11], [], [], []]
  ```

from collections import deque

def bfs(graph, root):
  visited = []
  queue = deque([root])

  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.append(node)
      queue += graph[node]

  return visited

print(bfs(graph, 1))

# [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]

```
- 재귀함수를 이용한 구현
```python
graph = [[], [2, 3], [4], [4, 5 ,6], [8], [], [9],[], [10, 11], [], [], []]

from collections import deque

def recursive_bfs(graph, queue, visited):
  if not queue:
    return

  node = queue.popleft()

  for n in graph[node]:
    if n not in visited:
      visited.append(n)
      queue.append(n)

  recursive_bfs(graph, queue, visited)

queue = deque([1])
visited = []

recursive_bfs(graph, queue, visited)

print(visited)

# [2, 3, 4, 5, 6, 8, 9, 10, 11]
```

### 2.4 BFS 활용할만한 문제 유형

1. 그래프의 모든 정점을 방문하는 것이 주요한 문제
2. 최단거리를 구해야 하는 문제
3. 검색 대상의 규모가 크지않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않을 때

---
