import sys
sys.stdin = open('input.txt')

'''
규칙
1. 별(4)이 많은 쪽이 이김
2. 별이 같다면 동그라미(3)가 많은 쪽
3. '' 네모(2)가 많은 쪽
4. 세모(1)가 많은 쪽
5. 모두 같다면 무승부 -> D 출력
A, B 중 승자 출력

라운드의 수 N과 두 어린이가 순서대로 내는 딱지의 정보가 주어졌을 때, 
각 라운드별로 딱지놀이의 결과를 구하는 프로그램을 작성하시오.
'''
from collections import deque

N = int(input())
def selection_sort(arr):
    M = len(arr)

    for i in range(M-1):
        max_idx = i
        for j in range(i, M):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr

for _ in range(N):
    num_a, a_cards = input().split(maxsplit=1)
    num_b, b_cards = input().split(maxsplit=1)

    a_cards = deque(selection_sort(a_cards.split()))
    b_cards = deque(selection_sort(b_cards.split()))

    while a_cards and b_cards:
        a = a_cards.popleft()
        b = b_cards.popleft()
        if a > b:
            print('A')
            break
        elif a < b:
            print('B')
            break

    else:
        if a_cards:
            print('A')
        elif b_cards:
            print('B')
        else:
            print('D')