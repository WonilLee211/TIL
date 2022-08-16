import sys
sys.stdin = open('input.txt')

c, r = map(int, input().split())
n = int(input())

matrix = list([0] * c for _ in range(r))


cnt = 0

