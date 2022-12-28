import sys
sys.stdin = open('input.txt')

'''
논리
- 최소와 최대 구하기
- 연산자 순서 순열 구하기
    - 중복값이 있는 배열의 순열 구하기...
    
- 순열별로 계산하기
- 계산결과 대소 비교
- 시간 초과

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # 수의 배열

add, sub, mul ,div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(d, value):
    global min_value, max_value, add, sub, mul, div

    if d == n:
        max_value = max(max_value, value)
        min_value = min(min_value, value)

    else:
        if add > 0:
            add -= 1
            dfs(d + 1, value + arr[d])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(d + 1, value - arr[d])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(d + 1, value * arr[d])
            mul += 1
        if div > 0:
            div -= 1
            dfs(d + 1, int(value / arr[d]))
            div += 1


dfs(1, arr[0])

print(max_value)
print(min_value)



'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # 수의 배열
info = list(map(int, input().split())) # 덧셈0 수 , 뺄셈1 수, 곱셈2 수, 나누셈3 수

operators_idx = []
for i in range(4):
    operators_idx += [i] * info[i] # 각 연산자 갯수 만큼 각 연산자를 의미하는 숫자들을 합친 배열

def compare_value(case, isMax):
    global min_max

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
        if isMax and acc >
    if min_max[0] > acc:
        min_max[0] = min(min_max[0], acc)
    if min_max[1] < acc:
        min_max[1] = max(min_max[1], acc)


def dfs(d, case):

    if d == n - 1 and case not in cases:
        cases.append(case)
        compare_value(case)

    else:
        for i in range(n - 1):
            if visited[i] == 0:
                visited[i] = 1
                dfs(d + 1,  case + [operators_idx[i]])
                visited[i] = 0


min_max = [int(1e9), int(-1e9)]
cases = []
visited = [0] * (n - 1)

dfs(0, [])

print(min_max[1])
print(min_max[0])

'''
