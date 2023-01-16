'''

일단 현재 기준점보다 큰 인덱스부터 나랑 다르다면 카운트하면 됨

'''
import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ball_weights = sorted(list(set(arr)))

cnt = 0

for idx1, d1 in enumerate(arr):
    for idx2, d2 in enumerate(arr):
        if idx1 >= idx2:
            continue

        if d1 != d2:
            cnt += 1

print(cnt)