'''


논리
- dp에 저장할 값 - 현재일에 받을 수 있는 최대의 수익
- 미래의 dp 값과 현재의 dp값 + 현재일을 하게 되면 얻게되는 이익과 비교

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
    if i + T_P[i][0] - 1 < n and dp[i + T_P[i][0] - 1] < dp[i] + T_P[i][1]:
        for j in range(T_P[i][0]):
            dp[i + j] = T_P[i][1]
        profit += dp[i]
print(dp)
print(profit)
