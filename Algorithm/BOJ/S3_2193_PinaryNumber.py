import sys
sys.stdin = open('input.txt')

n = int(input())
f = list([0, 0] for i in range(n + 1))
f[1] = [0, 1]
for i in range(2, n + 1):
    f[i][0] = f[i - 1][0] + f[i - 1][1]
    f[i][1] = f[i - 1][0]

print(sum(f[n]))