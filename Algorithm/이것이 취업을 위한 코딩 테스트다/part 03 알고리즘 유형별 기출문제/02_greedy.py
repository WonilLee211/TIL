'''

0이 아닌 수와 하나를 더하고 나머지는 다 곱하기

'''
import sys
sys.stdin = open("input.txt")
arr = list(map(int, input()))
print(arr)
arr.sort()
ans = 1
for d in arr:
    if d == 0:
        continue

    ans *= d

print(ans)