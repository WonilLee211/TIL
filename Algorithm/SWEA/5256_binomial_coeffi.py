import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, a, b = map(int, input().split())

    xy = [[0] * (n + 2) for i in range(n + 2)]

    for i in range(1, n + 2):
        xy[i][0] = 1
        xy[0][i] = 1

    for j in range(2, n+1):
        for i in range(1, n):
            xy[i][j-i] = xy[i-1][j-i] + xy[i][j - i - 1]

    print(f'#{tc} {xy[a][b]}')

'''
1 1 1 1 1 1 1 1 1 1 
1 2 3 4 5
1 3 6 10
1 4 10 
1 5 
1
1

'''