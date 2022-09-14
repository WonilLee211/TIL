import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    # n : 접수 창구의 수
    # m : 정비 창구의 수
    # k : 고객 수
    # a : 지갑을 두고간 고객이 이용한 접수 창구 번호
    # b : 지갑을 두고간 고객이 이용한 접수 창구 번호
    n, m, k, a, b = map(int, input().split())
    # i번째 접수 창구가 고장을 접수하는 데 걸리는 시간 리스트
    ta = [-1] + list(map(int, input().split()))
    # j번째 정비 창구가 고장을 정비하는 데 걸리는 시간 리스트
    tb = [-1] + list(map(int, input().split()))
    # k번째 고객이 정비소를 방문하는 시간
    tk = [-1] + list(map(int, input().split()))

    t  = 0
    cli_n = 1
    rct_wait = deque()
    rpr_wait = deque()
    receptions = [0] * (n + 1)
    repairshops = [0] * (m + 1)

    # 지갑을 두고간 고객이 사용한 창구를 사용한 고객 모을 곳
    rct_a = []
    rpr_b = []
    flag = True
    cnt = 0

    while flag:

        while cli_n <= k and t == tk[cli_n]:
            rct_wait.append([cli_n, 0])
            cli_n += 1

        for i in range(1, n + 1):
            if receptions[i] != 0:
                receptions[i][1] -= 1

                if receptions[i][1] == 0:
                    rpr_wait.append(receptions[i])
                    receptions[i] = 0


            if len(rct_wait) > 0 and receptions[i] == 0:
                receptions[i] = rct_wait.popleft()
                receptions[i][1] = ta[i]
                if i == a:
                    rct_a.append(receptions[i][0])

        for i in range(1, m + 1):
            if repairshops[i] != 0:
                repairshops[i][1] -= 1
                if repairshops[i][1] == 0:
                    cnt += 1
                    if cnt == k:
                        flag = False
                    repairshops[i] = 0
            if len(rpr_wait) > 0 and repairshops[i] == 0:
                repairshops[i] = rpr_wait.popleft()
                repairshops[i][1] = tb[i]
                if i == b:
                    rpr_b.append(repairshops[i][0])

        t += 1

    result = sum(set(rct_a)&set(rpr_b))

    print(f'#{tc} {result or -1}')