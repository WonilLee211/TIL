import sys
sys.stdin = open("input.txt")

'''
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수
N번째 감소하는 수를 출력하는 프로그램을 작성
'''

from itertools import combinations

n = int(input())
scope = list(range(0, 10))
coms = []

if n < 11:
    print(n)
elif n > 1022:
    print(-1)

else:
    for i in range(1, 11):
        for com in combinations(scope, i):
            com = sorted(list(com), reverse=True)
            coms.append(int("".join(map(str, com))))

    coms.sort()
    print(coms[n])
