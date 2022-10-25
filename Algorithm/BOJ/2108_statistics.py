'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이

n = 1 ~ 5000000 사이 홀수
절대값이 4000이 넘지않는 정수 n개

논리
- 일단 입력값만 봐도 O(n)이 2초가 넘음
-


'''
import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

sorted_nums = sorted(nums)

cnt_list = [0 for i in range(n)]
for i in range(n - 1):
    if sorted_nums[i] == sorted_nums[i + 1]:
        cnt_list[i + 1] = cnt_list[i] + 1

max_frequency = max(cnt_list)
max_fre_list = []
for i in range(n):
    if max_frequency == cnt_list[i]:
        max_fre_list.append(sorted_nums[i])

mean = round(sum(nums)/n)
center_num = sorted_nums[n//2]
max_freq_num = 0
if len(max_fre_list) > 1:
    max_freq_num = max_fre_list[1]
else:
    max_freq_num = max_fre_list[0]
range_nums = max(nums) - min(nums)

print(mean)
print(center_num)
print(max_freq_num)
print(range_nums)