import sys
sys.stdin = open('input.txt')
import heapq as hq

n, m = map(int, input().split())
arr = list(range(1, n + 1))
res = []
a_hq = []
b_hq = []
priority = {}

for _ in range(m):
    a, b = map(int, input().split())
    priority[b] = a
    hq.heappush(a_hq, a)
    arr.remove(a)

keys = priority.keys()

while a_hq or arr:
    if a_hq:
        res.append(hq.heappop(a_hq))
    
    if arr[0] in keys:
        if priority[arr[0]] not in res:
            continue
    res.append(hq.heappop(arr))        

print(*res)