import sys
sys.stdin = open('input.txt')

'''
톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다
마주보는 톱니가 다른 극일 때 회전하게 됨

입력 
- 첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태
- 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로
- N극은 0, S극은 1
- 다섯째 줄에는 회전 횟수 K
다음 K개 줄에는 회전시킨 방법
두 개의 정수 : 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향
- 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향

총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합
- 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
- 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
- 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
- 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
-------
논리
- g번 톱니를 r방향으로 회전시킬 때 4 개의 기어를 회전 여부와 방향 정보를 저장
-  왼쪽기어 2번 톱니와 오른쪽 기어의 6번 톱니 비교
    - 다르다면 회전
- 저장된 변화 정보 업데이트

'''

import collections

deque = collections.deque

gears = [0] + list(deque(map(int, list(input()))) for i in range(4))

k = int(input())
rotate_info = list(list(map(int, input().split())) for i in range(k))

def rotate_gear(g, r): # 톱니 번호 g별  r방향으로 회전시키는 함수
    temp = gears[g]
    if r == 1:
        temp.appendleft(temp.pop())
        gears[g] = temp
    else:
        temp.append(temp.popleft())
        gears[g] = temp

for rotate in rotate_info:
    change_info = [''] * 5 # 1 시계방향 회전, -1 반시계방향 회전, 0 회전하지 않음. '' 방문하지 않음

    # 주변 톱니가 움직이는지 확인
    stack = []
    stack.append(rotate)
    while stack:
        rotated = stack.pop()
        change_info[rotated[0]] = rotated[1] # 회전하게되는 바퀴 정보 저장

        for other in [rotated[0] - 1, rotated[0] + 1]: # 회전할 톱니의 양쪽 인덱스

            if other not in list(range(1, 5)) or change_info[other] != '': # 인덱스 양쪽이 중에 1 ~ 4번호를 벗어나거나 방문했다면 패스
                continue

            if other > rotated[0] and gears[rotated[0]][2] != gears[other][6]:   # 회전할 바퀴보다 오른쪽에 있고 마주보는 톱니가 극성이 다른 경우
                stack.append([other, -rotated[1]])                               # 다음 점검 대상으로 담기
                change_info[other] = -rotated[1]                                 # 회전 정보 담기
            else:                                                                # 회전하지 않을 경우
                change_info[other] = 0

            if other < rotated[0] and gears[rotated[0]][6] != gears[other][2]: # 회전할 바퀴보다 왼쪽에 있고 마주보는 톱니가 극성이 다른 경우
                stack.append([other, -rotated[1]])
                change_info[other] = -rotated[1]
            else:
                change_info[other] = 0

    for g, r in enumerate(change_info[1:]): # 회전해야하는 바퀴 일 때 rotate_gear 함수 실행
        if r in [1, -1]:
            rotate_gear(g + 1, r)

total = 0
for idx, gear in enumerate(gears[1:]):      # 12시 방향 톱니 계산
    if gear[0] == 1:
        total += 2 ** idx

print(total)
