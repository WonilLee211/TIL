'''
n : 2의 제곱수

(0 (0011) (0(0111)01) 1)

논리
- 분할 정복으로 재귀형태로 표현
- 사각형이 한 숫자로 구성되어있으면 그 숫자로 압축하여 리턴
- 그렇지않다면 한숫자로 구성될 때까지 분할
- 조건에 만족하면 시작점의 데이터를 문자열의 합
- 분할을 시작하고 끝날 때 ()로 표현

주의점
- 비교 대상이 행별 시작점이 아닌 전체 사각형의 시작점이어야 한다.
'''

import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

def comp_data(n, i, j):
    global ans
    if n == 1:
        ans += data[i][j]
        return
    else:
        for k in range(n):
            if set(data[i + k][j:j + n]) != set([data[i][j]]):
                ans += '('
                for r in range(2):
                    for c in range(2):
                        comp_data(n//2, i + n//2 * r, j + n//2 * c)
                ans += ')'
                break
        else:
            ans += data[i][j]
            return

n = int(input())
data = list(list(input()) for i in range(n))

ans = ''
comp_data(n, 0, 0)
print(ans)