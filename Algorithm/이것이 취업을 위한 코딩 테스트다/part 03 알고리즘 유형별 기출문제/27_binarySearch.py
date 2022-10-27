'''
n 개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어있음
x가 등장하는 횟수

O(logN)으로 설계하기

논리
- 최대 100만개니까 이진탐색으로
- 가운데에서부터 나눠서 탐색

'''

import sys
sys.stdin = open('input.txt')

n, target = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0     # target의 개수를 저장할 변수

def binary_search(fr, to):
    global cnt
    i = (to + fr)//2


    if arr[i] == target:
        cnt = 1
        j, k = i - 1, i + 1
        # target을 찾은 곳에서 양방향으로 세기
        while j >= 0 and arr[j] == target:
            cnt += 1
            j -= 1
        while k < n and arr[k] == target:
            cnt += 1
            k += 1

    elif cnt == 0 and i != to and arr[i] > target: # 가운데 인덱스를 찾는 것을 반복하는 걸 방지
        binary_search(fr, i)
    elif cnt == 0 and fr != i and arr[i] < target:
        binary_search(i, to)

binary_search(0, n - 1)

if cnt == 0:
    print(-1)
else:
    print(cnt)
