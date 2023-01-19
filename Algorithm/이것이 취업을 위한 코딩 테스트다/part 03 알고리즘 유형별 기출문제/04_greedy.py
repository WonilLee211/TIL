'''
1. 1 부터 시작해서 주어진 숫자로 만들기
못만들면 프린트
만들면 다음 수로 넘어가기

2. 이차원 누적합을 이용해서

n이 1000개 미만이니까 모든 수의 누적합으로 계산해서 비어있는 자연수 중 가장 작은 값 출력

'''
import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 1

for d in arr:

    if ans < d:
        break
    ans += d

print(ans)
