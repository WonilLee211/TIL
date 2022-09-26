import sys
sys.stdin = open('input.txt')

def HoarePartition(arr, l, r):
    p = arr[l]
    i, j = l, r

    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j: arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def qsort(arr, l, r):
    if l < r:
        s = HoarePartition(arr, l, r)
        qsort(arr, l, s - 1)
        qsort(arr, s + 1, r)

n = 1000000
arr = list(map(int, input().split()))
qsort(arr, 0, n - 1)
print(arr[500000])