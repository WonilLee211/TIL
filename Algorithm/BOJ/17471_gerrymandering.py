import sys
sys.stdin = open('input.txt')

'''
모든 조합에 대해서 가능성을 따져야함.
처음 한 집합에 대해서 

N : 구역 개수
두번째 줄 : 구역별 인구수
세번째 줄부터 N개 : 각 구역에 인접한 구역의 수, 인접한 구열 번호

두 개의 구역으로 나누고 각 구열끼리만 연결되어 함
그 중 선거구 인구 차이의 최소값을 출력

논리
- 일딴 두 집단으로 나누는 모든 조합을 구한다.
- 한집단의 크기를 전체 선거구의 반틈만 비교하면 된다. 어차피 중복되기 때문
- bfs로 자기 선거 구 내에 있는 구역만 탐색하면서 선거구 인원을 계산
- 반대편도 탐색
- 두 개의 탐색 결과 합이 전체 노드 개수와 동일하다면 잘 나눠졌다는 것을 의미함
'''
from collections import deque

def bfs(group):
    q = deque([group[0]])
    visited = set([group[0]])
    sub_voters = 0

    while q:
        node = q.popleft()
        sub_voters += voters[node]

        for idx, value in enumerate(board[node]):
            if value and idx not in visited and idx in group:
                visited.add(idx)
                q.append(idx)
    return sub_voters, len(visited)

n = int(input())
voters = list(map(int, input().split()))
result = n * 100

board = [[0] * n for _ in range(n)]
for i in range(n):
    info = list(map(int, input().split()))
    for j in info[1:]:
        board[i][j - 1] = 1

# [[0, 1, 0, 1, 0, 0],
#  [1, 0, 1, 0, 1, 1],
#  [0, 1, 0, 1, 0, 0],
#  [1, 0, 1, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0]]

for i in range(1, 1 << n):
    group_a = set()
    group_b = set(list(range(n)))
    flag = False

    for j in range(n):
        if i & (1<<j):
            group_a.add(j)
            group_b.remove(j)


    if len(group_a) > n//2:
        continue

    a_voters, cnt_a = bfs(list(group_a))
    b_voters, cnt_b = bfs(list(group_b))
    if cnt_a + cnt_b == n:
        result = min(result, abs(a_voters - b_voters))

if result == n * 100:
    print(-1)
else:
    print(result)