import sys
sys.stdin = open('input.txt')

from itertools import combinations
def max_com(arr):
    res = 0

    for i in range(1, len(arr)+1):
        coms = combinations(arr, i)
        for com in coms:
            if sum(com) <= c:
                temp = 0
                for j in range(len(com)):
                    temp += com[j]**2
                if res < temp:
                    res = temp
    return res

for tc in range(1, int(input()) + 1):
    n, m, c = map(int, input().split())
    data = list(list(map(int, input().split())) for i in range(n))

    max_profix = list([0] * n for i in range(n))
    for i in range(n):
        for j in range(n - m + 1):
            max_profix[i][j] = max_com(data[i][j : j + m])

    max_val = 0
    for i in range(n-1):
        for j in range(i+1, n):
            temp = max(max_profix[i]) + max(max_profix[j])
            if temp > max_val:
                max_val = temp

    print(f'#{tc} {max_val}')