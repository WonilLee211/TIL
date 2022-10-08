import sys
sys.stdin = open('input.txt')

n = int(input())
nums =[0] * (n + 1)
arr = []
for i in range(n):
    clr, size = map(int, input().split())
    arr.append([size, clr])
    nums[i + 1] = [clr, size]

arr.sort()

acc = [0 for i in range(n + 1)]
clrs = [0 for i in range(n + 1)]
sizes = [0 for i in range(n + 1)]

for i in range(n):
    clrs[nums[i][]]
    acc[i + 1] = acc[i] + arr[i][0]
# 색이 다르고 크기가 작은 공만 먹는다.
# 크기는 정렬을 통해 피하고
# 색이 같은 경우

print(acc)