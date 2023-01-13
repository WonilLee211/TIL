'''
여행을 함께 떠날 수 있는 그룹 수의 최댓값
공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음


'''
import sys
sys.stdin = open("input.txt")

n = int(input())
members = list(map(int, input().split()))
members.sort(reverse=True)

no_groups = 0
max_v = members[0]
for i in range(n + 1):

    if i == max_v:
        no_groups += 1
        max_v += members[i - 1]

print(no_groups)