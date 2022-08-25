import sys
sys.stdin =open('input.txt')

# a-f : 1-6
# c-e : 3-5
# b-d : 2-4

n = int(input())
linklist = []

for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
