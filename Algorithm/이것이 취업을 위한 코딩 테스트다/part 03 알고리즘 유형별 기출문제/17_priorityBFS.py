import sys
sys.stdin = open('input.txt')

'''

논리

- 우선순위큐를 이용
- 큐에 (반복횟수, 바이러스 번호, 위치 정보) 삽입
- 반복횟수가 s보다 커지면 break
- 목적지에 바이러스가 퍼지게 되면 break
- bfs로 순서대로 visited 찍기
    - 범위 내에 있고 방문하지 않았다면 방문하고 큐에 해당 위치 입력
    
'''
import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split()) # n x n 메트릭스, 1 ~ k 바이러스

visited = [] # 시험관
q = []

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    info = list(map(int, input().split()))
    visited.append(info)

    for j in range(n):
        if info[j] != 0:
            heapq.heappush(q, [1, info[j], i, j]) # (반복횟수, 바이러스 번호, 위치 정보)

s, x, y = map(int, input().split())
ans = 0

while q:
    iter, virus, r, c = heapq.heappop(q)

    if iter > s or visited[x-1][y-1] != 0:
        ans = visited[x-1][y-1]
        break

    for m in move:
        n_r, n_c = r + m[0], c + m[1]

        if not (0 <= n_r < n) or not (0 <= n_c < n) or visited[n_r][n_c] != 0:
            continue

        visited[n_r][n_c] = virus
        heapq.heappush(q, [iter + 1, virus, n_r, n_c])

print(ans)