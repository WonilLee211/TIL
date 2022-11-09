import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque


n, x = map(int, input().split())

lklst = [[] for i in range(n + 1)]

for i in range(n - 1):
    tmp = list(map(int, input().split()))
    lklst[tmp[0]].append((tmp[1], tmp[2]))
    lklst[tmp[1]].append((tmp[0], tmp[2]))

min_cost = 20

for i in range(1, n + 1):

    nodecost = 0
    visited = 1 << i
    q = deque()
    q.append([i, x])

    while q:

        node, X = q.popleft()

        for k in range(22):
            if X & (1 << k):
                nodecost += 1
            elif X < (1 << k):
                break

        if nodecost > min_cost:
            break

        for arr in lklst[node]:
            j, link = arr[0], arr[1]
            if visited & (1 << j):
                continue
            visited |= 1 << j
            q.append([j, X ^ link])

    if nodecost < min_cost:
        min_cost = nodecost

print(min_cost)