import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))

cnt = temp1 = temp2 = 1

for i in range(n-1):

    if arr[i] <= arr[i+1]:
        temp1 += 1
    else:
        if temp1 > cnt:
            cnt = temp1
        temp1 = 1

    if arr[i] >= arr[i + 1]:
        temp2 += 1
    else:
        if temp2 > cnt:
            cnt = temp2
        temp2 = 1

    if i == n-2:
        if temp1 > cnt:
            cnt = temp1
        if temp2 > cnt:
            cnt = temp2

print(cnt)
