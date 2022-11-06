'''

n = 현재 캐릭터의 점수, 항상 짝수


스킬 발동 조건
- n의 자릿 수를 기준으로 점수 n을 반으로 나누어
- 왼쪽 부분의 각 자릿수의 합과 오른족 부분의 각 자릿수의 합이 동일한 경우 LUCKY 출력
- 아닌 경우  READY 출력

'''

import sys
sys.stdin = open('input.txt')

n = list(map(int, input()))
length = len(n)

ans = "LUCKY" if sum(n[:length//2]) == sum(n[length//2:]) else "READY"

print(ans)