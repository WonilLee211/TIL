'''
R = 뒤집기
D = 첫번째 수 버리기


배열의 초기값과 수행할 함수 주어질 때 최종 결과를 구하는 프로그램

논리
- 제한 시간 1초
- 연산 배열은 1~1000000개
- 숫자 배열 0 ~ 1000000개
- R이 나오면 삭제할 위치를 바꾼다.
- D가 나오면 배열 자르기 또는 pop 시키기
- 시간을 줄이기 위해서 중복되서 나오는 경우 중복되는 수를 세기

주의할 점
- 함수를 조합해서 한번에 사용할 수 있음
'''

import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(int(input())):
    rd = input()
    n = int(input())
    arr = input()[1:-1]
    if len(arr) != 0:
        arr = deque(arr.split(','))

    m = len(rd)
    cnt_R = rd.count('R')
    cnt_D = m - cnt_R       # D 갯수

    if cnt_D > len(arr):
        print('error')
        continue
    elif cnt_D == len(arr):
        print('[]')
        continue

    reverse = False
    for op in rd:
        if op == 'R':
            reverse = not reverse
        else:
            if not reverse:
                arr.popleft()
            else:
                arr.pop()

    if reverse:
        arr = list(arr)[-1::-1]

    print('[' + ','.join(arr) + ']')





'''
for tc in range(int(input())):
    rd = input()
    n = int(input())
    arr = input()[1:-1]

    if len(arr) != 0:
        arr = arr.split(',')

    # print(arr)
    idx = 0
    ans = ''
    length = len(rd)
    while len(rd) > 1:
        i = 1

        # 중복 갯수 세기
        while length > i and rd[i] == rd[i - 1]:
            i += 1

        # 방향 정하기
        if rd[0] == 'R':
            idx = -(idx + (i % 2))
        else:
            if i > len(arr):
                ans = 'error'
                break
            elif idx == 0:
                arr = arr[i:]
            else:
                arr = arr[:-i]

        rd = rd[i:]
        length = len(rd)

    if ans == 'error':
        print('error')
        continue

    if len(rd) != 0:
        if rd[0] == 'R':
            idx = -(idx + 1)
        else:
            if len(arr) == 0:
                ans = 'error'
            elif idx == 0:
                arr = arr[1:]
            else:
                arr = arr[:-1]

    if ans == 'error':
        print('error')
        continue

    if idx == -1:
        ans = arr[-1::-1]
    else:
        ans = arr
    print('[' + ','.join(list(ans)) + ']')

'''