import sys
sys.stdin = open('input.txt')

'''
논리
- 최소와 최대 구하기
- 연산자 순서 순열 구하기
    - 중복값이 있는 배열의 순열 구하기...
    
- 순열별로 계산하기
- 계산결과 대소 비교

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # 수의 배열
info = list(map(int, input().split())) # 덧셈0 수 , 뺄셈1 수, 곱셈2 수, 나누셈3 수

operators_idx = []
for i in range(4):
    operators_idx += [i] * info[i] # 각 연산자 갯수 만큼 각 연산자를 의미하는 숫자들을 합친 배열

def compare_value(case):
    acc = arr[0]
    for i in range(n - 1):

        if case[i] == 0:
            acc += arr[i + 1]
        elif case[i] == 1:
            acc -= arr[i + 1]
        elif case[i] == 2:
            acc *= arr[i + 1]
        else:
            if acc < 0:
                acc = -(abs(acc) // arr[i + 1])
            else:
                acc //= arr[i + 1]

    return [min(min_max[0], acc), max(min_max[1], acc)]

def dfs(d, case):

    global min_max
    if d == n - 1 and case not in cases:
        cases.append(case)
        min_max = compare_value(case)
    else:
        for i in range(n - 1):
            if visited[i] == 0:
                visited[i] = 1
                case.append(operators_idx[i])
                dfs(d + 1, case)
                visited[i] = 0
                case.pop()

min_max = [int(1e9), int(-1e9)]
cases = []
visited = [0] * (n - 1)

dfs(0, [])
print(len(cases))

print(min_max[1])
print(min_max[0])