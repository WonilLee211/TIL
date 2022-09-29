# 서로소 집합 자료구조
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- 교집합이 없는 집합들
- 집합에 속한 하나의 특정 맴버**(대표자, representative)**를 통해 각 집합을 구분함

## 

## -1. 서로소 집합 표현방법

- 연결리스트(pass)
- 트리

## - 2. 서로소 집합 연산

- Make-Set(x)
- Find_Set(x)
  - 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
- Union(x, y)
  - 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
  - y의 대표원소를 x로 바꾸기

## - 3. 상호 베타 집합 표현 - 트리

- 자식 노드가 부모노드를 가리키며 루트 노드가 대표자가 됨

## - 4. 동작과정
- **초기단계**
   -  노드의 개수 크기의 부모 테이블 초기화
      -  노드번호 : 1, 2, 3, 4, 5, 6
      -  부모노드 : 1, 2, 3, 4, 5, 6
- **step 1**
  - union(1, 4)
  - 노드 1과 노드 4의 루트를 각각 찾고 두 루트 중 큰 루트를 작은 루트로 변경
    - 노드번호 : 1, 2, 3, 4, 5, 6
    - 부모노드 : 1, 2, 3, 1, 5, 6
  - union(2, 3), union(2, 4), union(5, 6)
    - 노드번호 : 1, 2, 3, 4, 5, 6
    - 부모노드 : 1, 1, 2, 1, 5, 5
```python
# # 부모 찾기 함수 최적화
# def find_parent(x):
#     if x != parent[x]:
#         x = find_parent(parent[x])
#     return parent[x]

# 루트 노드 찾을 때까지  재귀 호출
def find_parent(x):
    return x if x == parents(x) else find_parents(parent[x])

# 두 원소가 속한 집합을 합치기
def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    parents[a] = b if a > b else parents[b] = a

v, e = map(int, input().split())
parents = [0 for _ in range(v + 1)]

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v +1):
    parents[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 :', end = ' ')
for i in range(1, v + 1):
    print(find_parent(i), end = ' ')

```

## - 5. 기본 구현 방식의 문제점
- 합집합 연산이 편향되게 이루어지는 경우, 찾기 함수가 비효율적으로 동작
    - 최악의 경우 : 모든 노드 확인 O(v)

## - 6. 경로 압축
- 찾기 함수 최적화
  - 찾기 함수 재귀적으로 호출한 뒤 부모 테이블 값 바로 갱신
  - 시간복잡도 개선

```python
def find_parent(x):
    if x != parent[x]:
        x = find_parent(parent[x])
    return parent[x]
```