import sys
sys.stdin = open('input.txt')

'''
전형적인 구간합 문제
- 모든 구간의 누적합을 구함
- 누적합 - 누적합을 이용해서 구간합 구하기

'''
n, m = map(int, input().split())

arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

idxs = [0] * m
for i in range(m):
    idxs[i] = list(map(int, input().split()))

acc = list([0] * (n + 2) for _ in range(n + 2))

for i in range(n):
    for j in range(n):
        acc[i + 1][j + 1] = arr[i][j] + acc[i + 1][j] + acc[i][j + 1] - acc[i][j]

for i in range(m):
    fr_i, fr_j, to_i, to_j = idxs[i][0], idxs[i][1], idxs[i][2], idxs[i][3]
    ans = acc[to_i][to_j] - acc[fr_i-1][to_j] - acc[to_i][fr_j-1] + acc[fr_i-1][fr_j-1]
    print(ans)