import sys
sys.stdin = open("input.txt")

'''



'''

n = int(input())

adjList = [[] for i in range(n + 1)]

for i in range(n):
    p, c, w = map(int, input().split())
    adjList[p].append((c, w))
    adjList[c].append((p, w))


