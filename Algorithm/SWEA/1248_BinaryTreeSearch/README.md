# SWEA D5 1248 공통 조상

## 문제
이진트리에서 임의의 두 정점의 공통 조상 중 가장 가까운 정점을 찾기.
---
## 입력
- 첫번째 줄 : 테스트 수
- 테스트 케이스 첫번째 줄 : 트리의 정점의 총 수, 간선의 총 수, 공통 조상을 찾는 두가지 정점 번호
- 테스트 케이스 두번째 줄 : 부모-자식순의 간선
---
## 출력
- "#(testcase) (가장 가까운 공통조상 정점) (정점의 서브루트 크기)" 형태
---
## 제약
- 정점의 크기는 부모 자식 관계와 무관
- 주어지는 두 정점이 서로 조상과 손자인 관계인 경우는 없다.
---
## 알고리즘
1. 이진트리 데이터를 딕셔너리 형태로 저장
   graph = {부모1:[자식,...],...}
2. graph 내에 value가 빈 요소를 삭제
3. 탐색 시작 두 지점에 대해서
    1. 이미 방문했다면 그 지점이 정답(공통조상)
    2. 아니라면
        1. 현재 지역을 방문지역에 기록
        2. 다음 방문 지역 결정
            1. 현재 지역의 노드 번호를 value로 가지고 있는 key를 다음 노드로 결정
    3. 다음 방문지역 최신화
    4. 3.으로 돌아가기


4. 공동 조상에서 하위 노드 갯수 세기
    1. 첫 지점(공통조상)이 첫 방문 지역
    2. 방문 지역별로 graph에 value값이 있다면
        1. 그 수 만큼 cnt
        2. 그 value들을 다음 방문 지역으로 등록
    3. 다음 방문 지역을 현재 방문 지역으로 업데이트
    4. 1로 돌아가기
    5. 방문 지역이 없을 때까지 반복

```python
t = int(input())

for tc in range(1,t+1):
    v, e, node_a, node_b = map(int,input().split())
    data = list(map(int,input().split()))

    # 이진트리 데이터를 딕셔너리 형태로 저장({부모1:[자식,..], ...} 형태)
    graph = {key:[] for key in range(1,v+1)}
    for i in range(0,2*e-1,2):
        graph[data[i]].append(data[i+1])

    keys = list(graph.keys())

    # graph 안에 value가 비어있는 요소 삭제
    for key in keys:
        if not len(graph[key]):
            del graph[key]
    
    graph_cnt = graph
    visited = []
    nextnodelist = [node_a,node_b]
    
    answer = 1

    # 그래프 공동 조상 찾기
    while nextnodelist:
        
        tempnodelist = [] # nextnodelist를 업데이트하기 위한 저장장소
        
        for node in nextnodelist: # 두 노드에 대해서
            for key in graph.keys(): 
                if node in graph[key]: # 어떤 key의 value안에 있다면(자식 정점이라면)
                    if node in visited: # 해당 노드가 이미 방문되었다면
                        answer = node   # 이 노드가 공동 조상(다른 하나의 노드에서 이미 방문했기 때문)
                        break
                    else:tempnodelist.append(key) # 방문된 적 없다면, 다음 방문할 노드로 입력
            visited.append(node) # 방문기록 남기기

        nextnodelist = tempnodelist

    # 공동조사상에서 하위 노드 세기
    cnt = 1
    nodelist = [answer]

    while nodelist: 
        nextnodes = []  # nodelist를 업데이트할 저장장소
        
        for node in nodelist:   # 방문해야할 노드에 대해서

            if node in list(graph.keys()): # node가 key리스트에 포함된다면
                cnt += len(graph[node]) # 해당 노드의 하위 노드 수 더하기

                for i in range(len(graph[node])):   # 해당 노드는 다음 방문할 리스트에 저장
                    nextnodes.append(graph[node][i])

        nodelist = nextnodes

    print(f"#{tc} {answer} {cnt}")
```