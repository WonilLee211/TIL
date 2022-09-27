import sys
sys.stdin = open('input.txt')

from collections import deque

def mergesort(arr):
    if len(arr) < 2:
        return arr

    m_i = len(arr)//2
    left = mergesort(arr[:m_i])
    right = mergesort(arr[m_i:])
    arr = merging(left, right)
    return arr

def merging(left, right):
    global cnt
    merged, left, right= [], deque(left), deque(right)
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) and len(right):
        if left[0] > right[0]:
            merged.append(right.popleft())
        else:
            merged.append(left.popleft())

    merged += left if left else right
    return merged

for tc in range(1, int(input()) + 1):
    # 오름차순
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    arr = mergesort(arr)
    print(f'#{tc} {arr[n//2]} {cnt}')