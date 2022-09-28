
def Prim2(r, V):
    MST = [0] * (V + 1)         # MST 포함 여부
    MST[r] = 1                  # 시작정점 표시
    s = 0                       # MST 간선의 가중치 합

    for _ in range(V): # V + 1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (MST[u] == 0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V + 1):  # 
            if MST[i] == 1:
                for j in range(V + 1):
                    if adJM[i][j] > 0 and MST[j] == 0 and minV > adJM[i][j]:
                        u = j
                        minV = adJM[i][j]
        s += minV
        MST[u] = 1              # 정점 u를 MST에 추가    
    return s
    
v, e = map(int, input().split())
adJM = [[0]*(v + 1) for _ in range(v + 1)]
adJL = [[] for i in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adJM[u][v] = w
    adJM[v][v] = w # 가중치가 있는 부방향 그래프

print(Prim2(0, v))