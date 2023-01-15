'''

주어진 수에서 연속된 0의 개수, 연속된 1의 개수를 세고 그 중 작은 값이 답

'''


import sys
sys.stdin = open("input.txt")

arr = list(map(int, input()))
n = len(arr)

cnt_dict = {0:0, 1:0}
now = arr[0]

for idx, d in enumerate(arr[1:]):
    if d != now:
        cnt_dict[now] += 1
        now = d
    if idx == n - 2:
        cnt_dict[now] += 1

print(min(cnt_dict.values()))