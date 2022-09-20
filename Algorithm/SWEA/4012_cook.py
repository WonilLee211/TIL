import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [0] * n
    diff = 0
    for i in range(n):
        arr[i] = list(map(int, input().split()))
        diff += sum(arr[i])

    comb = list(combinations(range(n), n//2))
    for a in comb:
        b = list(set(range(n)) - set(a))
        a = list(a)
        sum_a = sum_b = 0
        for i in range(n//2 - 1):
            for j in range(i+1, n//2):
                sum_a += arr[a[i]][a[j]] + arr[a[j]][a[i]]
                sum_b += arr[b[i]][b[j]] + arr[b[j]][b[i]]

        temp = abs(sum_a - sum_b)
        if temp < diff:
            diff = temp

    print(f'#{tc} {diff}')
