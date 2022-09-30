import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while x != rep[x]:  # 대표원소가 아니면
        x = rep[x]   # x가 가리키는 정점으로 이동
    return x

V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w,u,v))
edge.sort()  # 가중치 기준 오름차순 정렬
rep = [i for i in range(V+1)]  # 대표원소 초기화
# N개의 정점이 있으면 사이클이 생기지 않도록 N-1개의 간선을 선택
# MST에 포함된 간선의 가중치의 합 구하기
N = V+1  # 0~V번 까지의 정점
cnt = 0
total = 0  # 가중치의 합
for w, u, v in edge:  # N-1개의 간선 선택 루프
    if find_set(u) != find_set(v):  # 사이클을 형성하지 않으면 선택
        cnt += 1
        total += w  # 가중치의 합
        # union(u, v) 와 동일
        rep[find_set(v)] = find_set(u)  # v의 대표원소를 u의 대표원소로 바꿈
        if cnt == N-1:
            break
print(total)

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