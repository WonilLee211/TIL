'''
마지막날까지 최대의 수익을 낼 수 있는 스케줄에 따라 일할 때 얻을 수 있는 최대 이익 계산

논리
- dp에 저장할 값 : 현재일에 받을 수 있는 최대의 수익
- 미래의 dp 값 vs 현재의 수익 + 현재일을 하게 되면 그 미래에 얻게되는 이익과 비교
- 현재의 dp 값이 profit보다 크면 갱신
    - dp문제를 풀 때 생각의 방향성은 해당 위치의 dp값은 어떤 경로로 거쳐서 저장된 값인지 모르지만
    - 현재의 위치에서 가장 최적의 값이 저장되어있어야 하고 저장되어있다고 생각하는 게 중요함
'''
import sys
sys.stdin = open('input.txt')

n = int(input())
T_P = [0 for i in range(n)] # 일기간, 이익
for i in range(n):
    T_P[i] = list(map(int, input().split()))

dp = [0 for _ in range(n)]

profit = 0
for i in range(n):
    if i + T_P[i][0] - 1 < n and dp[i + T_P[i][0] - 1] < profit + T_P[i][1]:
        dp[i + T_P[i][0] - 1] = profit + T_P[i][1]
    if dp[i] > profit:
        profit = dp[i]

print(profit)
