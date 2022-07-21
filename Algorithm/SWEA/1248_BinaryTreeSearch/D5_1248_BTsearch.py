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