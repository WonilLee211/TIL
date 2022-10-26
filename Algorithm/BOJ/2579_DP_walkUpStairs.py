'''
시작점에서 꼭대기에 위치한 도착점까지 가는 게임
각 계단에 적힌 점수를 획득하는 문제
규칙
- 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
- 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
- 마지막 도착 계단은 반드시 밟아야 한다.

논리
- 2차원 DP 테이블
- 각 위치별로
    - 한칸을 간 경우와 두칸을 가는 경우 연속된 계단인지 아닌지를 DP 테이블 열 위치로 나누기
    - 현재 위치에서 한 칸과 두 칸을 갈 수 있는 경우 표시해서 각 위치의 DP 값과 비교 갱신
'''
import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [[0, 0] for i in range(n)]

dp[0][0] = stairs[0]
if n != 1:
    dp[1][0] = stairs[1]

for i in range(n - 1):
    for j in range(2):
        if dp[i][j] == 0:
            continue

        if j == 0:
            if i + 1 < n and dp[i + 1][1] < dp[i][j] + stairs[i + 1]:
                dp[i + 1][1] = dp[i][j] + stairs[i + 1]
        if i + 2 < n and dp[i + 2][0] < dp[i][j] + stairs[i + 2]:
            dp[i + 2][0] = dp[i][j] + stairs[i + 2]

print(max(dp[-1]))
