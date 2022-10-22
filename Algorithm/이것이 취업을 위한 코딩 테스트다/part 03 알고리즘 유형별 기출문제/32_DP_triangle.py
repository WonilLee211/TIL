'''
삼각형 꼭대기에서 아래 칸에 양쪽 중 하나를 선택해서 계산

논리
- 2차원 dp 필드를 만들고 각 위치별로 올 수 있는 값에 대해 비교하고 큰 값으로 없데이트

'''

import sys
sys.stdin = open('input.txt')
n = int(input())

input = sys.stdin.readline
dp = [[0] * n for _ in range(n)]
data = [[-1] * n for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(i + 1):
        data[i][j] = temp[j]

dp[0][0] = data[0][0]

for i in range(n - 1):
    for j in range(n - 1):
        if data[i][j] != -1:
            for ni, nj in [(i + 1, j), (i + 1, j + 1)]:
                if dp[ni][nj] < dp[i][j] + data[ni][nj]:
                    dp[ni][nj] = dp[i][j] + data[ni][nj]

print(max(dp[-1]))


