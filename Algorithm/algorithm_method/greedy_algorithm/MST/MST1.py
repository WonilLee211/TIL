v, e = map(int, input().split())
adJM = [[0]*(v + 1) for _ in range(v + 1)]
adJL = [[] for i in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adJM[u][v] = w
    adJM[v][v] = w # 가중치가 있는 부방향 그래프
    adJL[u].append((v, w))
    adJL[v].append((v, w))
    
