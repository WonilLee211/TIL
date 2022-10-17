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

'''

def score(lineup):
    global max_case
    point = 0
    ru = [0 for _ in range(3)]
    i = 0
    for inning in data:
        out = 0
        while out < 3:


            hit = inning[lineup[i]]
            if hit == 0:
                out += 1
            else:
                if hit == 4:
                    point += ru.count(1) + 1
                    ru = [0] * 3
                else:
                    point += ru[3 - hit:].count(1)
                    ru = [0] * (hit - 1) + [1] + ru[:3 - hit]

            i = (i + 1) % 9

    if max_case < point:
        max_case = point

def dfs(now):
    global visited, cnt

    if now == 9:
        score(lineup)
    else:
        if now == 3:
            dfs(now + 1)

        for i in range(9):
            if i != 0 and not(visited & 1<<i):
                visited |= 1 << i
                lineup[now] = i
                dfs(now + 1)
                visited &= ~(1 << i)
                lineup[now] = 0

import sys
sys.stdin = open('input.txt')

n = int(input()) # 이닝 수
data = list(list(map(int, input().split())) for _ in range(n))

# 순열만들기
visited = 1 << 9
lineup = [0 for _ in range(9)]


cnt = 0
max_case = 0

dfs(0)
print(max_case)