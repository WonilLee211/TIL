
def Prim1(r, V):
    MST = [0] * (V + 1)         # MST 포함 여부
    key = [10000] * (V + 1)     # 가중치의 최대값 이상으로 초기화. key[v]는 MST에 속한 정점과 연결
    key[r] = 0                  # 시작정점의 key
    for _ in range(V): # V + 1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (MST[u] == 0), key가 최소인 u 찾기
        u = 0
        minV = 10000

        for i in range(V + 1):      # v + 1개의
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1              # 정점 u를 MST에 추가    

        # u에 인접인 v에 대해, MST에 포함되지 앟은 정점이면
        for v in range(V + 1):
            if MST[v] == 0 and adJM[u][v] > 0:
                key[v] = min(key[v], adJM[u][v]) # u를 통해 MST에 포함되는 비용과 기존 비용 중 최소 값 
    return sum(key)             # MST 가중치의 합

v, e = map(int, input().split())
adJM = [[0]*(v + 1) for _ in range(v + 1)]
adJL = [[] for i in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adJM[u][v] = w
    adJM[v][v] = w # 가중치가 있는 부방향 그래프

print(Prim1(0, v))
