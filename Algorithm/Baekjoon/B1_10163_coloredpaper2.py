import sys
sys.stdin = open('input.txt')

matrix = list('0'*1001 for _ in range(1001))
n = int(input())
for j in range(1, n + 1):
    a, b, c, d = map(int, input().split())
    j = str(j)
    for i in range(b + 1, b + d + 1):
        matrix[i] = matrix[i][:a + 1] + j * c + matrix[i][a + c + 1:]

for j in range(1, n + 1):
    cnt = 0
    j = str(j)
    for row in matrix:
        if j in row:
            cnt += row.count(j)

    print(cnt)