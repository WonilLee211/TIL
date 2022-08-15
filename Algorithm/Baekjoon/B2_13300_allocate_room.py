import sys
sys.stdin = open('input.txt')

'''
한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때,
조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램
'''
N, K = map(int, input().split())
students = list([0, 0] for _ in range(6))
cnt = 0

for i in range(N):
    sex, grade = map(int, input().split())
    students[grade-1][sex] += 1

for subtotal in students:
    for i in range(2):
        t, v = divmod(subtotal[i], K)
        cnt += t
        if v:
            cnt += 1

print(int(cnt))