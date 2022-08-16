import sys
sys.stdin = open('input.txt')

width, height = map(int, input().split())
n = int(input())

range_arr = [[0, height], [0, width]] # r, c

for _ in range(n):
    direc, idx = map(int, input().split())
    range_arr[direc].append(idx) # 0 -> r, 1 -> c

# align
for i in range(2):
    range_arr[i].sort()

# max_range between i and i + 1
max_y = 0
max_x = 0
y_range = range_arr[0]
x_range = range_arr[1]

for i in range(len(y_range)-1):
    tempy = abs(y_range[i] - y_range[i+1])
    if tempy > max_y:
        max_y = tempy

for i in range(len(x_range) - 1):
    tempx = abs(x_range[i] - x_range[i + 1])
    if tempx > max_x:
        max_x = tempx

print(max_x * max_y)