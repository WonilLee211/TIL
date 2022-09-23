import sys
sys.stdin = open('input.txt')

def perm(i):
    global ans
    if i == n:
        '''
        [1, 2, 3]
        [1, 3, 2]
        '''
        arr = p[:] + [1]
        temp = 0
        for i in range(len(arr)-1):
            temp += data[arr[i]-1][arr[i+1]-1]
            if temp >= ans:
                return
        if temp < ans:
            ans = temp

    else:
        for j in range(1, n):
            if not used[j]:
                used[j] = 1
                p[i] = a[j]
                perm(i + 1)
                used[j] = 0

for tc in range(1, int(input()) + 1):
    n = int(input())
    data = list(list(map(int, input().split())) for i in range(n))
    # 1xx의 순열 구하기
    # 경우의 수에 따라 최소값 계산하기
    # 백트래킹으로 가지치기
    a = list(range(1, n + 1))
    used = [0] * n
    p = [0 for i in range(n)]
    p[0] = 1
    used[0] = 1
    ans = 0
    for i in range(n):
        ans += sum(data[i])

    perm(1)
    print(f'#{tc} {ans}')