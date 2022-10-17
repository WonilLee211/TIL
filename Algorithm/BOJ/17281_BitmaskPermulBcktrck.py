'''
팀당 9명의 두 팀이 공격과 수비를 번갈아하는 게임
n 이닝 동안 게임을 진행
한 이닝에 3아웃이 발생하면 이닝 종료
1번 선수는 항상 4번 타자

- 1 : 안타 : 타자와 모든 주자가 한 루씩 진루
- 2 : 2루타 : 타자와 모든 주자가 두 루씩 진루
- 3 : 3루타 : 타자와 모든 주자가 3루씩 진루
- 4 : 홈런 : 타자와 모든 주자가 홈까지 진루
- 0 : 아웃 : 모든 주자는 진루하지 못하고 공격 팀에 아웃이 하나 증가

가장 많은 득점을 하는 타순을 찾고, 그 떄의 득점을 구해보자
n : 이닝수 2 ~ 50
arr  : 이닝별 각 선수가 이닝에서 얻는 결과

논리
- 순열을 만들어야 하나? 9개의 순열 40320
-  1초에 20만
- dfs로 순열을 만들되, 비트마스크를 활용
- 순열을 만들게 되면
    - 이닝별 점수 계산
    -

시간초과 해결
- 리스트 연산을 변수 연산으로 변경했다.
- 중복되는 변수를 하나의 변수로 지정하는게 더 오래걸린다는 말이 있어서 수정했다.
- 가지치기를 위해서 누적합을 통해 각 이닝에서 남은 이닝동안 얻을 수 있는 이론상 최댓값을 구함
- 비트마스크를 이용한 순열을 구했다.
'''

import sys
import time
sys.stdin = open('input.txt')

input = sys.stdin.readline

def score(lineup):
    global max_case
    lineup = lineup[:3] + [0] + lineup[3:]
    point = 0
    i = 0
    num = 0
    for inning in data:
        out = 0
        ru1, ru2, ru3 = 0, 0, 0
        num += 1

        while out < 3:
            # hit = inning[lineup[i]]
            if inning[lineup[i]] == 0:
                out += 1
            elif inning[lineup[i]] == 4:
                point += ru1 + ru2 + ru3 + 1
                ru1, ru2, ru3 = 0, 0, 0

            elif inning[lineup[i]] == 1:
                point += ru3
                ru1, ru2, ru3 = 1, ru1, ru2
            elif inning[lineup[i]] == 2:
                point += ru2 + ru3
                ru1, ru2, ru3 = 0, 1, ru1
            else:
                point += ru1 + ru2 + ru3
                ru1, ru2, ru3 = 0, 0, 1

            i = (i + 1) % 9

        if num != n and max_case > prun_case[num] + point:
            return

    if max_case < point:
        max_case = point

# 순열 만들기
def dfs(now, visited):
    global cnt
    if now == 8:
        score(lineup)
    else:

        for i in range(1, 9):
            if not(visited & 1<<i):
                lineup[now] = i
                dfs(now + 1, visited | 1 << i)
                lineup[now] = 0

n = int(input()) # 이닝 수
data = [0 for i in range(n)]
prun_case = [0 for i in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))
    tmp = data[i].count(0)
    if tmp == 1:
        prun_case[i] = 24
    elif tmp == 2:
        prun_case[i] = 16
    else:
        prun_case[i] = 9 - tmp

# 각 이닝에서 남은 이닝동안 얻을 수 있는 이론상 최댓값(0이 아니면 홈런이라고 가정)
for i in range(n-2, -1, -1):
    prun_case[i] += prun_case[i + 1]

# 순열만들기
visited = 1 << 9
lineup = [0 for _ in range(8)]

cnt = 0
max_case = 0
dfs(0, visited)
print(max_case)