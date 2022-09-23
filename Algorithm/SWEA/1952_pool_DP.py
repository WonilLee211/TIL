import sys
sys.stdin = open('input.txt')
def find_min():

    for i in range(1, 13):
        dp[i] = min(d * plan[i-1], mp) + dp[i-1]
        if i > 2:
            dp[i] = min(m3p + dp[i - 3], dp[i])

    return dp

if __name__ == '__main__':
    t = int(input())
    for tc in range(1, t + 1):
        d, mp, m3p, yp = map(int, input().split())
        plan = list(map(int, input().split()))
        dp = [0 for i in range(13)]

        print(f'#{tc} {min(find_min()[-1], yp)}')