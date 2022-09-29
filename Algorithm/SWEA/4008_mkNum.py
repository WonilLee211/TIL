import sys
sys.stdin = open('input.txt')

from collections import deque
# from math import
from itertools import permutations

def calculate(op_arr, arr_):
    arr = deque(arr_)
    q = deque([arr.popleft()])
    j = 0
    while arr:
        q.append(arr.popleft())
        n1 = q.popleft()
        n2 = q.popleft()

        if op_arr[j] == '+':
            q.append(n1 + n2)
        elif op_arr[j] == '-':
            q.append(n1 - n2)
        elif op_arr[j] == '*':
            q.append(n1 * n2)
        else:
            q.append(int(n1 / n2))

        j += 1

    return q
#
# def mPm(d, arr):
#     global min_v, max_v
#
#     if d == m:
#         if tuple(op_arr) in used:
#             return
#         used.append(tuple(op_arr))
#         v = calculate(op_arr, arr)[0]
#
#         if min_v > v:
#             min_v = v
#         if max_v < v:
#             max_v = v
#     else:
#         for i in range(d, m):
#             op_arr[i], op_arr[d] = op_arr[d], op_arr[i]
#             mPm(d + 1, arr)
#             op_arr[i], op_arr[d] = op_arr[d], op_arr[i]



for tc in range(1, int(input()) + 1):
    #
    op = '+-*/'
    n = int(input())
    opnums = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    opstr = ''
    for i, num in enumerate(opnums):
        opstr += op[i]*num

    m = len(opstr)
    op_arr = list(opstr)
    used = []
    max_v = -100000001
    min_v = 100000001
    for op in permutations(op_arr, m):
        if tuple(op) in used:
            continue

        used.append(tuple(op))

        v = calculate(op, arr)[0]
        if min_v > v:
            min_v = v
        if max_v < v:
            max_v = v

    print(max_v-min_v)