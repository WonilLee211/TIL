'''
고정점 : 그 값이 인덱스와 동일한 원소를 의미
수열 a = {-15, -4, 3, 8, 13}
오름차순으로 정렬되어있음

논리
- 가운데 인덱스부터 시작
- 가운데 인덱스와 그 값이 같다면 고정점 발견
- 가운데 인덱스와 그 값이 다르다면
    - 가운데 인덱스가 그 값보다 크면 현재 인덱스보다 큰 부분을 탐색
    - 가운데 인덱스가 그 값보다 작으면 현재 인덱스보다 큰 부분을 탐색
'''

import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
idx = -1

def binary_search(fr, to):
    global idx

    i = (fr + to) // 2

    if arr[i] == i:
        idx = i
    elif to != i and arr[i] > i:
        binary_search(fr, i)
    elif fr != i and arr[i] < i:
        binary_search(i, to)

binary_search(0, n - 1)
print(idx)