def SelectionsSort(s):
    if s == n-1:
        return

    MinI = s

    for j in range(s+1, n):
        if arr[MinI] > arr[j]:
            MinI = j
    arr[MinI], arr[s] = arr[s], arr[MinI]
    SelectionsSort(s+1)


arr = [7, 1, 3, 5, 8, 6, 4, 2]
n = len(arr)
SelectionsSort(0)
print(arr)