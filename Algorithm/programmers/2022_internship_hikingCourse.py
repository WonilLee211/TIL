'''
n : 지점의 수 1 ~ n 출입구, 쉽터 혹은 산봉우리
양방향 등산로
path = 등산로 정보 [i,j,w]
- i와 j를 연결하는 w 걸리는 시간
intensity : 휴식없이 이동해야 하는 시간
summits : 산봉우리 번호들
gates : 출입구 번호

출입구 중 한 곳에서 출발해서 산봉오리 중  한 곳만 방문한 뒤 다시 원래의 출구로 돌아오는 등산코스
- 출입구는 처음과 끝에, 봉우리는 한번만 포함되어야 함
이러한 규칙을 지키멶서 intensity가 최소가 되는 코스 정하기

[산봉우리 번호, intensity] 출력

논리 - 오답
- 봉우리에서 입구까지 가는데 가장 작은 indensity로 가는 길
- bfs 탐색
- 백트래킹 : 현재 구한 indensity보다 크면 버리기
- 모든 봉우리에서 탐색 시작
- 봉우리가 있거나 방문했으면 pass
- 입구에 도착했으면 indensity 확인
오답

dp로 풀어야 할듯
논리
- 봉우리별로 탐색
- 연결된 노드로 가는 최소 indensity 저장
- 봉우리에서 해당 노드까지 가는데 가장 작은 indensity  dp에 저장
- 출입구별로  봉우리 번호, indensity 저장
- 출입구에 도착했을 때 indensity가 작다면 갱신
    - 이때 indensity가 같다면 작은 봉우리 번호로 저장

몇개는 시간초과  한개 틀림
우선순위큐를 써야할듯
- ans 초기값 설정에서 봉우리초기값을 50000으로 했어야 함
- 3개 시간초과

'''

import heapq

n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3, 7]
summits = [1, 5]


summits.sort()
link = [[] for i in range(n + 1)]
for path in paths:
    link[path[0]].append([path[1], path[2]])
    link[path[1]].append([path[0], path[2]])

ans = [1, 10000000]  # 봉우리와 indensity 저장

dp = [10000000] * (n + 1)
q = []

for gate in gates:
    dp[gate] = 0
    heapq.heappush(q, [0, gate])

while q:
    [max_ind, node] = heapq.heappop(q)

    if node in summits or max_ind > dp[node]:
        continue

    for next in link[node]:
        now_w = max(next[1], max_ind)

        if dp[next[0]] > now_w:
            dp[next[0]] = now_w
            heapq.heappush(q, [dp[next[0]], next[0]])

for summit in summits:

    if dp[summit] < ans[1]:
        ans = [summit, dp[summit]]

print(ans)

'''
for summit in summits:

    dp = [10000000 for i in range(n + 1)]
    node = summit
    dp[node] = 0
    q = deque([node])
    inden = 10000000
    while q:
        node = q.popleft()

        if dp[node] >= inden:
            continue

        if node in gates:
            if inden > dp[node]:
                inden = dp[node]
            continue

        for next in link[node]:
            if next[0] in summits:
                continue

            now_w = max(next[1], dp[node])

            if now_w >= inden:
                continue

            if dp[next[0]] > now_w:
                dp[next[0]] = now_w
                q.append(next[0])

    if inden < ans[1]:
        ans = [summit, inden]
    elif inden == ans[1]:
        ans[0] = min(ans[0], summit)

print(ans)
'''

'''
[[],
[[2, 3]], 
[[1, 3], [3, 5], [4, 2], [5, 4]],
[[2, 5], [4, 4]],
[[2, 2], [3, 4], [5, 3], [6, 1]], 
[[2, 4], [4, 3], [6, 1]], [[4, 1], [5, 1]]]
'''

'''
for summit in summits:                                              # 봉우리마다 탐색
    sub_indensity = 10000000                                        # 초기 indensity
    q = deque([[summit, 0, 1 << summit]])                             # 시작점, indensity, 방문 지점

    while q:
        [node, inden, visited] = q.popleft()

        if inden > sub_indensity:                                   # 현재 구한 indensity보다 크면 버리기
            continue

        if node in gates:
            if inden < sub_indensity:                 # 출구에 도착했고 inden이 작으면 갱신
                sub_indensity = inden
            continue

        for next in link[node]:
            if visited & (1 << next[0]) or next[0] in summits:
                continue

            now_inden = max(inden, next[1])
            if now_inden > sub_indensity:
                continue
            # 나아간 노드, indensity 큰 값, 방문 표시
            q.append([next[0], now_inden, visited ^ (1 << next[0])])

    if ans[1] > sub_indensity:
        ans = [summit, sub_indensity]
    elif ans[1] == sub_indensity:
        ans[0] = min(ans[0], summit)

print(ans)
'''