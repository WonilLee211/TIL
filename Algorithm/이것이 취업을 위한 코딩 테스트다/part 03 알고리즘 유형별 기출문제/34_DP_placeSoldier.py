'''
문제 요약
내부요소를 삭제함으로써 전투력이 내림차순으로 정렬되도록 함
최대한 많은 인원이 구성되어있도록 함
열외시켜야하는 병사의 수 출력하기

논리
- LDS(Longest Decreasing Subsequence)
- 현재의 위치에서 이전의 요소들에 대해서 각 요소들이 가진 최장 감소 수와 비교
- 각 위치는 이전에 어떤 경우로 만들어진 수인지와 상관없이 최장 감소 수를 저장하고 있다.
- 현재 위치가 이전의 위치 요소 값과 비교하여 작다면, 각 이전의 요소 dp + 1 vs 현재 위치 dp
- 작다면 갱신

'''
import sys
sys.stdin = open('input.txt')


n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n-max(dp))
