import sys
sys.stdin = open('input.txt')

n = int(input())

for num in range(1, n + 1):
    a, b, c, d = map(int, input().split())

    if b < start_y:
        start_y = b
    if b + d - 1 > last_y:
        last_y = b + d - 1

    for i in range(a, a + c):
        for j in range(b, b + d):
            matrix[j][i] = num

for num in range(1, n + 1):
    cnt = matrix.count(num)
    print(cnt)

'''
for num in range(1, n + 1):
    cnt = 0
    for j in range(start_y, last_y + 1):
        if num in matrix[j]:
            cnt += matrix[j].count(num)
'''
