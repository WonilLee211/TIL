import sys
sys.stdin = open("input.txt")


'''
10,000 이하의 자연수로 이루어진 길이 N짜리 수열
연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램

N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)

크거나 같을 땐 시작점 줄이기
작을 땐 끝 점 증가시키기
끝에 도달했을 때 중단

'''

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start = end = 0
ans = int(1e6) + 1

acc = 0

while True:
    if acc >= s:
        acc -= arr[start]
        start += 1
        ans = min(ans, end - start + 1)
    elif end == n:
        break
    else:
        acc += arr[end]
        end += 1

if ans == int(1e6) + 1:
    print(0)
else:
    print(ans)