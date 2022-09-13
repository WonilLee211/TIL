import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    last += 1
    heap[last] = n


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    last = 0
    heap = [0] * (n+1)