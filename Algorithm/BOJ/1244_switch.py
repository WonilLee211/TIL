import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
arr = [0] + list(map(int, input().split()))
num_p = int(input())
queue = deque()
for i in range(num_p):
    queue.append(list(map(int, input().split())))

while queue:
    temp = queue.popleft()

    if temp[0] == 1: # 남자일 경우
        for i in range(temp[1], len(arr), temp[1]):
            arr[i] = abs(arr[i] - 1)

    else: # 여자일 경우
        arr[temp[1]] = abs(arr[temp[1]] - 1)
        i = 1

        while  0 < temp[1] - i <= N and 0 < temp[1] + i <= N  and arr[temp[1] - i] == arr[temp[1] + i]:

            arr[temp[1] - i], arr[temp[1] + i] = abs(arr[temp[1] - i]-1),  abs(arr[temp[1] + i]-1)

            i += 1
arr = arr[1:]
j = 0
for i in range(len(arr)):
    print(arr[i], end = ' ')
    j += 1
    if j == 20:
        j = 0
        print()
