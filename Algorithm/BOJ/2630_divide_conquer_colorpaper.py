'''
n = 2^k
k : 1 ~ 7
사각형을 사분활하면서 내부의 수가 모두 같은 수로 채워지거나 크기가 1인 정사각형이 될 때까지

생성된 정사각형 개수 세기

논리
- 재귀적으로 탐색
- 모든 수가 같다는 조건을 만족할 때까지 분할
- 조건을 만족하면 수를 세고 탈출

'''
import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

def dividepaper(n, i, j):
    global blue_cnt, white_cnt

    if n == 1:
        if paper[i][j] == 1:
            blue_cnt += 1
        else:
            white_cnt += 1
        return
    else:
        for k in range(n):
            if paper[i + k][j:j + n].count(paper[i][j]) != n:
                dividepaper(n // 2, i, j)
                dividepaper(n // 2, i, j + n//2)
                dividepaper(n // 2, i + n//2, j)
                dividepaper(n // 2, i + n//2, j + n//2)
                break
        else:
            if paper[i][j] == 1:
                blue_cnt += 1
            else:
                white_cnt += 1
            return

n = int(input())
paper = list(list(map(int, input().split())) for i in range(n))

blue_cnt, white_cnt = 0, 0
dividepaper(n, 0, 0)
print(white_cnt)
print(blue_cnt)
