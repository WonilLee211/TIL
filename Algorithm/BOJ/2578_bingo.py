import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque

# 입력값들을 먼저 일차원 배열로 받기
bingo_arr = []
for i in range(5):
    bingo_arr.extend(input().split())

# 지워야할 값들을 일차원 배열로 저장
del_arr = deque([])
for _ in range(5):
    del_arr.extend(input().split())

# 지워야할 값마다 빙고의 위치를 저장
del_dict = {}
for key in del_arr:
    del_dict[key] = []

# 2차원 배열의 요소 값(key)들의 위치를 del_dict 값으로 저장
for i in range(25):
    t, v = divmod(i, 5)
    del_dict[bingo_arr[i]] = [t, v]

# 삭제 정보를 카운트할 딕셔너리
del_cnt = {0:0, 4:0}

for i in range(2):
    for j in range(5):
        del_cnt[(i, j)] = 0

cnt_three = 0
cnt_pop = 0
while cnt_three < 3:
    cnt_three = 0
    if 5 in del_cnt.values():
        for value in del_cnt.values():
            if value == 5:
                cnt_three += 1

    if cnt_three >=3:
        break

    cnt_pop += 1
    del_num = del_arr.popleft()
    r, c = del_dict[del_num]
    del_cnt[(0, r)] += 1
    del_cnt[(1, c)] += 1
    if r + c == 4:
        del_cnt[4] += 1
    if r - c == 0:
        del_cnt[0] += 1

print(cnt_pop)

'''
print(bingo_arr)
pprint(bingo_matrix)
print(del_dict)
print(del_cnt)
'''