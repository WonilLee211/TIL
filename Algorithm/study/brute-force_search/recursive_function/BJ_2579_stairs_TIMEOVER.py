'''
Baekjoon 2579 계단 오르기
1. 규칙
- 계단은 한 번에 한 계단 또는 두 계단 오르기
- 연속된 세 개의 계단 밟기 안됨
- 마지막 도착 계단은 반드시 밟아야 함

2. 알고리즘
- DFS를 사용
- 각 경우 중 더 큰 경우만 저장하기
- 한 번에 이동가능한 거리 1 ~ 2칸
- 제약 조건 
    - 이동거리가 이전에 3번 중복되는지
    - 마지막 계단을 밟았는지
'''
''' 시간 초과

import sys

def dfs(N, crt_case, crt_i, arr):
    global max_case
    global cnt_one

    if crt_i == N-1:
        if crt_case > max_case:
            max_case = crt_case
            cnt_one = 0
            crt_case = 0
            crt_i = 0
            return
        
    elif crt_i > N-1:
        cnt_one = 0
        crt_case = 0
        crt_i = 0
        return
    
    # 이동 거리 crt_i 정하기
    for i in range(1,3):
        if i == 1:
            if cnt_one == 2:
                cnt_one = 0
                continue
            
            else:
                cnt_one += 1
                crt_i += i
                if crt_i < N:
                    crt_case += arr[crt_i]
                    dfs(N, crt_case, crt_i, arr)
                    
        else:
            cnt_one = 0
            crt_i += i
            if crt_i < N:
                crt_case += arr[crt_i]
                dfs(N, crt_case, crt_i, arr)
            
   
N = int(input())
arr = list(int(sys.stdin.readline()) for _ in range(N))

max_case = 0
cnt_one = 0
dfs(N, 0, 0, arr)
print(max_case)
'''
'''
# 가능한 인덱스 조합만 구하고 최종 단계에서 계산 후 최대 값 구하기
import sys
def dfs(N, arr, idx_arr):
    global crt_i
    global max_acc

    if crt_i >= N + 1:
        return

    elif crt_i == N:
        acc = 0

        for i, bool in enumerate(idx_arr):
            if bool:
                acc += arr[i]

        if acc > max_acc:
            max_acc = acc
        return


    for i in range(1, 3):
        if i == 1:
            if idx_arr[crt_i] and idx_arr[crt_i-1]:
                continue
        
        crt_i += i
        if crt_i < N + 1:
            idx_arr[crt_i] = i
            dfs(N, arr, idx_arr)
            idx_arr[crt_i] = 0
            crt_i -= i
        else:
            crt_i -= i
            return
        
N = int(input())
arr = [0]
arr += list(int(sys.stdin.readline()) for _ in range(N))
# N = 6
# arr = [0, 10, 20, 15, 25, 10, 20]

idx_arr = [0 for _ in range(N + 1)]
crt_i = 0
max_acc = 0

dfs(N, arr, idx_arr)
print(max_acc)
'''
# 가능한 인덱스 조합만 구하고 최종 단계에서 계산 후 최대 값 구하기
import sys
def dfs(N, arr, idx_arr):
    global crt_i
    global max_acc

    if crt_i >= N + 1:
        return

    elif crt_i == N:
        acc = 0

        for i, bool in enumerate(idx_arr):
            if bool:
                acc += arr[i]

        if acc > max_acc:
            max_acc = acc
        return


    for i in range(1, 3):
        if i == 1:
            if idx_arr[crt_i] and idx_arr[crt_i-1]:
                continue
        
        crt_i += i
        if crt_i < N + 1:
            idx_arr[crt_i] = i
            dfs(N, arr, idx_arr)
            idx_arr[crt_i] = 0
            crt_i -= i
        else:
            crt_i -= i
            return
        
N = int(input())
arr = [0]
arr += list(int(sys.stdin.readline()) for _ in range(N))
# N = 6
# arr = [0, 10, 20, 15, 25, 10, 20]

idx_arr = [0 for _ in range(N + 1)]
crt_i = 0
max_acc = 0

dfs(N, arr, idx_arr)
print(max_acc)
