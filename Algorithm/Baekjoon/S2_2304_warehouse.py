import sys
sys.stdin = open('input.txt')
# 주어진 범위 내에 최대 값의 인덱스 반환하는 함수
def max_in_range(L, R):
    max_idx = L
    for i in range(L, R):
        if col_arr[i][1] > col_arr[max_idx][1]:
            max_idx = i
    return max_idx

# 주어진 범위 내에 최대 값의 인덱스 반환하는 함수
def max_in_range(L, R):
    max_idx = L
    for i in range(L, R):
        if col_arr[i][1] > col_arr[max_idx][1]:
            max_idx = i
    return max_idx

num_col = int(input())
col_arr = []

for i in range(num_col):
    col_arr.append(list(map(int, input().split())))

# 정렬 및 맥스 위치 인덱스 찾기
for i in range(num_col-1):
    temp = i
    for j in range(i+1, num_col):
        if col_arr[j][0] < col_arr[temp][0]:
            temp = j
    col_arr[i], col_arr[temp] = col_arr[temp], col_arr[i]

<<<<<<< HEAD
# 가장 높은 곳의 인덱스
=======
>>>>>>> 2bc358a9614404e2012a80e5b5dc647288d27534
max_idx = num_col-1
for i in range(num_col-1):
    if col_arr[i][1] > col_arr[max_idx][1]:
        max_idx = i

area = col_arr[max_idx][1]
max_ldx = max_rdx = max_idx

<<<<<<< HEAD
# 가장 높은 곳의 왼쪽 부분 넓이
=======
>>>>>>> 2bc358a9614404e2012a80e5b5dc647288d27534
while max_ldx != 0:
    next_ldx = max_in_range(0, max_ldx)
    area += (col_arr[max_ldx][0]-col_arr[next_ldx][0]) * col_arr[next_ldx][1]
    max_ldx = next_ldx

<<<<<<< HEAD
# 가장 높은 곳의 오른쪽 부분 넓이
=======
>>>>>>> 2bc358a9614404e2012a80e5b5dc647288d27534
while max_rdx != len(col_arr)-1:
    next_rdx = max_in_range(max_rdx+1, len(col_arr))
    area += (col_arr[next_rdx][0] - col_arr[max_rdx][0]) * col_arr[next_rdx][1]
    max_rdx = next_rdx

<<<<<<< HEAD
print(area)
=======
print(area)
>>>>>>> 2bc358a9614404e2012a80e5b5dc647288d27534
