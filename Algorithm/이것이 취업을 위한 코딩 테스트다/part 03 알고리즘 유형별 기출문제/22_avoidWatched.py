import sys
sys.stdin = open('input.txt')

'''
선생님, 학생, 장애물
몇 명의 학생들은 수업시간에 몰래 복도로 빠져나왔는데, 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표
각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 
단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다.
또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정

NxN 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램

입력 
n : (3 ≤ N ≤ 6)
해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X

출력
첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력
"YES", 그렇지 않다면 "NO"를 출력

논리
- 학생 위치 저장
- 선생님 위치 저장
- teacher의 감시 범위 인덱스 저장
- 인덱스 3개 조합만들어서 벽 세우고 테스트하기
- 

'''

import sys

input = sys.stdin.readline

n = int(input())

student = []
teacher = []
corridor = []
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    row = input().split()
    corridor.append(row)

    for j in range(n):
        if row[j] == "S":
            student.append((i, j))
        elif row[j] == "T":
            teacher.append((i, j))

watchline = []

for i, j in teacher:

    for dr, dc in move:
        r, c = i, j

        while True:

            r, c = r + dr, c + dc

            if not(0 <= r < n) or not(0 <= c < n) or corridor[r][c] == "S":
                break

            watchline.append((r, c))



m = len(watchline)
flag = True

for i in range(1, 1<<m):
    case = []
    for j in range(m):
        if i & (1 << j):
            case.append(watchline[j])

    if len(case) != 3:
        continue

    find_student = False

    for r, c in teacher:

        for dr, dc in move:
            nr, nc = r, c
            while True:
                nr, nc = nr + dr, nc + dc
                if not(0 <= nr < n) or not(0 <= nc < n) or (nr, nc) in case:
                    break

                elif (nr, nc) in student:
                    find_student = True
                    break

            if find_student:
                break
        if find_student:
            break

    if not find_student:
        print("YES")
        flag = False
        break


if flag:
    print("NO")



