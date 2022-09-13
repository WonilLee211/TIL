def find_root(n):
    for i in range(1, v+1):
        if p[i] == 0:
            return i

def preorder(n):

    if n:
        print(n, end=' ')
        preorder(c1[n])
        preorder(c2[n])

v = int(input())
e = v - 1
arr = list(map(int, input().split()))

c1 = [0] * (v + 1)
c2 = [0] * (v + 1)
p = [0] * (v + 1)

for i in range(0, e*2, 2):
    if c1[arr[i]] == 0:
        c1[arr[i]] = arr[i + 1]
    else:
        c2[arr[i]] = arr[i + 1]
    p[arr[i+1]] = arr[i]

root = find_root(arr[-1])
preorder(root)