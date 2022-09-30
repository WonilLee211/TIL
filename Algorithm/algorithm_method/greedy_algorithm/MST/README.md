# 최소 신장 트리(MST)
- 
## 1. 그래프에서 최소비용문제

1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
2. 두 정점 사이의 최소 비용의 경로 찾기

## 2. 신장 트리

- n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과n-1개의 간선으로 이루어진 트리
- 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
  
## 3. 최소 신장 트리(Minimum Spanning Tree)

- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

## 4. 크루스칼 알고리즘
- 대표적인 최소 신장 트리 알고리즘
- 그리디 알고리즘의 일종

### 동작과정
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 아직 처리하지 않는 간선중 가장 짧은 간선 선택
3. 
4. 간선을 하나씩 확인하면서 현재의 간선이 사이클을 발생시키는지 확인
   1. 사이클이 발생하는경우 최소신장트리에 제외
   2. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
5. 모든 간선에 대해 2번의 과정을 반복

```python

# 특정 원소가 속한 집합을 찾기
def find_parents(x):
    # 루트 노드가 아니라면 투트 노드를 찾을 때까지 재귀적으로 호출
    while x != parents[x]:
        x = parents[x]
    return x

# 두 원소가 속한 집합 합치기
def union(x, y):
    a = find_parents(x)
    b = find_parents(y)
    if b > a:
        parents[b] = a
    else:
        parents[a] = b

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parents = [0 for _ in range(1, v + 1)]


# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parents[i] = i

# 모든 간선에 대한 정보 담기
# 가중치를 기준으로 정렬하기 위해 첫번째 원소를 가중치로 이동
edges = []
for i in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))
edges.sort()

# 간선을 하나씩 확인하며 
for edge in edges:
    w, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parents[a] != find_parents[b]:
        union(a, b)
        res += w

print(res)
```



## 4. prim 알고리즘
- 

### 동작과정
1. 

```python

def prim1(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    key = [10000]*(V+1) # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0          # 시작정점의 key
    for _ in range(V):  # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i]==0 and key[i]<minV:
                u = i
                minV = key[i]
        MST[u] = 1                  # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])     # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)         # MST 가중치의 합

def prim2(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):    # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
            if MST[i]==1:
                for j in range(V+1):
                    if adjM[i][j]>0 and MST[j]==0 and minV>adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s

V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프
    adjL[u].append((v, w))
    adjL[v].append((u, w))
print(adjM)
print(adjL)
#print(prim1(0, V))
print(prim2(0, V))
```