import sys
sys.stdin = open('input.txt')

num_col = int(input())
col_arr = []

for i in range(num_col):
    col_arr.append(list(map(int, input().split())))

# 정렬
for i in range(num_col-1):
    temp = i
    for j in range(i+1, num_col):
        if col_arr[j][0] < col_arr[temp][0]:
            temp = j
    col_arr[i][0], col_arr[temp][0] = col_arr[temp][0], col_arr[i][0]


max_idx = col_arr[0][0]
for i in range(1, num_col):
    if col_arr[i][1] > col_arr[max_idx][1]:
        max_idx = i

# 5 [[2, 4], [4, 4], [5, 8], [8, 6], [11, 3], [13, 10], [15, 6]]
i = 1
area = col_arr[max_idx][1]
max_Ldx, max_Rdx = max_idx, ,max_idx + 1
max_L = max_R = col_arr[max_idx][1]
cnt_L,

while max_Ldx -i > 0:
    if col_arr[max_Ldx - i][1] < col_arr[max_Ldx][1]:

    if col_arr[max_Ldx - i][1] > col_arr[max_Ldx][1]:
        area += (max_Ldx - col_arr[max_Ldx-i][0]) * max_L
        max_Ldx = col_arr[max_Ldx-i][0]

    i -= 1

while max_idx + i < num_col:
    if col_arr[max_idx + i][1] > col_arr[max_idx][1]:
        area += (col_arr[max_idx + i][0] - max_idx) * col_arr[max_idx - i][1]
        max_idx = col_arr[max_idx - i][0]

    i -= 1
