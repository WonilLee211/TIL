import sys
sys.stdin = open('input.txt')

def pre_process(n, arr):
    for i in range(n):
        if arr[i][0] == 1:
            arr[i][0] = 0
        elif arr[i][0] == 2:
            arr[i][0] = h
        elif arr[i][0] == 3:
            arr[i][0], arr[i][1] = arr[i][1], 0
        else:
            arr[i][0], arr[i][1] = arr[i][1], w

    return arr


w, h = map(int, input().split())
# 1, 2, 3, 4 : 북, 남, 서, 동

n = int(input())
stores = [list(map(int, input().split())) for i in range(n)]
security = list(map(int, input().split()))

# [[1, 4], [3, 2], [2, 8]]
# [2, 3]

# 전처리 동서남북을 좌표로 바꾸기
stores = pre_process(n, stores)
security = pre_process(1, [security])
# [[0, 4], [2, 0], [5, 8]]
# [[5, 3]]

total = 0
for store in stores:
    temp = 0
    # 북남 마주볼 때
    if (store[0] == 0 and security[0][0] == h) or (store[0] == h and security[0][0] == 0):
        x = store[1] + security[0][1]
        if w*2 - x > x:
            total += x + h
        else:
            total += w*2 - x + h

    # 동서 마주볼 때
    elif (store[1] == 0 and security[0][1] == w) or (store[1] == w and security[0][1] == 0):
        x = store[0] + security[0][0]
        if h * 2 - x > x:
            total += x + w
        else:
            total += h * 2 - x + w

    else:
        total += abs(store[0]-security[0][0]) + abs(store[1]-security[0][1])

print(total)