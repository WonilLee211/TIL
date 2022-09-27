import sys
sys.stdin = open('input.txt')

def hoarepartition(arr, lo, hi):

    i, j = lo + 1, hi
    pivot = arr[lo]

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]

    return j

def quicksort(arr, lo, hi):
    if lo < hi:
        s = hoarepartition(arr, lo, hi)
        quicksort(arr, lo, s - 1)
        quicksort(arr, s + 1, hi)

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, n - 1)
    print(f'#{tc} {arr[n//2]}')