'''
계단 수

n < 10 = 0
n == 10 = 1
n > 10 =


시작값을 1 ~ 9 로 선택
다음 값은 현재 값의 +- 1로 설정
시작값 1일 때
1 2 1   0
        2
    3

1 0

bfs 비트마스크
q 요소 형태 (iter, 비트, now)

문제를 분리해서 생각하자.
1. 계단수 찾기
- n + 1의 계단 수는 n의 계단 수에서 양쪽에 1 차이나는 수 붙이기

2. 0123456789가 포함된 계단만 cnt
- 비트마스크 마지막에 1<<10 - 1 위치 값만
n 계단 수 길이 / 방금 사용한 숫자 / 비스 마스크

'''
import sys
sys.stdin = open("input.txt")

num = int(1<<9)

n = int(input())
dp = list(list([0] * (1 << 10) for _ in range(10)) for __ in range(n + 1))

for i in range(1, 10):
    dp[1][i][(1 << i)] = 1

# 계단의 길이가 1일 때 사용된 숫자 0 ~ 9까지 사용했음을 표시

for i in range(2, n + 1):
    for j in range(10):
        for k in range(1 << 10):
            if j == 0:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][1][k]) % num
            elif j == 9:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][8][k]) % num
            else:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j - 1][k]) % num
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j + 1][k]) % num

ans = 0
for i in range(10):
    ans = (ans + dp[n][i][(1 << 10) - 1]) % num

print(ans)