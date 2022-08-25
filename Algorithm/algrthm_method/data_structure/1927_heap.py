import heapq
import sys
sys.stdin = open('1927.txt')
n = int(sys.stdin.readline())

heap = []

for i in range(n):
    tmp = int(sys.stdin.readline())

    if tmp > 0:
        heapq.heappush(heap, tmp)
    elif tmp == 0:
        try:
            p = heapq.heappop(heap)
            print(p)
        except:
            print(0)

