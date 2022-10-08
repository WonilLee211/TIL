matrix = list('0'*101 for _ in range(101))

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(b + 1, d+1):
        matrix[i] = matrix[i][:a+1] + '1'*(c-a) + matrix[i][c+1:]
cnt = 0
for row in matrix:
    if '1' in row:
        cnt += row.count('1')

print(cnt)