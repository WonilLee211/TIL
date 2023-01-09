import sys, collections
sys.stdin = open("input.txt")
deque = collections.deque

n, m = list(map(int, input().split()))
adList = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    a, b = list(map(int, input().split()))
    adList[a].append(b) # a가 b로 갈 수 있는 방향

# 성적 순위를 정확히 알 수 있는 학생
# >> 나보다 큰 노드의 수와 나보다 작은 노드의 수의 합이 n - 1 일 때

cnt_minmax = [[0, 0] for i in range(n + 1)] # 나보다 작은 노드의 수, 나보다 큰 노드의 수

for i in range(1, n + 1):
    visited = []

    for bigger in adList[i]:
        if bigger in visited:
            continue

        visited.append(bigger)
        q = deque()
        q.append((bigger, i)) # 나보다 큰 노드, 시작점
        cnt_minmax[i][1] += 1
        cnt_minmax[bigger][0] += 1

        while q: # bfs 그래프 탐색
            now, origin = q.popleft()

            for bigger1 in adList[now]:
                if bigger1 not in visited:
                    visited.append(bigger1)
                    q.append((bigger1, origin))
                    cnt_minmax[i][1] += 1
                    cnt_minmax[bigger1][0] += 1

ans = 0
for minmax in cnt_minmax:
    ans += 1 if sum(minmax) == n - 1 else 0

print(ans)