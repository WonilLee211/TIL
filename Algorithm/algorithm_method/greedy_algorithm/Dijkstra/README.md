# 다익스트라 최단 경로 알고리즘
- 특정 노드에서 출발하여 다른 모든 노드로 가는 최단 경로로 계산
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상 동작
- 그리디 알고리즘의 일부
  - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
- 한번 처리된 노드 최단 거리는 고정됨
  - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것
- 최단 거리 테이블에는 각노드까지 가는 최단 거리 정보가 저장됨

  
## 다양한 문제 상황
- 한 지점에서 다른 한 지점까지의 최단 경로
- 한 지점에서 다른 모든 지접까지의 최단 경로
- 모든 지점에서 다른 모든 지점까지의 최단 경로

## 동작 과정
1. 출발 노드 설정
2. 최단 거리 테이블을 무한대로 초기화
3. 방문하지 않은 노드 중에서 최단 거리를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산
5. 최단 거리 테이블을 갱신
6. 위 과정에서 3번과 4번을 반복
- 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있음
- 처리 과정에서 더 짧은 경로를 찾으면 갱신

## 우선순위 큐
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
  
### heap
- 우선순위 큐를 구현하기 위해서 사용하는 자료구조 중 하나
- 최소 힙
  ```python
    import heapq ad hp

    def heapsort(iterable):
        h = []
        result = []
        for v in iterable:
            hq.heappush(h, v)
        
        for i n range(len(h)):
            result.append(hq.heappop(h))

        return result

    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

- 최대 힙
  ```python
    import heapq ad hp

    def heapsort(iterable):
        h = []
        result = []
        for v in iterable:
            hq.heappush(h, -v)
        
        for i n range(len(h)):
            result.append(-hq.heappop(h))

        return result

    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

## priority queue를 이용한 dijkstra
```python
import heapq as hq
import sys
import sys.stdin.readline
INF =  int(1e9) # 10억

# 노드의 개수, 간선의 개수 입력받기
v, e = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())

# 연결리스트 : 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for in range(v + 1)]
# 최단 거리 테이블을 큰 값으로 설정
dp = [INF for i in range(v + 1)]

# 간선 정보 받아오기
for _ in range(e):
    a, b, w = map(int, input().split())
    # a에서 b로 가는 비용이 w
    graph[a]append((b, w))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정. 큐에 삽입
    hq.heappush(q, (0, start))
    dp[start] = 0

    while q:
        # 가장 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있다면
        if dp[node] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adj in graph[node]:
            # 현재의 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dp[adj[0]] > dp[node] + adj[1]:
                dp[ajd[0]] = dp[node] + adj[1]
                hq.heappush(h, (dp[adj[0]], adj[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한으로 출력
    if dp[i] == INF:
        print('Infinity')
    else:
        print(dq[i])
```