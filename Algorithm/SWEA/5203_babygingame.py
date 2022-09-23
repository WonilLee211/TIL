import sys
sys.stdin = open('input.txt')

def check(arr):
    n = len(arr)
    for i in range(n - 2):
        if arr[i]:
            if arr[i] and arr[i + 1] and arr[i + 2]:
                return 1

    for i in range(n):
        if arr[i] > 2:
            return 1
    return 0

for tc in range(1, int(input()) + 1):
    a = list(map(int, input().split()))
    a = a[::-1]

    cnt_1 = [0 for i in range(10)]
    cnt_2 = [0 for i in range(10)]

    while a:
        cnt_1[a.pop()] += 1
        if check(cnt_1):
            print(f'#{tc} 1')
            break

        cnt_2[a.pop()] += 1
        if check(cnt_2):
            print(f'#{tc} 2')
            break
    else:
        print(f'#{tc} 0')