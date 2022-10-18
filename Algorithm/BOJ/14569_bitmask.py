'''
수강신청
비어있는 시간에 어떤 과목이 추가로 신청할 수 있는 과목의 후보 개수를 구하자
후보 개수를 세는 것으로 현재 내 시간표에서 신청할 수 있는 과목끼리 시간이 겹치더라도 모두 센다.
월요일 1, 2, 3, 4, 5교시 시간이 비어 있고 한 과목의 시간이 월요일 1, 2, 3, 4교시이고
 나머지 한 과목의 시간이 월요일 2, 3, 4, 5교시라면 2과목 모두 후보가 될 수 있다.

n : 과목 수 3 ~ 1000
k, ti  : n줄에 걸친 각 과목의 수업시간의 수,  k개의 수업이 진행되는 교시
월요일 1~10교시: 1~10, 화요일 1~10교시: 11~20, …
m : 학생 수
p, qi = m 줄에 걸친 학생의 비어있는 교시 갯수, p개의 비어있는 교시

학생별 들을 수 있는 과목 개수

논리
- 입력값들의 범위가 굉장히 크다.
- 비교를 시간을 비트에 표시하고 비교
- 모두 같다면 카운트
- 하나라도 틀리면 제외

틀린 점
- 자리수 맞출 때 50칸만 만들면 된다고 생각했는데 밀어내는 수에도 50이 있어서
51칸을 밀어내야했다.
'''
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
t = 1 << 51
subjects = [0 for i in range(n)]

for i in range(n):
    subjects[i] = list(map(int, input().split()))[1:]

m = int(int(input()))

# 학생이 가능한 시간을 비트에 표시하기
students = [t for i in range(m)]
for i in range(m):
    temp = list(map(int, input().split()))
    for j in temp[1:]:
        students[i] |= 1<<j

# 학생별로 과목별 모든 시간과 일치하면 cnt
# 하나라도 틀리면 pass
for student in students:
    cnt = 0
    for subject in subjects:

        for time in subject:
            if not(student & (1<<time)):
                break
        else:
            cnt += 1

    print(cnt)