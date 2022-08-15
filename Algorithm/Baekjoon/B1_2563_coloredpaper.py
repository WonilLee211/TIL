import sys
sys.stdin = open('input.txt')
matrix = list('0'*101 for _ in range(101))
n = int(input())
for _ in range(n):
    a, b= map(int, input().split())
    for i in range(b + 1, b+ 11):
        matrix[i] = matrix[i][:a+1] + '1'*10 + matrix[i][a+11:]
cnt = 0
for row in matrix:
    if '1' in row:
        cnt += row.count('1')

print(cnt)