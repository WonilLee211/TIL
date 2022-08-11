from collections import deque

arr = [[9,20,2,18,11], [19,1,25,3,21], [8,24,10,17,7],[15,4,16,5,6], [12,13,22,23,14]]
n = len(arr)

max_idx = [0, 0]
temp = []

# 이중 리스트 arr를 단일 리스트로 변경
for li in arr:
    temp += li

# 삽입정렬
for i in range(1, n**2):
    min_i = i
    for j in range(i-1 , -1, -1):
        if temp[j] > temp[min_i]:
            temp[j], temp[min_i] = temp[min_i], temp[j]
            min_i = j
        else:
            break

# deque 자료형 사용
ordered_arr = deque(temp)


i = 0 # i : 정렬방향을 결정할 변수
idx = [0, 0] # 값이 저장이 위치를 저장

# 달팽이 배열을 저장할 2차원 리스트
result = list([0]*len(arr) for _ in range(n))
result[0][0] = ordered_arr.popleft()

# idx가 마지막 저장 위치가 될 때 까지
while idx != [n//2, n//2]:
    if i == 0: # 오른쪽으로 나아가는 경우
        # 열이 범위를 벗어나지 않고 다음 값을 저장할 위치가 result가 비어있을 경우
        while idx[1] < n-1 and not result[idx[0]][idx[1]+1]:
            res = ordered_arr.popleft() # 왼쪽 값을 빼내서 작은 값이 순서대로 나오도록 설정
            idx[1] += 1
            result[idx[0]][idx[1]] = res

    if i == 1: # 아래로 나아가는 경우
        while idx[0] < n-1 and not result[idx[0]+1][idx[1]]:
            res = ordered_arr.popleft()
            idx[0] += 1
            result[idx[0]][idx[1]] = res

    if i == 2: # 왼쪽으로 나아가는 경우
        while idx[1] > 0 and not result[idx[0]][idx[1]-1]:
            res = ordered_arr.popleft()
            idx[1] -= 1
            result[idx[0]][idx[1]] = res

    if i == 3: # 위쪽으로 나아가는 경우
        # 위쪽으로 나아갈 땐 범위를 벗어날 가능성 없음
        while not result[idx[0]-1][idx[1]]:
            res = ordered_arr.popleft()
            idx[0] -= 1
            result[idx[0]][idx[1]] = res

    i += 1
    i %= 4

print(result)